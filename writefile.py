def read_file(filename):
    tab = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            # remove the \n at the end of the line
            if line[-1] == "\n":
                line = line[0:-1]
            language = line.split(" ")
            tab.append(language)
    return tab



def add_language(filename, language):
    f = open(filename, "a")
    f.write(language + "\n")
    f.close()


def delete_language(filename, language):
    """delete a language from the file. boulean is used to know if
    the language was succesfully deleted or if it didn't exist"""

    boulean = 0

    # make a list of element of the file
    f_read = open("file.txt", "r")
    lines = f_read.readlines()
    f_read.close()

    # re-write the file with every element except the language
    # we want to delete
    f_write = open(filename, "w")
    for line in lines:
        if line.strip("\n").split(" ")[0] != language:
            f_write.write(line)
        else:
            boulean = 1
    f_write.close()

    if boulean == 0:
        print("language not found")
    else:
        print("language deleted")


filename = "file.txt"
#delete_language(filename, "Elfes")
add_language(filename, "Elfes 1 4 6 8")
read_file(filename)