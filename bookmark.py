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

pageStartingWords = input('Enter first few words: ')
pageEndingWords = input('Enter last few words: ')

bookmarkPageWords = input('Enter few words of page to bookmark: ')

matchCase1 = r'' + pageStartingWords + '(.*)' + pageEndingWords

regex1 = re.compile(matchCase1, re.IGNORECASE | re.DOTALL)

charCountPerPage = re.search(regex1, pdfFileData).end() - re.search(regex1, pdfFileData).start()

print("Character count per page :", charCountPerPage)

matchCase2 = r'' + bookmarkPageWords

regex2 = re.compile(matchCase2, re.IGNORECASE | re.DOTALL)

print(re.search(regex2, pdfFileData).start())

pageNumber = re.search(regex2, pdfFileData).start() / charCountPerPage

print(pageNumber)
