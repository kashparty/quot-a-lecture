from os import listdir
import re
from time import time
import pickle

def precalc_counts():
    counts = dict()
    files_dir = "panopto-api-stuff/"
    filenames = [f for f in listdir(files_dir) if f.endswith(".txt")]
    for filename in filenames:
        file = open(files_dir+filename, "r")
        for word in split_to_words(file.read()):
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts

def save_counts():
    file = open("PrecalculatedCounts.dat", "wb")
    pickle.dump(precalc_counts(),file)
    file.close()

def load_counts():
    file = open("PrecalculatedCounts.dat", "rb")
    counts = pickle.load(file)
    file.close()
    return counts

def split_to_words(inp):
    return list(filter(lambda c: c != "", re.sub("[\n,.;@#?!&$]+", " ", inp.lower()).split(" ")))

def heuristic(question1, question2):
    value = 0
    counts = load_counts()
    for word in split_to_words(question1):
        if word in question2.lower() and word in counts:
            value += 1/counts[word]
            print(word, str(value))
    for word in split_to_words(question2):
        if word in question1.lower()  and word in counts:
            value += 1/counts[word]
            print(word, str(value))
    return value
    

    





