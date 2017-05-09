import encoder_lib as encoder
import zigzag_lib as ziggy

import huffman_lib as huffman
import getopt
import sys

def main(argv):
    inputFile = ""
    qsize = ""

    # load file with command line args
    try:
        opts, args = getopt.getopt(argv,"i:q:")
    except getopt.GetoptError:
        print("USAGE: python3 encoder.py -i <file> -q <qsize>")
        sys.exit()

    for opt, arg in opts:
        if opt == "-i":
            inputFile = arg
        elif opt == "-q":
            qsize = arg
        else:
            print("USAGE: python3 encoder.py -i <file> -q <qsize>")
            sys.exit()

    # error check command line args
    if inputFile is "":
        print("USAGE: python3 encoder.py -i <file> -q <qsize>")
        sys.exit()

    if qsize is "":
        print("USAGE: python3 encoder.py -i <file> -q <qsize>")
        sys.exit()

    if int(qsize) > 512:
        print("qsize cannot be greater than 512!")
        print("USAGE: python3 encoder.py -i <file> -q <qsize>")
        sys.exit()

    # load image as array
    print("Loading image...")
    imgArr = encoder.load_image_as_array(inputFile)
    print("\tImage loaded!")

    # apply DCT transform
    print("Applying DCT transform...")
    imgDCT = encoder.cv2.dct(imgArr.astype(float))
    print("\tTransform applied!")

    # zig-zag scan through array
    # store values to text file then feed that to huffman
    # and have it output its file - ENCODER DONE
    print("Encoding matrix...")
    imgDCTZ = ziggy.generateZigMatrix(imgDCT)

    if imgDCTZ is None:
        print("\tFailed to zig-zag! Please re-run the program with valid params.")
        sys.exit()

    encoder.np.savetxt("raw.txt", imgDCTZ)

    enc = huffman.Encoder("raw.txt")
    enc.write("image.bit")
    print("\tEncoding complete!")

if __name__ == "__main__":
    main(sys.argv[1:])
