# Bit Plane Slicing

TODO

## Installing

```
$ git clone https://github.com/deanwetherby/bit-plane-slicing
$ cd bit-plane-slicing
$ python3 -m venv ./venv
$ source activate venv/bin/activate
$ pip install -r requirements.txt
```

## Script usage

```
$ python main.py -h
usage: main.py [-h] [-i INPUT] [-o OUTPUT] [-p PLANE [PLANE ...]]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input image path
  -o OUTPUT, --output OUTPUT
                        Output image path
  -p PLANE [PLANE ...], --plane PLANE [PLANE ...]
                        Space separated list of bit planes to zeroize

```

## Examples

![original](../master/images/image.jpg)
![bit plane 0 (MSB)](../master/images/output_0.jpg)
![bit plane 1 (MSB)](../master/images/output_1.jpg)
![bit plane 2 (MSB)](../master/images/output_2.jpg)
![bit plane 3 (MSB)](../master/images/output_3.jpg)
![bit plane 4 (MSB)](../master/images/output_4.jpg)
![bit plane 5 (MSB)](../master/images/output_5.jpg)
![bit plane 6 (MSB)](../master/images/output_6.jpg)
![bit plane 7 (MSB)](../master/images/output_7.jpg)
