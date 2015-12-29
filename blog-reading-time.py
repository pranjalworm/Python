# Author		: Pranjal Dubey
# Created		: 29 Dec 2015
# Last Modified	:
# Version		: 1.0
# Modifications	:
# Description	: Parse text data from file/clipboard memory, count the number of words in it and copy the estimated reading time embeded in html into clipboard, assuming that average reading time is 200 wpm and where the average word length is taken as 5.1 letters
# Known Bugs    :


#importing vendor modules
import sys, pyperclip


def countCharacters(fileData):
    '''
    function to count the number of letters in a given string
    '''
    count = 0

    fileData = fileData.lower()

    for i in range(len(fileData)):
        if fileData[i] in 'abcdefghijklmnopqrstuvwxyz':
            count += 1
    estimatedReadingTime(count//5.1)

def estimatedReadingTime(words):
    '''
    function to calculate estimated reading time from input words; then embed that value into predefined html code and load that into clipboard
    '''

    #finding time
    time = str(round((1/200) * words, 2)).split(".")

    #number of hours
    hours = int(time[0]) // 60

    #number of mins
    minutes = int(time[0]) % 60

    #number of seconds
    seconds = round(int(time[1]) * 0.6)

    #converting to human readable form
    copyBuffer = ''

    if hours != 0:
        copyBuffer += str(hours) + ' '
        if hours == 1:
            copyBuffer += 'hour '
        else:
            copyBuffer += 'hours '


    if minutes != 0:
        copyBuffer += str(minutes) + ' '
        if minutes == 1:
            copyBuffer += 'minute '
        else:
            copyBuffer += 'minutes '

    copyBuffer += str(seconds) + ' seconds'

    htmlPrefixCode = "<div style=\"background:#f1ebeb;padding:1%;width:auto;margin-bottom:2%;\">Estimated reading time : "
    htmlSuffixCode = "</div>"

    copyBuffer = htmlPrefixCode + copyBuffer + htmlSuffixCode

    pyperclip.copy(copyBuffer)


    print("\nWords : " + str(words) + "\nCode copied in Clipboard!\n")


#if no command line arguments are passed, the script loads data from clipboard
if len(sys.argv) > 1:
    filename = sys.argv[1]

    fileHandle = open(filename, "r")

    #number of words in file
    fileData = fileHandle.read()

    if fileData == '':
        print("File is empty!")
    else:
        countCharacters(fileData)

else:
    #loading number of words from data in clipboard
    fileData = pyperclip.paste()

    if fileData == '':
        print("Clipboard is empty!")
    else:
        countCharacters(fileData)
