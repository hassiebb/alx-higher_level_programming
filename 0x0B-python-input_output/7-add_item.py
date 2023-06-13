#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from os import path
from typing import List
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_list(items: List[str]):
    filename = "add_item.json"

    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(items)
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_items_to_list(arguments)