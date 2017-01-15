import fileinput
import zipfile
import requests
import filefind
import sys
try:
    f = open('.age.txt')
    if int(f.read()) < int(18):
        print("Fuck, we dont need any shitcoins")
        sys.exit()
except FileNotFoundError:
    old = int(input("How old are you? \n"))
    if old < 18:
        print("Fuck, we dont need any shitcoins")
        file = open(".age.txt", "w")
        file.write(str(old))
        file.close()
    else:
        print("First run configure.sh file")
        print("Don't forget to chmod u+x configure.sh")
        if str(input("Done? Y/N ")) == 'Y':
            print("This tool helps you to make your own cryptocurrency")
            algo = input("1.ProofOfStake 2.ProofOfWork\n")
            if algo == '1':
                print("Selected POS")
                print("Requests version: ", requests.__version__)
                url = "https://github.com/rat4/blackcoin/archive/master.zip"
                r = requests.get(url)
                with open("pos.zip", "wb") as code:
                    code.write(r.content)
                with zipfile.ZipFile("pos.zip", "r") as zip_ref:
                    zip_ref.extractall("pos")
                textToSearch = "BlackCoin"
                textToSearch1 = "blackcoin"
                textToSearch2 = "BLACKCOIN"
                texts = "BLK"
                textToReplace = input("Name of your coin? Like Litecoin or Bitcoin (Uppercase) ")
                textToReplace1 = input("Name of your coin in lowercase ")
                textToReplace3 = input("Name of your coin with CAPS LOCK ")
                texts1 = input("Name of your coin like TLC, BTC ")
                fileToSearch = "pos/blackcoin-master/README.md"
                fileToSearch = ','.join(filefind.get_filepaths(directory="pos"))
                tempFile = open(fileToSearch, 'r+')
                for line in fileinput.input(fileToSearch):
                    tempFile.write(line.replace(textToSearch, textToReplace))
                tempFile.close()
                tempFile = open(fileToSearch, 'r+')
                for line in fileinput.input(fileToSearch):
                    tempFile.write(line.replace(texts, texts1))
                tempFile.close()
                tempFile = open(fileToSearch, 'r+')
                for line in fileinput.input(fileToSearch):
                    tempFile.write(line.replace(textToSearch2, textToReplace3))
                tempFile.close()
            if algo == '2':
                print("Selected POW")
                print("Requests version: ", requests.__version__)
                url = "https://github.com/litecoin-project/litecoin/archive/v0.13.2.1.zip"
                r = requests.get(url)
                with open("pow.zip", "wb") as code:
                    code.write(r.content) # Downloading sources
                with zipfile.ZipFile("pow.zip", "r") as zip_ref:
                    zip_ref.extractall("pow") # Unzip sources into 'pow' folder
                textToSearch = "Litecoin"
                textToSearch1 = "litecoin"
                textToSearch2 = "LITECOIN"
                texts = "LTC"
                textToReplace = input("Name of your coin? Like Litecoin or Bitcoin (Uppercase) ")
                textToReplace1 = input("Name of your coin in lowercase ")
                textToReplace3 = input("Name of your coin with CAPS LOCK ")
                texts1 = input("Name of your coin like TLC, BTC ")
                fileToSearch = ' , '.join(filefind.get_filepaths(directory="pow"))
                tempFile = open(fileToSearch, 'r+')
                for line in fileinput.input(fileToSearch):
                    tempFile.write(line.replace(textToSearch, textToReplace))
                tempFile.close()
                tempFile = open(fileToSearch, 'r+')
                for line in fileinput.input(fileToSearch):
                    tempFile.write(line.replace(texts, texts1))
                tempFile.close()
                tempFile = open(fileToSearch, 'r+')
                for line in fileinput.input(fileToSearch):
                    tempFile.write(line.replace(textToSearch2, textToReplace3))
                tempFile.close()
                ports = int(input("What ports do you want to use? Mainnet: "))
                ports1 = int(input("Testnet: "))
                textToSearch = int("9333")
                textToSearch1 = int("19993")
                fileToSearch = "pow/litecoin-0.13.2.1/src/chainparams.cpp"
                tempFile = open(fileToSearch, 'r+')
                for line in fileinput.input(fileToSearch):
                    tempFile.write(line.replace(textToSearch, ports))
                tempFile.close()
                tempFile = open(fileToSearch, 'r+')
                for line in fileinput.input(fileToSearch):
                    tempFile.write(line.replace(textToSearch1, ports1))
                tempFile.close()
        else:
            print|("Bye.")