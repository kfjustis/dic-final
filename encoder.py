import encoder_lib as encoder
import zigzag_lib as ziggy

import huffman_lib as huffman
import getopt
import sys

def main(argv):
    inputFile = ""

    # load file with command line args
    try:
        opts, args = getopt.getopt(argv,"i:")
    except getopt.GetoptError:
        print("USAGE: python3 encoder.py -i <file>")
        sys.exit()

    for opt, arg in opts:
        if opt == "-i":
            inputFile = arg
        else:
            print("USAGE: python3 encoder.py -i <file>")
            sys.exit()

    if (inputFile is ""):
        print("USAGE: python3 encoder.py -i <file>")
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
    imgDCTZ = ziggy.printZMatrix(imgDCT)
    encoder.np.savetxt("raw.txt", imgDCTZ)

    enc = huffman.Encoder("raw.txt")
    enc.write("image.bit")
    print("\tEncoding complete!")

if __name__ == "__main__":
    main(sys.argv[1:])
