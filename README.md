# Bit Plane Slicing

Zeroize bit planes in 8-bit color images as a form of image augmentation. Bit plane slicing has previously been used for image compression.

## Installing on Linux

```
$ git clone https://github.com/deanwetherby/bit-plane-slicing
$ cd bit-plane-slicing
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pytnon -m pip install --upgrade pip setuptools wheel
(venv) $ python -m pip install -r requirements.txt
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

```
original image.jpg
```
![original](../master/images/image.jpg)
---
```
(venv) $ python main.py --input images/image.jpg --output images/output_0.jpg --plane 0
```
![bit plane 0 (MSB)](../master/images/output_0.jpg)
---
```
(venv) $ python main.py --input images/image.jpg --output images/output_1.jpg --plane 1
```
![bit plane 1 (MSB)](../master/images/output_1.jpg)
---
```
(venv) $ python main.py --input images/image.jpg --output images/output_2.jpg --plane 2
```
![bit plane 2 (MSB)](../master/images/output_2.jpg)
---
```
(venv) $ python main.py --input images/image.jpg --output images/output_3.jpg --plane 3
```
![bit plane 3 (MSB)](../master/images/output_3.jpg)
---
```
(venv) $ python main.py --input images/image.jpg --output images/output_4.jpg --plane 4
```
![bit plane 4 (MSB)](../master/images/output_4.jpg)
---
```
(venv) $ python main.py --input images/image.jpg --output images/output_5.jpg --plane 5
```
![bit plane 5 (MSB)](../master/images/output_5.jpg)
---
```
(venv) $ python main.py --input images/image.jpg --output images/output_6.jpg --plane 6
```
![bit plane 6 (MSB)](../master/images/output_6.jpg)
---
```
(venv) $ python main.py --input images/image.jpg --output images/output_7.jpg --plane 7
```
![bit plane 7 (MSB)](../master/images/output_7.jpg)

## References
[Wikipedia:bit plane](https://en.wikipedia.org/wiki/Bit_plane)

[Bit plane slicing](https://nptel.ac.in/courses/117104069/chapter_8/8_13.html)

[Image Compression using bit planes](https://spin.atomicobject.com/2013/10/08/image-compression-bit-planes/)

