#!/bin/bash
gq=$(sed 's/ /+/g' <<< "$*")
osascript -e "tell application \"Safari\" to search the web for \"$*\"";

