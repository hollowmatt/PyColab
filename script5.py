import fileinput
for line in fileinput.input():
  if fileinput.isfirstline():
    print(f"Processing file: {fileinput.filename()}")
  if not line.startswith("##"):
    print(line, end="")