import fontTools
import argparse

parse = argparse.ArgumentParser(prog='Latin Kern Fixer', description='Self-explanatory')
parse.add_argument('-f', '--file', type = str, help = 'Font file | Can be path.', required = True)
parse.add_argument('-o', '--output', type = str, help = 'Output font file | Can be path.', required = True)
parse.add_argument('-g', '--glyphs', type = str, help = 'Specify Letters to Kern.', required = False)
args = parse.parse_args()

def main():
    return
