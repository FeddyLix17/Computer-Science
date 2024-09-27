#!/bin/bash

echo "esecuzione del comando man ls"
sleep 2
man ls

echo 
echo "aggiunta di alcune opzioni"
sleep 2

echo
echo "1. opzione -f"
sleep 2

echo
man -f ls
sleep 2

echo
echo "2. opzione -a"
sleep 2

echo
man -a ls
sleep 2

echo
echo "3. opzione -k"
sleep 2

echo
man -k ls
sleep 2

echo
echo "4. opzione -w"
sleep 2

echo
man -w ls
sleep 2

echo
echo "5. opzione -I"
sleep 2

echo
man -I ls
