from os import listdir

files_dir = "panopto-api-stuff"
filenames = [f for f in listdir(".") if f.endswith(".txt")]


def fix_file(file):
    temp = open(file, "rb")
    data = str(temp.read().decode('utf-8', 'ignore').encode("utf-8"), "utf-8")
    temp.close()
    temp = open(file, "w")
    temp.write(data)
    temp.close()


for filename in filenames:
    fixFile(fix_file)
    #with open(filename, encoding="utf-8") as f:
    #    f.read()

