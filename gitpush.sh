#!/bin/bash

clear
echo "pushing changes to remote repository"
rm -rf *~
git rm *~
git rm *aux 
git rm *dvi 
git rm *log 
git rm *out
git add *
git commit -m $1
git push 
