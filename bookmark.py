# Author		: Pranjal Dubey
# Created		: 31 Dec 2015
# Last Modified	:
# Version		: 1.0
# Modifications	:
# Description	: Script to keep a sync between your soft copy and hard copy file
# Known Bugs    :


import PyPDF2, re

filename = input('\nFilename : ')
actualBookPages = input('\nTotal number of pages in your hard copy : ')
bookmarkPageWords = input('\nFew words of page to bookmark : ')

pdfFileObject = open(filename, "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

pdfFileData = ''

print('\nReading file...')

for i in range(pdfReader.numPages):
    pageObject = pdfReader.getPage(i)
    pdfFileData += pageObject.extractText()

avgCharCountPerPage = len(pdfFileData) / int(actualBookPages)

matchCase = r'' + bookmarkPageWords

regex = re.compile(matchCase, re.IGNORECASE | re.DOTALL)

matchResults = re.finditer(regex, pdfFileData)
possiblePages = [match.start(0) for match in matchResults]

if len(possiblePages) == 1:
    print('\nPossible hit in your hard copy:-\n')
elif len(possiblePages) > 1:
    print('\nPossible hits in your hard copy:-\n')
else:
    print('\nNo matches found!')
    exit

for page in possiblePages:
    print(int(page / avgCharCountPerPage))
