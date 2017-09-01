# coding: utf-8

import csv
import re
import nltk
import string
import unicodedata
import sys

#def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
#    enc = file.encoding
#    if enc == 'UTF-8':
#        print(*objects, sep=sep, end=end, file=file)
#    else:
#        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
#        print(*map(f, objects), sep=sep, end=end, file=file)

def remove_url(text):
    clean_text = re.match(r"(.*?)http.*?\s?(.*?)$", text)
    if clean_text:
       return clean_text.group(1)
    else:
        return text

def remove_hashtag(text):
    words = text.split()

    for w in words:
        if w.startswith("#") or w.startswith("@"):
            words.remove(w)            
    
    return " ".join(words)

def remove_stopwords(text):
    regex = re.compile('[%s]' % re.escape(string.punctuation))

    a = []
    
    words = text.split()
    for word in words:
        new_token = regex.sub(u'', word) 
        if not new_token == u'':
            a.append(new_token)

    stop_words = nltk.corpus.stopwords.words("portuguese")
    content = [w for w in a if w.lower().strip() not in stop_words]
    
    clean_text = []
    for word in content:
        nfkd = unicodedata.normalize("NFKD", word)
        palavra_sem_acento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
 
        q = re.sub("[^a-zA-Z0-9\\\]", " ",palavra_sem_acento)

        clean_text.append(q.lower().strip())

    tokens = [t for t in clean_text if len(t) > 2 and not t.isdigit()]
    ct = " ".join(tokens)

    return ct


new_file = csv.reader(open("base_masterchef.csv", "r", encoding="utf-8", newline="\n"))

list_docs = []

list_label = []

for row in new_file:
    doc_text = remove_hashtag(row[0]) 
    doc_text = remove_stopwords(doc_text)
    doc_text = remove_url(doc_text)

    print(doc_text)
