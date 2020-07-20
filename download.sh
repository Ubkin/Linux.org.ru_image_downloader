#!/bin/bash

wget -P images --input-file=$(cat links | sort -t/ -nk5)
