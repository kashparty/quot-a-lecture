from os import listdir
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import re

nltk.download("wordnet")
nltk.download("omw-1.4")
lemmatizer = WordNetLemmatizer()


def precalc_counts():
    counts = dict()
    files_dir = "panopto-api-stuff/"
    filenames = [f for f in listdir(files_dir) if f.endswith(".txt")]
    for filename in filenames:
        file = open(files_dir + filename, "r")
        for word in map(
            lambda w: lemmatizer.lemmatize(w),
            filter(
                lambda c: c != "",
                re.sub("[\n,.;@#?!&$]+", " ", file.read().lower()).split(" "),
            ),
        ):
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts


def save_counts():
    file = open("PrecalculatedCounts.dat", "wb")
    pickle.dump(precalc_counts(), file)
    file.close()


if __name__ == "__main__":
    save_counts()
