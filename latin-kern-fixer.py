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

latinChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', \
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
              'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', \
              'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ő', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', \
              'Ű', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', \
              'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', 'ő', 'ø', 'ù', \
              'ú', 'û', 'ü', 'ű', 'ý', 'þ', 'ÿ', \
              '.', ',', '?', '!', ':', ';', "'", '"', '(', ')', '[', ']', '{', '}', \
              '<', '>', '@', '#', '$', '%', '&', '*', '+', '-', '/', '=', '^', '_', \
              '|', '~', '`']

def main():
    return

def getKerningPairs():
    if args.glyphs:
        args.glyphs = args.glyphs.split('')
        newKernTable = [ ]
        basicGlyphs = [ ]
        for glyph in args.glyphs:
            if unidecode(glyph) not in basicGlyphs:
                basicGlyphs.append(unidecode(glyph))
        for left, right, val in kern.kernTable:
            if left in basicGlyphs or right in basicGlyphs:
                newKernTable.append([left, right, val])
        newKernTable = newKernTable.sort()
        for char in args.glyphs:
            indivKernTable = [ ]
            whitespace = len(re.findall(r'\s', char))
            if whitespace:
                del args.glyphs[args.glyphs.index(char)]
                continue
            indices = [index for index, sublist in enumerate(newKernTable) if unidecode(char) in sublist]
            for index in indices:
                indivKernTable.append(newKernTable[index])
                
