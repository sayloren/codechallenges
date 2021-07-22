# code golf challenge
# https://code.golf/css-colors#python
# wren 20210624

# Given each CSS color keyword print the corresponding hex value.
# The output will be checked case-insensitively.
# The full mapping is as follows:
# https://www.geeksforgeeks.org/matplotlib-colors-to_hex-in-python/
# https://matplotlib.org/stable/tutorials/colors/colors.html

# note:
# i found a lot of very effiicent solutions, but was restricted because of
# the libraries avaialbe for python on the website :_(

# would work except that code golf doenst have matplotlib
import matplotlib
import sys

# get the input argment given by the website
keyword = sys.argv[1]

# use the visualization library matplotlib, which has all the color information
# organized already to convert the keyword string name to the corresponding
# hex value
matplotlib.colors.to_hex(keyword)

# https://learn.circuit.rocks/how-to-extract-data-from-webpages-using-python
import urllib
import gazpacho

# would work except that code golf doenst have any of these libaries
import bs4
import requests
import re

# give the url of the code challenge, where all of teh colors and their
# hexes are written
url = 'https://code.golf/css-colors#python'

# use the url variable to make a request to the website to get the text content
# from the webpage
html_content = requests.get(url).text

# get the content from the website using the keyterm lxml
# there is a lot of javascript stuff that i dont understand, but somehow
# this is the correct term to get the content i want from that part of the
# website
soup = bs4.BeautifulSoup(html_content, "lxml")

# find where in that content a table is, which has the conversions between
# the keyword strings and the hex values
hex_table = soup.find("table")

# find all instances of td in that table, which somehow helps to parse
# out the information i want from it
hrefs = gdp_table.find_all("td")

# initalize the dictionary that im going to build for the keyterm to
# hexidecimal look ups
hex_dict={}

# for each of the references
for h in hrefs:
    # split up the string contained by these special characters to get out the
    # the keyword string - not quite cleaned up, but getting there
    string_h = re.split(' |"|<|>',str(h))
    # if the section contains informatuion and is not empty - indicated
    # by having the below condition, then add the below to my dicationary
    if 'fill=' in string_h:
        # add to the dicationary under the keyterm as given by the 16th item
        # in the list with fill= as the index with plus one for zero based,
        # where the hex term is stored
        hex_dict[a[16]]=a[a.index('fill=')+1]

# this is aparently the only library that codegolf lets me import
# which is to read from the command line the arguments give by the
# website
import sys

