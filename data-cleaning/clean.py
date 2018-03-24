import csv
import argparse
import sys
import os


parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file',required=True, help='CSV file to read from')
parser.add_argument('-o', '--output', help='file to write output to')

args = parser.parse_args()


def main():
  print(os.path.abspath('/var/www/html'))
  with open(os.path.abspath(args.file), newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
      print(row)

if __name__=="__main__":
  main()
