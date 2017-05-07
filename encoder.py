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
        print("USAGE: python3 main.py -i <file>")
        sys.exit()

    for opt, arg in opts:
        if opt == "-i":
            inputFile = arg
        else:
            print("USAGE: python3 main.py -i <file>")
            sys.exit()

    if (inputFile is ""):
        print("USAGE: python3 main.py -i <file>")
        sys.exit()

    # load image as array
    print("Loading image...")
    imgArr = encoder.load_image_as_array(inputFile)
    print("\tImage loaded!")

    # apply DCT transform
    print("Applying DCT transform...")
    imgArrFloat = imgArr.astype(float)
    imgDCT = encoder.cv2.dct(imgArrFloat)
    print("\tTransform applied!")

    # zig-zag scan through array
    # testing zig-zag
    '''
    x = encoder.np.array([[1,2,3],[4,5,6],[7,8,9]], encoder.np.int8)
    print(x)
    newMat = ziggy.printZMatrix(x)
    print(newMat)
    '''
    
    # I say just print values to text file then feed that to huffman
    # and have it output its file - ENCODER DONE

    # test inverse transform
    '''
    imgIDCT = cv2.idct(imgDCT)
    print(imgIDCT)
    imgOrig = imgIDCT.astype("uint8")
    print(imgOrig)
    pass1 = encoder.Image.fromarray(imgOrig)
    pass1.show()
    '''

    # test huffman coding
    '''
    testFile = "test1.txt"
    compdFile = "compd.scw"
    decompdFile = "test2.txt"
    enc = huffman.Encoder(testFile)
    enc.write(compdFile)
    enc.write("test_read.txt")
    dec = huffman.Decoder(compdFile)
    dec.decode_as(decompdFile)
    '''

if __name__ == "__main__":
    main(sys.argv[1:])
