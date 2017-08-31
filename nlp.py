# coding: utf-8

import csv
import re
import nltk
import string
import unicodedata
import sys

new_file = csv.reader(open("base_teste.csv", "r", encoding="utf-8"))

list_docs = []

list_label = []

for row in new_file:
    print(row)
