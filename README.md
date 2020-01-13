This is a command line interface for dithering images using the hitherdither library.

SETUP:
1) Install python3
2) cd into the folder which this file is stored and create a folder called output
2) Use pip to install the requirements from requirements.txt, the command "pip install -r requirements.txt" should work, but if it doesn't, you may want to try "pip3 install -r requirements.txt" or "python -m pip install -r requirements.txt"
3) Now run "python dither.py --help" to show all the options available

Inside dither.py I have some code that assumes when writing paths you will be using forwards slashes (/) but if you are on windows this may not be the case, if you need to use backslashes (\), simply edit the line:
split_path = image_path.split("/")
to say:
split_path = image_path.split("\\")
(the two backslashes are needed to escape the backslash so it's a valid string)
