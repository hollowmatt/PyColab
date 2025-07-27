import os
import pathlib
print(os.getcwd())
print(os.listdir(os.curdir))

cur_path = pathlib.Path()
print(cur_path.resolve())
print(cur_path.cwd())

print(os.name)
exists = os.path.exists('mac.py')
print(f"Does 'mac.py' exist? {exists}")