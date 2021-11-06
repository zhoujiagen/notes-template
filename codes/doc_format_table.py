import sys

# ([^\.]+)\.(\s+)\.$
# | `$2`$3||

if __name__ == "__main__":
  if (len(sys.argv) < 2):
    print("Example: python doc_format_table.py sample.txt");
    exit(0)

  lines = []
  with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
  max_size = max([len(line) for line in lines])
  for line in lines:
    print("{line}.{padding}.".format(
      line=line.replace("\r", "").replace("\n", ""), 
      padding=" "*(max_size+1-len(line))))
