import os
import sys



def main():
    filename = "./main.py"
    file = open(filename, "r")
    output = file.read()
    
    
    
    sys.stdout.write(f'::set-output name=output::{output}\n')

    sys.exit(0)


if __name__ == "__main__":
    main()
