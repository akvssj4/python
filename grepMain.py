import re
import sys

searchFileName = "/Users/akhil-2245/Desktop/searchFile.txt"#sys.argv[2]
searchPatternFileName = "/Users/akhil-2245/Desktop/searchPatterns.txt"
searchPattern = "lor"#sys.argv[1]

searchFile = open(searchFileName,"r")
searchPatternFile = open(searchPatternFileName,"r")

print "Grepping for pattern in file["+searchFileName+"]"

for searchPattern in searchPatternFile:
    print "Grepping for pattern[" + searchPattern + "]..."
    for line in searchFile:
        if re.search(searchPattern, line):
            print line

print "Completed. Exiting..."