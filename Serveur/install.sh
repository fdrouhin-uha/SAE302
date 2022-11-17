#!/bin/bash

echo "Intallation des librairies python"
echo "---------------------------------"
echo "Installation de python3"
sudo apt-get install python3
echo "Installation de python3-pip"
sudo apt-get install python3-pip
echo "Installation de Qt6"
sudo apt-get install python3-pyqt6
sudo pip install pyqt6
echo "Intallation de platform"
sudo pip install lib-platform
echo"---------------------------------"
echo "Installation terminée"