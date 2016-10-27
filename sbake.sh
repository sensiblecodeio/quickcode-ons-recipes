#!/bin/bash -e
{
    cat "$1"
    echo
    echo "import databaker.databakersolo"
    echo "databaker.databakersolo.runall(per_file, per_tab, '$1')"
} > dbs.py

full_bake_path=$(which bake)
parent_bake_path=$(dirname "$full_bake_path")
databaker_path=${parent_bake_path}/../src/databaker/
PYTHONPATH=$PYTHONPATH:$databaker_path python dbs.py "${@:2}"
