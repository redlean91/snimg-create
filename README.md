# snimg-create
This script is used to create the file to unlock the bootloader of Lenovo ZUI devices

Example: TB311FU, TB311XU, TB322FC

## How to use it
It's a simple command line program, arguments are:

**--sn1**: The first serial number of the bootloader

**--sn2**: The second serial number of the bootloader

**--output**/**-o**: Output path of where you want the sn.img to be (default: sn.img)

## Obtaining sn1 and sn2
Boot your device in fastboot mode and run:

`fastboot getvar all`

And you're gonna get the Bootloader's Serial Number in two parts, part 1 is **sn1** and part 2 is **sn2**.

## Code
I took the code for this from a website hosted on a random website that i don't have access to anymore, as i only have the html file of it.
