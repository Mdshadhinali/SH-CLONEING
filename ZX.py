"/data/python/lib/python2.7/_io.so"
import os, sys

os.system("git pull")

try:

    __import__("SHADHIN").Main()

except Exception as e:

    exit(str(e))
