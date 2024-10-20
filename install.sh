#!/bin/sh
rm -r ${HOME}/.local/share/icons/Anya_Cursor
cd xcursor
./generate.py
mkdir -p ${HOME}/.local/share/icons/Anya_Cursor
cp -r cursors ${HOME}/.local/share/icons/Anya_Cursor
cp index.theme ${HOME}/.local/share/icons/Anya_Cursor
