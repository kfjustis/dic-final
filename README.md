# dic-final
Final project for Digital Image Compression, Spring 2017

# Instructions
This project uses requires Python 3 to run. Checkout out the .py files for dependencies and install as necessary.

First run ```encoder.py``` with

    python3 encoder.py -i <image filepath> -q <quantization step size>
    
Then run ```decoder.py``` with

    python3 decoder.py -b image.bit -i <image filepath> -q <quantization step size>

Note: The image filepath used with ```decoder.py``` must match the filepath used with ```encoder.py```
