from os.path import join
from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
framework_dir = env.PioPlatform().get_package_dir("framework-circle2")

env.Append(
    CPPPATH=[
        join(framework_dir, "include"),
        join(framework_dir, "addon")
    ],
    LIBPATH=[join(framework_dir, "lib")],
    LIBS=["circle"]
)

env.Append(
    LINKFLAGS=[
        "-T", join(framework_dir, "boards", f"{env.BoardConfig().get('build.variant')}.ld"),
        "-nostdlib",
        "-nostartfiles",
        "-Wl,--gc-sections"
    ]
)

env.AddPostAction(
    "$BUILD_DIR/${PROGNAME}.elf",
    env.VerboseAction(
        "arm-none-eabi-objcopy -O binary $BUILD_DIR/${PROGNAME}.elf $BUILD_DIR/kernel.img",
        "Building kernel.img"
    )
)
