import encoder_lib as encoder
import decoder_lib as decoder
import zigzag_lib as ziggy

import huffman_lib as huffman
import matplotlib.pyplot as plt
import getopt
import sys

def main(argv):
    inputFile1 = ""
    intputFile2 = ""
    qsize = ""

    # load file with command line args
    try:
        opts, args = getopt.getopt(argv, "b:i:q:")
    except getopt.GetoptError:
        print("USAGE: python3 decoder.py -b <.bit file> -i <image> -q <qsize>")
        sys.exit()

    for opt, arg in opts:
        if opt == "-b":
            inputFile1 = arg
        elif opt == "-i":
            inputFile2 = arg
        elif opt == "-q":
            qsize = int(arg)
        else:
            print("USAGE: python3 decoder.py -b <.bit file> -i <image> -q <qsize>")
            sys.exit()

    if inputFile1 is "":
        print("USAGE: python3 decoder.py -b <.bit file> -i <image> -q <qsize>")
        sys.exit()

    if inputFile2 is "":
        print("USAGE: python3 decoder.py -b <.bit file> -i <image> -q <qsize>")
        sys.exit()

    if qsize is "":
        print("USAGE: python3 decoder.py -b <.bit file> -i <image> -q <qsize>")
        sys.exit()

    # decode huffman back into text
    print("Decoding .bit file...")
    #dec = huffman.Decoder(inputFile1)
    #dec.decode_as("raw_inverse.txt")
    print("\tDecoding complete!")

    # read imgDCTZ back in
    print("Loading zig-zagged DCT array...")
    imgDCTZ = decoder.np.loadtxt("raw_inverse.txt")
    print("\tArray loaded!")

    # reverse zig-zag
    print("Unpacking zigged matrix...")
    imgDCT = ziggy.iZigZag(imgDCTZ, qsize)
    print("\tMatrix unpacked!")

    print("Reversing DCT...")
    imgInverse = decoder.cv2.idct(imgDCT.astype(float))
    print("\tDCT reversed!")
    imgRecon = decoder.Image.fromarray(imgInverse)
    print("Displaying image...")
    imgRecon.show()

    print("Calculating error...")
    imgOrig = encoder.load_image_as_array(inputFile2)
    iError = decoder.getImageError(decoder.np.asarray(imgRecon),
                                   decoder.np.asarray(imgOrig))
    if iError is not None:
        print("\tMean squared error: ""{:.5}%".format(float(iError) * 100))
    else:
        print("\tERROR: Could not display error!")

    print("Calculating PSNR...")

    print("Generating graph...")
    #plt.plot(imgRecon)
    #plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
