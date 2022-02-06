from os import listdir

files_dir = "panopto-api-stuff"
filenames = [f for f in listdir(".") if f.endswith(".txt")]


def fixFile(file):
    temp = open(file, "r")
    data = str(bytes(temp.read(), "utf-16").decode('utf-8', 'ignore').encode("utf-8"))
    temp.close()
    temp = open(file, "w")
    temp.write(data)
    temp.close()


for filename in filenames:
    fixFile(filename)
