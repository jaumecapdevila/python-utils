#!/usr/bin/python

import sys
import os

if(len(sys.argv) < 2):
    print('You need to provide a valid file path...')
    exit(0)

target = sys.argv[1]

if (not os.path.exists(target)):
    print("File or directory {} does not exist".format(path))
    exit(0)

path = target.split("/")

lastName = path[len(path) - 1]

path[len(path) - 1] = lastName.lower()

if lastName == lastName.lower():
    print("Skipping because the file or folder is already in lower case")
    exit(0)

toLowerName = "/".join(path)

print('Renaming {} to {}'.format(target, toLowerName))

os.rename(target, toLowerName)
