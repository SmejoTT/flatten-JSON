#!/bin/bash
export BASEDIR=$(dirname "$0")
cat "$BASEDIR/../data/test1.json" | python3 "$BASEDIR/../../flattenJSON.py" > "$BASEDIR/actual_output.json"