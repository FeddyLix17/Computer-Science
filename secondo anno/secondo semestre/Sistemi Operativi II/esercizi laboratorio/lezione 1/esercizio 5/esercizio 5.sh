#!/bin/bash

echo "aggiunta dell'utente1"
sleep 2
sudo adduser utente1

echo
echo "aggiunta dell'utente2"
sleep 2
sudo adduser utente2

echo
echo "esecuzione del comando apt-get update"
sleep 2
apt-get update

echo
echo "esecuzione del comando sudo apt-get update"
sleep 2
sudo apt-get update
