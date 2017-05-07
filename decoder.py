import encoder_lib as encoder
import zigzag_lib as ziggy

import huffman_lib as huffman
import getopt
import sys

def main(argv):
    inputFile = ""

    # load file with command line args
    try:
        opts, args = getopt.getopt(argv, "i:")
    except getopt.GetoptError:
        print("USAGE: python3 decoder.py -i <file>")
        sys.exit()

    for opt, arg in opts:
        if opt == "-i":
            inputFile = arg
        else:
            print("USAGE: python3 decoder.py -i <file>")
            sys.exit()

    if (inputFile is ""):
        print("No file was read!\nUSAGE: python3 decoder.py -i <file>")
        sys.exit()

    print(str(inputFile))

if __name__ == "__main__":
    main(sys.argv[1:])
