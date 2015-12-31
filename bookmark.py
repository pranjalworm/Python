# Author		: Pranjal Dubey
# Created		: 31 Dec 2015
# Last Modified	:
# Version		: 1.0
# Modifications	:
# Description	: Script to keep a sync between your soft copy and hard copy file
# Known Bugs    :


import PyPDF2, re

pdfFileObject = open("pdfs/the_girl_who_played_with_fire.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

pdfFileData = ''

for i in range(pdfReader.numPages):
    pageObject = pdfReader.getPage(i)
    pdfFileData += pageObject.extractText()

actualBookPages = 568

avgCharCountPerPage = len(pdfFileData) / actualBookPages

print(avgCharCountPerPage)

bookmarkPageWords = input('Enter few words of page to bookmark: ')

matchCase = r'' + bookmarkPageWords

regex = re.compile(matchCase, re.IGNORECASE | re.DOTALL)

print(re.search(regex, pdfFileData).start())

pageNumber = re.search(regex, pdfFileData).start() / avgCharCountPerPage

print(pageNumber)
