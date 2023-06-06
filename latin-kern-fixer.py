from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import kerning
from unidecode import unidecode
import argparse
import re

parse = argparse.ArgumentParser(prog='Latin Kern Fixer', description='Self-explanatory')
parse.add_argument('-f', '--file', type = str, help = 'File Name or Path.', required = True)
parse.add_argument('-o', '--output', type = str, help = 'Output File Name.', required = True)
parse.add_argument('-g', '--glyphs', type = str, help = 'Specify Letters to Kern.', required = False)
args = parse.parse_args()

font = TTFont(args.file)
kern = font['kern']

kernTables = { }
latinChars = ['À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', \
              'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ő', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', \
              'Ű', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', \
              'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', 'ő', 'ø', 'ù', \
              'ú', 'û', 'ü', 'ű', 'ý', 'þ', 'ÿ']

def main():
    glyphs = args.glyphs.split('') if args.glyphs else latinChars
    getKernTables(glyphs)
    for glyph in glyphs:
        unidecoded = unidecode(glyph)
        for item in kernTables[unidecoded]:
            if item.index(unidecoded) == 0:
                kern[(glyph, item[1])] = item[2]
            elif item.index(unidecoded) == 1:
                kern[(item[0], glyph)] = item[2]
    font.save(f'{args.output}.ttf')

def getKernTables(glyphs):
    tempTables = [ ]
    basicGlyphs = [ ]
    for glyph in glyphs:
        if unidecode(glyph) not in basicGlyphs:
            basicGlyphs.append(unidecode(glyph))
    for left, right, val in kern.kernTable:
        if left in basicGlyphs or right in basicGlyphs:
            tempTables.append([left, right, val])
    tempTables = tempTables.sort()
    for glyph in glyphs:
        unidecoded = unidecode(glyph)
        whitespace = len(re.findall(r'\s', glyph))
        if whitespace:
            continue
        indices = [index for index, sublist in enumerate(tempTables) \
                    if unidecoded in sublist]
        for index in indices:
            if not kernTables[f'{tempTables[index][0]}']:
                kernTables[f'{tempTables[index][0]}'] = [ ]
            kernTables[f'{tempTables[index][0]}'].append(tempTables[index])
        
main()