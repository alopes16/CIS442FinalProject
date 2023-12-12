#Austin Lopes
#CIS 442
#Final Project
# Create a program that lists all the masquaraded files in any given
# folder. This is accomplished by the program checking "the
# file signature" and comparing it with the file's extension
# in it's name. If the file extension and the file signature
# indicates a difference, the program must output the file's path. 
#

import os
import magic

#function to find and return the file signature of an inputted file
def getFileSignature(filePath):
    mime = magic.Magic(mime=True)
    fileSignature = mime.from_file(filePath)

    fileSignature = fileSignature.split('/')[-1]

    return fileSignature

#this function interates through the files in an inputted folder
#and finds both the file signature and extension and prints both out 
#for each file. It then compares them and prints out the file's 
#path if they dont match
def iterateFiles(folderPath):
    for root, dirs, files in os.walk(folderPath):
        for fileName in files:
            filePath = os.path.join(root, fileName)
            fileSignature = getFileSignature(filePath)
            fileExtension = os.path.splitext(filePath)[1][1:]

            print(fileName)
            print("  File Signature: ", fileSignature)
            print("  File Extension: ", fileExtension)

            if fileSignature.lower() != fileExtension.lower():
                print(f"  DOES NOT MATCH, FILE PATH: {filePath}")
            else:
                print ("MATCHES")
            print()


#change this to your own folder path
folderPath = '/home/austinlopes/Desktop/ProjectTest'
iterateFiles(folderPath)
