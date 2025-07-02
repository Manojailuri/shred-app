import sys
from os import walk
import os
pattt = str(sys.argv[1])
#f = set()
f = []
for (dirpath, dirnames, filenames) in walk(pattt):
    #f.extend(filenames)
    for file_name in filenames:
        rel_dir = os.path.relpath(dirpath, pattt)
    #print(rel_dir)
        rel_file = os.path.join(rel_dir, file_name)
        #f.add(rel_file)
        f.append(rel_file)
    #print(filenames)
    #break
print(pattt)
file = open(os.path.join("/home/pugvsgold/bin/Danger", 'del.sh'), 'w')
for x in f:
    y = x.replace(" ", "\ ")
    y = y.replace("(", "\(")
    y = y.replace(")", "\)")
    #file.write("shred -u " + y + ";")
    print("shred -u " + y + ";")
#print(f)
print("Do you really want to delete the above files permanently? (Y/N)")
c = input()
if c == "y" or c == "Y":
    for x in f:
        y = x.replace(" ", "\ ")
        y = y.replace("(", "\(")
        y = y.replace(")", "\)")
        file.write("shred -u -v -n 3 " + y + ";")
    
file.close()
