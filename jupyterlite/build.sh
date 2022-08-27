#!/bin/bash

declare -a cmds=(
    "rm -rf _output"
    "pip install -r requirements.txt"
    "jupyter lite build"
    "ghp-import -nfp _output"
)

for cmd in "${cmds[@]}"
do
    read -r -p "${cmd}?[Y/n] " input
    case $input in
        [yY][eE][sS]|[yY]|'')
            echo "Executing..."
            eval $cmd
        ;;
        [nN][oO]|[nN])
            echo "Skipped..."
        ;;
        *)
            echo "Invalid input..."
            exit 1
        ;;
    esac
done
