# snimg-create
# redlean91

import struct
import argparse
import sys

ENDIANESS = "<"

class sn:
    MAGIC = "1a2blenovo3c4d5e"
    
    @staticmethod
    def create(sn1: str = "", sn2: str = "", out_path: str = "") -> None:
        if len(sn1) != 32:
            print("The bootloader serial number 1 is not 32 chars!")
            sys.exit(1)

        if len(sn2) != 32:
            print("The bootloader serial number 2 is not 32 chars!")
            sys.exit(1)

        full_sn = sn1 + sn2
    
        buffer = b""
           
        buffer += sn.MAGIC.encode()
            
        # I dont know what these are but they're there so
        buffer += struct.pack(ENDIANESS+"IIIII", 0, 1, 0, 0, 1)
        
        # Bootloader serial number
        buffer += full_sn.encode()
        
        # garbage ig
        buffer += b'\0' * 256
        
        # saving it
        with open(out_path, "wb") as f:
            f.write(buffer)

def main():
    parser = argparse.ArgumentParser(description="sn.img Creator to unlock Lenovo ZUI devices bootloader.")

    parser.add_argument("--sn1", required=True, type=str, help="The first serial number of the bootloader")
    parser.add_argument("--sn2", required=True, type=str, help="The second serial number of the bootloader")
    parser.add_argument("--output", "-o", default="sn.img", type=str, help="Output file name (default: sn.img)")

    args = parser.parse_args()

    sn.create(args.sn1, args.sn2, args.output)
    
if __name__ == "__main__":
    main()
