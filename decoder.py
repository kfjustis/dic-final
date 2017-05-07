import decoder_lib as decoder
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
    '''
    x = decoder.np.array([[1,2,3],[4,5,6],[7,8,9]], decoder.np.int8)
    print(x)
    newMat = ziggy.printZMatrix(x)
    print(newMat)
    newMat2D = decoder.np.reshape(newMat, (3,3))
    print(newMat2D)
    '''

    # just having fun - read in anyway lol
    print("Loading image...")
    imgDCT = decoder.np.reshape(imgDCTZ, (512,512))
    imgInverse = decoder.cv2.idct(imgDCT)
    imgRecon = decoder.Image.fromarray(imgInverse)
    imgRecon.show()

if __name__ == "__main__":
    main(sys.argv[1:])
