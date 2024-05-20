#!/bin/bash

echo "esecuzione del comando ps"
sleep 2


echo
ps
sleep 2

echo
echo "esecuzione del comando ps -p \$\$"
sleep 2

ps -p $$

echo
echo "esecuzione del comando ps -p \$\$ -ocmd"
sleep 2

echo
ps -p $$ -ocmd
sleep 2

echo
echo "esecuzione del comando ps -p \$\$ -ocmd -h"
sleep 2

echo
ps -p $$ -ocmd -h
echo
