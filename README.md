This is a command line interface for dithering images using the [hitherdither](https://github.com/hbldh/hitherdither) library.

# Setup:
1. Install python3
2. cd into the folder which this file is stored and create a folder called output
3. Use pip to install the requirements from requirements.txt, the command `pip install -r requirements.txt` should work
4. Now run `python dither.py --help` to show all the options available

# Arguments:

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
Name of the palette you wish to dither with. The default palette is geo32. If you want to add more palettes, add them to the palettes.py file as a dictionary of string and rgb tuple pairs, and then go into dither.py and edit the choices of this arg to include the name that you give to your dictionary. </br>
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

## Exclude
**-e** or **--exclude** </br>
The colours that you do not want to use from whichever palette you are using. The default value is 0, which removes no colours. To see which number corresponds to each palette's colours, look in palettes.py. </br>

Example:
`python dither.py -i input/myverycoolimage.png -p geo32 -e 5 8 89`
Here the colours 5 and 8 would not be used in dithering, and the input 89 would be ignored, as it isn't a valid colour number.
