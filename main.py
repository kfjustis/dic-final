import encoder

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

    # test inverse transform
    '''
    imgIDCT = cv2.idct(imgDCT)
    print(imgIDCT)
    imgOrig = imgIDCT.astype("uint8")
    print(imgOrig)
    pass1 = encoder.Image.fromarray(imgOrig)
    pass1.show()
    '''

if __name__ == "__main__":
    main(sys.argv[1:])
