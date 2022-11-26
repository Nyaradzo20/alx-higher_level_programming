#!/bin/bash
#dislay all methods accepted
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
