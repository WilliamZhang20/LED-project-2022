# Raspberry-Pi-Projects

A collection of all the projects that I do using a Raspberry Pi

## LED Project (July 2022)
In this project, I programmed a set of six LED lights using a Raspberry Pi to randomly light up individual LEDs. When the user runs the code, the program will randomly select one of the six LEDs and turn it on for 0.7 seconds. This is done 50 times, and each time, the program will select a different random light. 

The circuit board is set up on a breadboard, and uses only 3 GPIO (General Purpose Input-Output) pins to light 6 LED individually. This is possible with a techinique called [Charlieplexing](https://www.instructables.com/Charlieplexing-the-Arduino/), in which simply making current flow between various combinations of pins can light up more lights than there are pins. 

For example, with 3 pins, there are 6 combinations. If the pins were numbered 1 to 3, current can be run in combinations 1-2, 1-3, 2-3, 2-1, 3-1, 3-2. So long as the other pin in those combinations is set to high impedance mode (in which no current is allowed through), then current is guaranteed to flow between those chosen pins. Therefore, 6 lights could be lit up that way.

## Camera Project (July 2022)
In this project, I controlled the Raspberry Pi Camera Module to take photos at random time intervals between 4 and 10 seconds. Each time, the program will send the photo to my email as an attachment. To open the photo, simply download and open in browser.
