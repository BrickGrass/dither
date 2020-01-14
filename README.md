This is a command line interface for dithering images using the hitherdither library.

# Setup:
1. Install python3
2. cd into the folder which this file is stored and create a folder called output
3. Use pip to install the requirements from requirements.txt, the command `pip install -r requirements.txt` should work, but if it doesn't, you may want to try `pip3 install -r requirements.txt` or `python -m pip install -r requirements.txt`
4. Now run `python dither.py --help` to show all the options available

Inside dither.py I have some code that assumes when writing paths you will be using forwards slashes (/) but if you are on windows this may not be the case, if you need to use backslashes (\\), simply edit the line:
`split_path = image_path.split("/")`
to say:
`split_path = image_path.split("\\")`
(the two backslashes are needed to escape the backslash so it's a valid string)

# Arguments

## Image
**-i** or **--image** </br>
Path to the image you wish to dither. If you do not give the absolute path, it must be either within the same folder as this script or a subfolder. This command is the only one that is always required.

Example:
`python dither.py -i myimage.png`

## Dither
**-d** or **--dither** </br>
The name of the dithering algorithm you wish to use. The default will be bayer dithering. </br>
Available choices:
1. **bayer** or **b**
2. **yliluoma** or **y**
3. **cluster-dot** or **cd**
4. **floyd-steinberg** or **fs**
5. **jarvis-judice-ninke** or **jjn**

Example:
`python dither.py --image input/mycoolimage.png -d yliluoma`

![alt text](https://i.imgur.com/RXuE64I.png, "A comparison of the dithers available in this program")

## Palette
**-p** or **--palette** </br>
Name of the palette you wish to dither with. The default palette is geo32. If you want to add more palettes, add them to the palettes.py file as a list of rgb tuples, and then go into dither.py and edit the choices of this arg to include the name that you give to your list. </br>
Available choices:
1. **geo32**
2. **dawnbringer16**
3. **pixelcanvas**
4. **pixelzone**
5. **pxlsspace**

Example:
`python dither.py -i /home/username/Pictures/myverycoolimage.jpg -p geo32`

## Threshold
**-t** or **--threshold** </br>
The threshold value you want to use for dithering. The default value is 128. Not all of these dithering algorithms take a threshold value as an argument. </br>
Available choices:
1. **2**
2. **4**
3. **8**
4. **16**
5. **32**
6. **64**
7. **128**
8. **256**
9. **512**

## Order
**-o** or **--order** </br>
The order value you want to use for dithering. The default value is 8. </br>
Available choices:
1. **2**
2. **4**
3. **8**
4. **16**
5. **32**
