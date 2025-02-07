# ADC:

BBB\_ADC.py is the original file written by Bruno. Slightly modified to show which outputs are coming from which pins.

ADC1.py shows the values read into the BBB from Pin 33 on the P9 header. Shows both raw and ADC values. This value comes from the output of Pin 1 on the joystick.

ADC2.py shows the values read into the BBB from Pin 35 on the P9 header. This value comes from the output of Pin 2 on the joystick.


*the Analaog inputs cannot take more than 1.8V*  
ADC.read returns a normalized value of the input between 0 and 10  
ADC.read_raw returns the actual value which is between 0 and 4095 (12 bits)  

The joystick labelled GFS appears to be a JC200 from P&G LTD UK and is discontinued. Datasheets do not give any details on the pinout of the D-Type connector.

Attempting to interpret the ADC readings:

Assuming GFS label facing to the left

Pin 1

Centered:  
P1: 0.55  
P1R: 2252.0  

Forward:  
P1: 0.662  
P1R: 2714.0  

Backwards:  
P1: 1830.0  
P1R: 0.447  

Right, Left:  
There are very little changes to the values from the centered position so i will assume ADC1 is a speed output and so the values only change when the joystick is in the forward or backwards orientation as lateral movement has no effect on the speed.

-------------------------------------------------
Pin 2

Centered:
P2: 0.544  
P2R: 2229.0  

Right:  
0.66  
2704.0  

Left:  
0.435  
1783.0  

The forward and backward now have very little changes to the value from the centered position, so this is like the opposite of the first ADC pin. This will likely be used to control the amount of turn wanted in the wheels.



NOTE: The 9-way D Type Pin-out in the OMNI Manual(page 168) has a different pinout configuration than the PCB\_DAC.pdf.

OMNI -> PCB\_DAC
1 -> 5	Joystick Speed  
2 -> 4	Joystick Direction  
3 -> 3	Joystick Reference  
4 -> 2		-  
5 -> 1	Detect  
6 -> 9	Fifth Switch   
7 -> 8	12V 100mA  
8 -> 7	Joystick Ground  
9 -> 6	Connected to 7 (12V 100mA)  

Joystick Speed and Joystick Direction will be where the Analog outputs of our DAC on the shield will go. Again see the OMNI Manual for these specifications when needed. Page 168.


#SPI

Intended SPI Pin Configuration
SPI1:  
CS: P9\ 23  
DI: P9\ 18  
SCLK: P9\ 22  

SPI2:  
CS: P9\ 27  
DI: P9\_30  
SCLK: P9\_31  

Our SPI configuration differs slightly from the standard spi configuration and what you will see in most tutorials.  
- We are only using SPI for data input so do not worry about the pins labelled DO(data output) in tutorials  
- We are not using the usual Chip Select Pins shown in tutorials either, although they are configured.  
- We are esentially simulating the chip select function by using GPIO pins and holding them high when idle and dropping low when writing  

Understanding highByte:
-takes in number and outputs 0 if it is less than 8 bits in length  
-if greater than 8 bits in length, bitwise shift which is equivalent to dividing by 2^8 and then bitwise and which will slice off any bits greater past the first 8


The DACs have an SPI interface. Our BBB will be the master which writes to the SDI on the DACs which are the slaves. Those DACs will then output a voltage proportional to the op-amp for amplification and into the OMNI  


