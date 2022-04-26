#!/usr/bin/env python

from rtlsrt import RtlSrt
from sys import argv


def raed_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except:
        return None


def create_output_file_path(path, over_write):
    if over_write:
        return path
    path = path[::-1]
    index = path.find(".")
    if index > 0:
        path = path[:index + 1] + "_modified"[::-1] + path[index + 1:]
    else:
        path = "_modified.srt"[::-1] + path
    return path[::-1]


def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)


if __name__ == "__main__":
    if len(argv) <= 1:
        print("An SRT file path is not provided in arguments.")
        exit(1)

    path = argv[1]
    file = raed_file(path)

    over_write = False
    if len(argv) > 2:
        over_write = str(argv[2]).lower() == "true"

    if file is None:
        print("File not found.")
        exit(1)

    try:
        rtl = RtlSrt(file=file)
    except:
        print("An error occured while parsing the SRT file.")
        exit(1)

    try:
        rtl.fix_rtl()
    except:
        print("An error occured while fixing the SRT file.")
        exit(1)

    try:
        output_file = rtl.compose()
    except:
        print("An error occured while composing the SRT file.")
        exit(1)

    try:
        output_path = create_output_file_path(path, over_write)
        write_file(output_path, output_file)
    except:
        print("An error occured while writing the SRT file.")
        exit(1)

    print("Successfully fixed the SRT file.")
    exit(0)
