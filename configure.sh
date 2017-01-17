#!/usr/bin/env bash
echo This script will configure your computer.
sudo add-apt-repository ppa:bitcoin/bitcoin -y
sudo apt-get update
echo Installing dependencies
sudo apt install python3 python3-pip
sudo apt-get install build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils -y
sudo apt-get install libboost-all-dev -y
sudo apt-get install libdb4.8-dev libdb4.8++-dev -y
echo Installing QT Gui dependencies
sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libprotobuf-dev protobuf-compiler -y
echo Done!