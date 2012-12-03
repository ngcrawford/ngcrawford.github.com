import re

fin = open("index.md")

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


	# if re.search("^#+",line) != None:
	# 	print line
	line = re.sub("^#+\s", "", line)
	line = re.sub("[*]*", "", line)
	line = re.sub("^- ",'  ', line)
	line = re.sub("^\s*- ", "     ", line)
	line = re.sub("^   ", "    ", line)
	if re.search("\[.\]$",line) != None:
		line = re.sub("\[.\]$","", line)
		line = re.sub("\[","", line)
		line = re.sub("\]","", line)

	if line.startswith('[') == True:
		continue
	print line
	

