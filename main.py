import os
import sys



def main():
    
    #filename = "./main.py"
    #file = open(filename, "r")
    #loops = 0
    #for line in file:
    #    if "for" in line or "while" in line:
    #        loops = loops+1
    
    
    output = "Expecting " + 10 + " kgs of CO2 output"
    sys.stdout.write(f'::set-output name=output::{output}\n')

    sys.exit(0)


if __name__ == "__main__":
    main()
