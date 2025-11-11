#include <circle/startup.h>
#include <circle/gpiopin.h>
#include <circle/timer.h>
#include <circle/logger.h>

int main(void)
{
    CLogger logger;
    logger.Write("Blink example starting...");

    CGPIOPin led(47, GPIOModeOutput);
    CTimer timer;

    while (1)
    {
        led.Invert();
        timer.SimpleMsDelay(500);
    }

    return 0;
}
