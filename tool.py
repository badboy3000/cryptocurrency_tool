import requests
import zipfile
import os
import sys
import fileinput
algo = input("1.POS 2.POW\n")
if algo == '1':
    print("Selected POS")
    print("Requests version: ", requests.__version__)
    url = "https://github.com/rat4/blackcoin/archive/master.zip"
    r = requests.get(url)
    with open("pos.zip", "wb") as code:
        code.write(r.content)
    with zipfile.ZipFile("pos.zip", "r") as zip_ref:
        zip_ref.extractall("pos")
    name = input("Name of your coin? ")
if algo == '2':
    print("Selected POW")
    print("Requests version: ", requests.__version__)
    url = "https://github.com/litecoin-project/litecoin/archive/master-0.10.zip"
    r = requests.get(url)
    with open("pow.zip", "wb") as code:
        code.write(r.content)
    with zipfile.ZipFile("pow.zip", "r") as zip_ref:
        zip_ref.extractall("pow")
    textToSearch = "Litecoin"
    textToSearch1 = "litecoin"
    textToSearch2 = "LITECOIN"
    texts = "LTC"
    textToReplace = input("Name of your coin? Like Litecoin or Bitcoin (Uppercase) ")
    textToReplace1 = input("Name of your coin in lowercase ")
    textToReplace3 = input("Name of your coin with CAPS LOCK ")
    texts1 = input("Name of your coin like TLC, BTC ")
    fileToSearch = "pow/litecoin-master-0.10/README.md"
    tempFile = open(fileToSearch, 'r+')
    for line in fileinput.input(fileToSearch):
        tempFile.write(line.replace(textToSearch, textToReplace))
    for line in fileinput.input(fileToSearch):
            tempFile.write(line.replace(textToSearch1, textToReplace1))
    for line in fileinput.input(fileToSearch):
        tempFile.write(line.replace(textToSearch2, textToReplace3))
    for line in fileinput.input(fileToSearch):
        tempFile.write(line.replace(texts, texts1))
    tempFile.close()

