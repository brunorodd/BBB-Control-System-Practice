#!/bin/bash
SHELL=/bin/bash
## BBB configure pins script
#ADC is already configured upon startup
sleep 1

# configure pins for the

# configure pins for spi
config-pin P9.17 spi_cs
config-pin P9.18 spi
config-pin P9.21 spi
config-pin P9.22 spi_sclk

config-pin P9.28 spi_cs
config-pin P9.29 spi
config-pin P9.30 spi
config-pin P9.31 spi_sclk

#configure pins for the uart on BBB
config-pin P9.11 uart
config-pin P9.13 uart

config-pin P9.24 uart
config-pin P9.26 uart

#configure pins for the pwm on the beaglebone
config-pin P9.42 pwm
config-pin P9.14 pwm
config-pin P9.16 pwm
config-pin P8.13 pwm
config-pin P8.19 pwm

#configure gpio pind for the BBB
config-pin P9.12 gpio
config-pin P9.15 gpio
config-pin P9.23 gpio
config-pin P9.25 gpio
config-pin P9.27 gpio
config-pin P9.41 gpio
config-pin P8.7  gpio
config-pin P8.8  gpio
config-pin P8.9  gpio
config-pin P8.10 gpio
config-pin P8.11 gpio
config-pin P8.12 gpio
config-pin P8.14 gpio
config-pin P8.15 gpio
config-pin P8.16 gpio
config-pin P8.17 gpio
config-pin P8.18 gpio
config-pin P8.26 gpio
config-pin P8.37 gpio
config-pin P8.38 gpio
config-pin P8.39 gpio
config-pin P8.40 gpio
config-pin P8.41 gpio
config-pin P8.42 gpio
config-pin P8.43 gpio
config-pin P8.44 gpio
config-pin P8.45 gpio
config-pin P8.46 gpio

# reconfigurable digital

#print statement to indicate pins commands have been executed
echo "pins configured"

sleep 1
exit
