#!/bin/bash


# Git Setup Multiple Repository
git remote add gitlab git@gitlab.com:proginfra/stackainer.git
git remote set-url --add --push origin git@gitlab.com:proginfra/stackainer.git

git remote add github git@github.com:ProgInfra/Stackainer.git
git remote set-url --add --push origin git@github.com:ProgInfra/Stackainer.git


# Display Config
git remote show origin

git config --list
