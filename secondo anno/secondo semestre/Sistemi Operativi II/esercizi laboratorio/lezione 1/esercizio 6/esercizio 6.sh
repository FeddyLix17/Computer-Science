#! /bin/bash


echo "cambio utente in utente1"
sleep 2
su utente1

echo
echo "esecuzione del comando apt-get update come utente utente1"
sleep 2
echo "apt-get update"

echo
echo "esecuzione del comando sudo apt-get update"
sleep 2
sudo apt-get update

echo
echo "aggiunta di utente1 ai sudoers"
sleep 2
sudo adduser utente1 sudo

echo
echo "nuova esecuzione del comando apt-get update come utente utente1"
sleep 2
echo "apt-get update"

echo
echo "nuova esecuzione del comando sudo apt-get update"
sleep 2
sudo apt-get update
