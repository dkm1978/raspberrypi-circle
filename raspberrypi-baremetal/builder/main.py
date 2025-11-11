from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
env.Replace(
    AR="arm-none-eabi-ar",
    AS="arm-none-eabi-as",
    CC="arm-none-eabi-gcc",
    CXX="arm-none-eabi-g++",
    OBJCOPY="arm-none-eabi-objcopy",
    RANLIB="arm-none-eabi-ranlib",
    SIZETOOL="arm-none-eabi-size",
)

env.AddPostAction(
    "$BUILD_DIR/${PROGNAME}.elf",
    env.VerboseAction(
        "arm-none-eabi-objcopy -O binary $BUILD_DIR/${PROGNAME}.elf $BUILD_DIR/kernel.img",
        "Building kernel.img"
    )
)