# this is the stupid dictinoary I made, where each color name string maps to
# the corresponding hexidecimal code
# there appear to be some duplicates in the greys, but that is just
# because people use grey and gray interchangale
hex_dict={'IndianRed':'#cd5c5c',
'LightCoral':'#f08080',
'Salmon':'#fa8072',
'DarkSalmon':'#e9967a',
'LightSalmon':'#ffa07a',
'Red':'#ff0000',
'Crimson':'#dc143c',
'FireBrick':'#b22222',
'DarkRed':'#8b0000',
'Pink':'#ffc0cb',
'LightPink':'#ffb6c1',
'HotPink':'#ff69b4',
'DeepPink':'#ff1493',
'MediumVioletRed':'#c71585',
'PaleVioletRed':'#db7093',
'Coral':'#ff7f50',
'Tomato':'#ff6347',
'OrangeRed':'#ff4500',
'DarkOrange':'#ff8c00',
'Orange':'#ffa500',
'Gold':'#ffd700',
'Yellow':'#ffff00',
'LightYellow':'#ffffe0',
'LemonChiffon':'#fffacd',
'LightGoldenRodYellow':'#fafad2',
'PapayaWhip':'#ffefd5',
'Moccasin':'#ffe4b5',
'PeachPuff':'#ffdab9',
'PaleGoldenRod':'#eee8aa',
'Khaki':'#f0e68c',
'DarkKhaki':'#bdb76b',
'Lavender':'#e6e6fa',
'Thistle':'#d8bfd8',
'Plum':'#dda0dd',
'Violet':'#ee82ee',
'Orchid':'#da70d6',
'Fuchsia':'#ff00ff',
'Magenta':'#ff00ff',
'MediumOrchid':'#ba55d3',
'MediumPurple':'#9370db',
'BlueViolet':'#8a2be2',
'DarkViolet':'#9400d3',
'DarkOrchid':'#9932cc',
'DarkMagenta':'#8b008b',
'Purple':'#800080',
'Indigo':'#4b0082',
'DarkSlateBlue':'#483d8b',
'SlateBlue':'#6a5acd',
'MediumSlateBlue':'#7b68ee',
'RebeccaPurple':'#663399',
'GreenYellow':'#adff2f',
'Chartreuse':'#7fff00',
'LawnGreen':'#7cfc00',
'Lime':'#00ff00',
'LimeGreen':'#32cd32',
'PaleGreen':'#98fb98',
'LightGreen':'#90ee90',
'SpringGreen':'#00ff7f',
'MediumSpringGreen':'#00fa9a',
'MediumSeaGreen':'#3cb371',
'SeaGreen':'#2e8b57',
'ForestGreen':'#228b22',
'Green':'#008000',
'DarkGreen':'#006400',
'YellowGreen':'#9acd32',
'OliveDrab':'#6b8e23',
'Olive':'#808000',
'DarkOliveGreen':'#556b2f',
'MediumAquamarine':'#66cdaa',
'DarkSeaGreen':'#8fbc8f',
'LightSeaGreen':'#20b2aa',
'DarkCyan':'#008b8b',
'Teal':'#008080',
'Aqua':'#00ffff',
'Cyan':'#00ffff',
'LightCyan':'#e0ffff',
'PaleTurquoise':'#afeeee',
'Aquamarine':'#7fffd4',
'Turquoise':'#40e0d0',
'MediumTurquoise':'#48d1cc',
'DarkTurquoise':'#00ced1',
'CadetBlue':'#5f9ea0',
'SteelBlue':'#4682b4',
'LightSteelBlue':'#b0c4de',
'PowderBlue':'#b0e0e6',
'LightBlue':'#add8e6',
'SkyBlue':'#87ceeb',
'LightSkyBlue':'#87cefa',
'DeepSkyBlue':'#00bfff',
'DodgerBlue':'#1e90ff',
'CornflowerBlue':'#6495ed',
'RoyalBlue':'#4169e1',
'Blue':'#0000ff',
'MediumBlue':'#0000cd',
'DarkBlue':'#00008b',
'Navy':'#000080',
'MidnightBlue':'#191970',
'Cornsilk':'#fff8dc',
'BlanchedAlmond':'#ffebcd',
'Bisque':'#ffe4c4',
'NavajoWhite':'#ffdead',
'Wheat':'#f5deb3',
'Burlywood':'#deb887',
'Tan':'#d2b48c',
'RosyBrown':'#bc8f8f',
'SandyBrown':'#f4a460',
'GoldenRod':'#daa520',
'DarkGoldenRod':'#b8860b',
'Peru':'#cd853f',
'Chocolate':'#d2691e',
'SaddleBrown':'#8b4513',
'Sienna':'#a0522d',
'Brown':'#a52a2a',
'Maroon':'#800000',
'White':'#ffffff',
'Snow':'#fffafa',
'Honeydew':'#f0fff0',
'MintCream':'#f5fffa',
'Azure':'#f0ffff',
'AliceBlue':'#f0f8ff',
'GhostWhite':'#f8f8ff',
'WhiteSmoke':'#f5f5f5',
'SeaShell':'#fff5ee',
'Beige':'#f5f5dc',
'OldLace':'#fdf5e6',
'FloralWhite':'#fffaf0',
'Ivory':'#fffff0',
'AntiqueWhite':'#faebd7',
'Linen':'#faf0e6',
'LavenderBlush':'#fff0f5',
'MistyRose':'#ffe4e1',
'Gainsboro':'#dcdcdc',
'LightGray':'#d3d3d3',
'LightGrey':'#d3d3d3',
'Silver':'#c0c0c0',
'DarkGray':'#a9a9a9',
'DarkGrey':'#a9a9a9',
'Gray':'#808080',
'Grey':'#808080',
'DimGray':'#696969',
'DimGrey':'#696969',
'LightSlateGray':'#778899',
'LightSlateGrey':'#778899',
'SlateGray':'#708090',
'SlateGrey':'#708090',
'DarkSlateGray':'#2f4f4f',
'DarkSlateGrey':'#2f4f4f',
'Black':'#000000',}

# just print the given command line argument (1 becauase the first is probably
# something like 'python' or script) by getting the correct itme
# from the dictionary
print(hex_dict[sys.argv[1]])
