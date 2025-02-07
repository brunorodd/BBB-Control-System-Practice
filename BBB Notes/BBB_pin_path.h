// BBB header file for GPIO/ADC/etc pins
// written by Bruno Rodriguez

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Digital Pin Paths (remember to concatenate the value when using fprintf and other sort) and configure direction to either "in" or "out"
// eg. echo "out" > direction in the directory and then "echo 1 >value" to turn it high
#define GPIO61_PATH  "/sys/class/gpio/gpio61"  // P8.26
#define GPIO60_PATH  "/sys/class/gpio/gpio60"  // P9.12
#define GPIO66_PATH  "/sys/class/gpio/gpio66"  // P8.7
#define GPIO65_PATH  "/sys/class/gpio/gpio65"  // P8.15
#define GPIO67_PATH  "/sys/class/gpio/gpio67"  // P8.8
#define GPIO68_PATH  "/sys/class/gpio/gpio68"  // P9.10
#define GPIO69_PATH  "/sys/class/gpio/gpio69"  // P8.9
#define GPIO44_PATH  "/sys/class/gpio/gpio44"  // P8.12
#define GPIO45_PATH  "/sys/class/gpio/gpio45"  // P8.11
#define GPIO46_PATH  "/sys/class/gpio/gpio46"  // P8.16
#define GPIO47_PATH  "/sys/class/gpio/gpio47"  // P8.15
#define GPIO48_PATH  "/sys/class/gpio/gpio48"  // P9.15
#define GPIO49_PATH  "/sys/class/gpio/gpio49"  // P9.23
#define GPIO27_PATH  "/sys/class/gpio/gpio27"  // P8.17
#define GPIO20_PATH  "/sys/class/gpio/gpio20"  // P9.41
#define GPIO117_PATH "/sys/class/gpio/gpio117" // P9.25
#define GPIO115_PATH "/sys/class/gpio/gpio115" // P9.27
#define GPIO112_PATH "/sys/class/gpio/gpio112" // P9.30
#define UART1_TXD    "/sys/class/gpio/gpio15"  // P9.24
#define UART1_RXD    "/sys/class/gpio/gpio14"  // P9.26
#define UART4_RXD    "/sys/class/gpio/gpio30"  // P9.11
#define UART4_TXD    "/sys/class/gpio/gpio31"  // P9.13

// PWM Output Pins (subclasses: enable capture device duty_cycle period polarity)
// eg. echo 1 > /sys/class/pwm/pwmchip1/pwm-1:0 
#define SPI0_D0   "/sys/class/pwm/pwmchip0/pwm-0:0"
#define SPI0_SCLK "/sys/class/pwm/pwmchip0/"
#define EHRPWM1A  "/sys/class/pwm/pwmchip1/pwm-1:0" // P9.14 
#define EHRPWM1B  "/sys/class/pwm/pwmchip1/pwm-1:1" // P9.16

// ADC pin paths
#define AIN0_PATH "/sys/bus/iio/devices/iio:device0/in_voltage_raw0"
#define AIN1_PATH "/sys/bus/iio/devices/iio:device0/in_voltage_raw1"
#define AIN2_PATH "/sys/bus/iio/devices/iio:device0/in_voltage_raw2"
#define AIN3_PATH "/sys/bus/iio/devices/iio:device0/in_voltage_raw3"
#define AIN4_PATH "/sys/bus/iio/devices/iio:device0/in_voltage_raw4"
#define AIN5_PATH "/sys/bus/iio/devices/iio:device0/in_voltage_raw5"
#define AIN6_PATH "/sys/bus/iio/devices/iio:device0/in_voltage_raw6"

// Continuous ADC Voltage reading enable 
#define AIN0_EN_PATH "/sys/bus/iio/devices/iio\:device0/scan_elements/in_voltage0_en"
#define AIN1_EN_PATH "/sys/bus/iio/devices/iio\:device0/scan_elements/in_voltage1_en"
#define AIN2_EN_PATH "/sys/bus/iio/devices/iio\:device0/scan_elements/in_voltage2_en"
#define AIN3_EN_PATH "/sys/bus/iio/devices/iio\:device0/scan_elements/in_voltage3_en"
#define AIN4_EN_PATH "/sys/bus/iio/devices/iio\:device0/scan_elements/in_voltage4_en"
#define AIN5_EN_PATH "/sys/bus/iio/devices/iio\:device0/scan_elements/in_voltage5_en"
#define AIN6_EN_PATH "/sys/bus/iio/devices/iio\:device0/scan_elements/in_voltage6_en"

// Buffer Enable for continuous reading ADC (https://www.teachmemicro.com/beaglebone-black-adc/  - BeagleBone Black ADC Continuous Reading)
#define BUFFER_LENGTH_FILL "/sys/bus/iio/devices/iio\:device0/buffer/length" // set it to 100 in the echo 
#define BUFFER_EN 		   "/sys/bus/iio/devices/iio\:device0/buffer/enable" // set to 1

//Additional Reconfigurable Digital Pins 
#define GPIO2_PATH    "/sys/class/gpio/gpio2"
#define GPIO3_PATH    "/sys/class/gpio/gpio3"
#define GPIO4_PATH    "/sys/class/gpio/gpio4"
#define GPIO5_PATH    "/sys/class/gpio/gpio5"
#define GPIO7_PATH    "/sys/class/gpio/gpio7"
#define GPIO15_PATH   "/sys/class/gpio/gpio15"
#define GPIO14_PATH   "/sys/class/gpio/gpio14"
#define GPIO48_PATH   "/sys/class/gpio/gpio48"
#define GPIO51_PATH   "/sys/class/gpio/gpio51"
#define GPIO125_PATH  "/sys/class/gpio/gpio125"
#define GPIO22_PATH   "/sys/class/gpio/gpio22"
#define GPIO23_PATH   "/sys/class/gpio/gpio23"
#define GPIO28_PATH   "/sys/class/gpio/gpio28"
#define GPIO50_PATH   "/sys/class/gpio/gpio50"



void write_pin(char filename[], char value[], char pin_path[]){
   FILE* fp;   // create a file pointer fp
   char  fullFileName[100];  // to store the path and filename
   sprintf(fullFileName, pin_path "%s", filename); // write path and filename
   fp = fopen(fullFileName, "w+"); // open file for writing
   fprintf(fp, "%s", value);  // send the value to the file
   fclose(fp);  // close the file using the file pointer
   }
