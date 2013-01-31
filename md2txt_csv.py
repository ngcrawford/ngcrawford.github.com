
import re
import sys
import subprocess

"""
Converts markdown formated CV to plaintext.

$ python md2txt_csv.py index.md > cv.txt
"""

fin = sys.argv[1]
fin = open(fin,'rU')

header = False
for count, line in enumerate(fin):

    # Skip header
    line = line.strip("\n")
    if line == "---" and header == False:
        header = True
        continue

    if line == "---" and header == True:
        header = False
        continue

    if header == True:
        continue

    # All sorts of REGEX fun!
    line = re.sub("^#+\s", "", line)
    line = re.sub("[*]*", "", line)
    line = re.sub("^- ", '  ', line)
    line = re.sub("^\s*- ", "     ", line)
    line = re.sub("^   ", "    ", line)
    
    if re.search("\[.\]$", line) != None:
        line = re.sub("\[.\]$", "", line)
        line = re.sub("\[", "", line)
        line = re.sub("\]", "", line)

    if line.startswith('[') == True:
        continue

    print line

"""
subprocess
gimli -y -f  index.md -o assets/downloads/
mv assets/downloads/index.pdf assets/downloads/NGCrawford_CV.pdf

"""

