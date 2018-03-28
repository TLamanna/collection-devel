import csv
import argparse
import sys
import os
import re
import isbnlib

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file',required=True, help='CSV file to read from')
parser.add_argument('-o', '--output', help='file to write output to')
parser.add_argument('-p', '--problems', help="file to write records that can't be cleaned to")

args = parser.parse_args()

books = []
problems = []

def main():
  if args.file:
     cleaned_data = parse_csv(args.file)
  if cleaned_data:
    write_cleaned_data(cleaned_data)
    print('{} Records Cleaned'.format(len(books))) 
  if args.problems:
    if problems:
      write_problems(problems)
      print('{} Problem Records'.format(len(problems))) 
    else:
      print('Congratulations, no problems!')


def parse_csv(input_file):

  with open(os.path.abspath(input_file), newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    x = 0
    for row in reader:
      if isbnlib.get_isbnlike(row[2]):
        isbn_final = isbnlib.EAN13(isbnlib.get_isbnlike(row[2])[0])
        books.append([x,row[0],row[1],isbn_final, row[3]])
      else:
        problems.append([row[0],row[1],row[2], row[3]])
      x += 1
    return books
    
def write_cleaned_data(cleaned_data):
  if args.output:
    output_file = os.path.abspath(args.output)
  else:
    output_file = os.path.dirname(os.path.abspath(args.file)) + '/cleaned-data-' + os.path.basename(args.file)
  with open(output_file, mode='w', newline='\n') as csvoutputfile:
    writer = csv.writer(csvoutputfile)
    writer.writerow(['id','title','author','isbn','annual circs'])
    for row in cleaned_data:
      writer.writerow(row)
  csvoutputfile.close()

def write_problems(problems):
  if args.problems:
    output_file = os.path.abspath(args.problems)
  else:
    output_file = os.path.dirname(os.path.abspath(args.file)) + '/problem-children-' + os.path.basename(args.file)
  with open(output_file, mode='w', newline='\n') as csvoutputfile:
    writer = csv.writer(csvoutputfile)
    writer.writerow(['title','author','isbn','annual circs'])
    for row in problems:
      writer.writerow(row)
  csvoutputfile.close()




if __name__=="__main__":
  main()
