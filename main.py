import os
import sys


def remove_last_occurrence(string: str, char: str):
    length = len(string)
    string2 = ''
    for i in range(length):
        if string[i] == char:
            string2 = string[0:i] + string[i + 1:length]
    return string2


def main():
    path = os.environ["INPUT_PATH"]

    paths = ''
    for root, dirs, files in os.walk(path):
        for file in files:
            paths = paths + '\"' + root + '/' + str(file) + '\", '

    paths = remove_last_occurrence(paths, ',')
    paths = "[" + paths + "]"
    sys.stdout.write(f'::set-output name=paths::{paths}\n')
    print(paths)

    sys.exit(0)


if __name__ == "__main__":
    main()