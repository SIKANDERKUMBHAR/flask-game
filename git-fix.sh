#!/bin/bash
git merge --abort
git pull --rebase origin main
git push origin main
