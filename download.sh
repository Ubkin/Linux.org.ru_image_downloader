#!/bin/bash

#Donloads images
python img_find.py > links
wget -P images --input-file=$(cat links | sort -t/ -nk5)
