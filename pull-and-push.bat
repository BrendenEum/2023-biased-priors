#!/bin/sh
d:
cd "OneDrive - California Institute of Technology/PhD/Rangel Lab/2023-biased-priors"
git pull
git add .
git commit -a -m "Automatic pull-push using shell script"
git push
cmd /k
