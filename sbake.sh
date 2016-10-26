#!/bin/bash -e
{
    cat $1
    echo
    echo "import databaker.databakersolo"
    echo "databaker.databakersolo.runall(per_file, per_tab, '$1')"
} > dbs.py

PYTHONPATH=$PYTHONPATH:"/home/sm/.virtualenvs/databaker/src/databaker/" python dbs.py "${@:2}"

