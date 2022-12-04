import os
import sys



def main():
    
    filename = "./App.java"
    file = open(filename, "r")
    loops = 0
    for line in file:
        if "for" in line or "while" in line:
            loops = loops+1
    
    
    output = "Expecting " + str(loops) + " kg of CO2"
    #sys.stdout.write(f'::set-output name=output::{output}\n')
    print(output)
    sys.exit(0)


if __name__ == "__main__":
    main()
