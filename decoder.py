import decoder_lib as decoder
import zigzag_lib as ziggy

import huffman_lib as huffman
import getopt
import sys

def main(argv):
    inputFile = ""
    qsize = ""

    # load file with command line args
    try:
        opts, args = getopt.getopt(argv, "i:q:")
    except getopt.GetoptError:
        print("USAGE: python3 decoder.py -i <file> -q <qsize>")
        sys.exit()

    for opt, arg in opts:
        if opt == "-i":
            inputFile = arg
        elif opt == "-q":
            qsize = int(arg)
        else:
            print("USAGE: python3 decoder.py -i <file> -q <qsize>")
            sys.exit()

    if (inputFile is ""):
        print("USAGE: python3 decoder.py -i <file> -q <qsize>")
        sys.exit()

    # decode huffman back into text
    print("Decoding .bit file...")
    #dec = huffman.Decoder(inputFile)
    #dec.decode_as("raw_inverse.txt")
    print("\tDecoding complete!")

    # read imgDCTZ back in
    print("Loading zig-zagged DCT array...")
    imgDCTZ = decoder.np.loadtxt("raw_inverse.txt")
    print("\tArray loaded!")

    # reverse zig-zag
    print("Unpacking zigged matrix...")
    imgDCT = ziggy.iZigRedux(imgDCTZ, qsize)
    print("\tMatrix unpacked!")

    print("Reversing DCT...")
    imgInverse = decoder.cv2.idct(imgDCT.astype(float))
    imgRecon = decoder.Image.fromarray(imgInverse.astype("uint8"))
    imgRecon.show()

if __name__ == "__main__":
    main(sys.argv[1:])
