### Thermal Printer Fortunes
A small python program to package up fortunes and quotes for a thermal receipt printer. The "device" currently has a single physical button that prints a random fortune with a random cowsay character constrained to the width of the 203dpi printer.

![a wise chicken](https://github.com/tegan-lamoureux/thermal-printer-fortune/blob/master/images/all_of_them.jpg)

#### Device
This is running on a Raspberry Pi 3 and communicates with a CSN-A2 thermal printer (see datasheets directory) over the Pi's mini uart, `/dev/ttyS0` @ 19200/8N1.

#### Todo:
* Add buffy/firefly/dr who quotes with appropriate ascii.
* Turn off weird men-women database and religious stuff from the fortunes program.
