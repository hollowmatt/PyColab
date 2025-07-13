from argparse import ArgumentParser

def main():
  parser = ArgumentParser()
  parser.add_argument("indent", type=int, help="Indentation level for the output")
  parser.add_argument("input_file", type=str, help="Input file to process")
  parser.add_argument("-f", "--file", dest="filename", help="file to write output to")
  args = parser.parse_args()
  print("arguments:", args)

main()