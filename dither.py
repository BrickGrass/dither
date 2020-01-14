from PIL import Image, ImageChops
import hitherdither
import argparse
import sys
from datetime import datetime, timedelta
import time
from yaspin import yaspin
import os

import palettes

start = datetime.now()

# Defining all command line arguments that can be used
parser = argparse.ArgumentParser(
    description = "Dithers images using various dithering algorithms.")
parser.add_argument("-i", "--image",
    required=True,
    help="Path to the image you wish to dither. If you do not give the absolute path, it must be either within the same folder as this script or a subfolder.")
parser.add_argument("-d", "--dither",
    help="The name of the dithering algorithm you wish to use.",
    default="bayer",
    choices=["bayer", "b", "yliluoma", "y", "cluster-dot", "cd", "floyd-steinberg", "fs", "jarvis-judice-ninke", "jjn"])
parser.add_argument("-p", "--palette",
    default="geo32",
    help="Name of the palette you wish to dither with.",
    choices=["geo32", "dawnbringer16", "pixelcanvas", "pixelzone", "pxlsspace"])
parser.add_argument("-t", "--threshold",
    default=256,
    choices=[2, 4, 8, 16, 32, 64, 128, 256, 512],
    help="The threshold value you want to use for dithering.",
    type=int)
parser.add_argument("-o", "--order",
    default=8,
    choices=[2, 4, 8, 16, 32],
    help="The order value you want to use for dithering.",
    type=int)

# Getting the user input/default values from the arguments
args = vars(parser.parse_args())

image_path = args["image"]
dither_type = args["dither"]
try:
    palette = getattr(palettes, args["palette"])
except:
    sys.exit("Not a valid palette. See palettes.py for the available options and to add more.")
threshold = args["threshold"]
order = args["order"]

# extract the filename from the path
filename = os.path.basename(image_path)
# get rid of the extension (.png etc)
image_name = filename.split(".")
image_name = " ".join(image_name[:-1])

try:
    with Image.open(image_path).convert("RGBA") as original_image:
        #find all fully transparent pixels
        alpha_mask = original_image.split()[3]
        alpha_mask = Image.eval(alpha_mask, lambda a: 255 if a == 0 else 0)

        #convert from RGBA to RGB and dither
        original_image = original_image.convert('RGB')
        palette = hitherdither.palette.Palette(palette)

        dithered_image = None

        if dither_type == "bayer" or dither_type == "b":
            options = [threshold, order]
            text = "Dithering {name} with bayer dithering. Palette: {p} Threshold: {t} Order: {o}".format(
            name=filename, p=args["palette"], t=threshold, o=order)
            # Pop a spinner in so you can see it's working
            with yaspin(text=text) as sp:
                dithered_image = hitherdither.ordered.bayer.bayer_dithering(original_image, palette, threshold, order)
                sp.write(text)

        elif dither_type == "yliluoma" or dither_type == "y":
            options = [order]
            text = "Dithering {name} with yliluoma dithering. Palette: {p} Order: {o}".format(
            name=filename, p=args["palette"], o=order)
            # Pop a spinner in so you can see it's working
            with yaspin(text=text) as sp:
                dithered_image = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(original_image, palette, order)
                sp.write(text)

        elif dither_type == "cluster-dot" or dither_type == "cd":
            options = [threshold, order]
            text = "Dithering {name} with cluster dot dithering. Palette: {p} Threshold: {t} Order: {o}".format(
            name=filename, p=args["palette"], t=threshold, o=order)
            # Pop a spinner in so you can see it's working
            with yaspin(text=text) as sp:
                dithered_image = hitherdither.ordered.cluster.cluster_dot_dithering(original_image, palette, threshold, order)
                sp.write(text)

        elif dither_type == "floyd-steinberg" or dither_type == "fs":
            options = [order]
            text = "Dithering {name} with floyd steinberg dithering. Palette: {p} Order: {o}".format(
            name=filename, p=args["palette"], o=order)
            # Pop a spinner in so you can see it's working
            with yaspin(text=text) as sp:
                dithered_image = dithered_image = hitherdither.diffusion.error_diffusion_dithering(original_image, palette, "floyd-steinberg", order)
                sp.write(text)

        elif dither_type == "jarvis-judice-ninke" or dither_type == "jjn":
            options = [order]
            text = "Dithering {name} with jarvis judice ninke dithering. Palette: {p} Order: {o}".format(
            name=filename, p=args["palette"], o=order)
            # Pop a spinner in so you can see it's working
            with yaspin(text=text) as sp:
                dithered_image = dithered_image = hitherdither.diffusion.error_diffusion_dithering(original_image, palette, "jarvis-judice-ninke", order)
                sp.write(text)

        else:
            sys.exit("That dithering algorithm is not implemented.")

        #put transparency back in
        dithered_image = Image.composite(Image.new('RGBA', original_image.size, (0, 0, 0, 0)), dithered_image.convert('RGBA'), alpha_mask)
        dithered_image.save("./output/{}_{}_{}_{}.png".format(image_name, dither_type, args["palette"], options))
        #time formatting
        finish = datetime.now()
        delta = finish - start
        print("Dithering completed in {}, closing!".format(str(delta)[:10]))
except IOError:
    sys.exit("File not found")
except Exception as err:
    print("\nUnknown Error! Please contact me on github with the information below, and I will do my best to fix whatever bug you are having.\n")
    sys.exit(err)
