
def openfile():
    with open("books/frankenstein.txt") as f:
        return f.read()

def cntword():
    str = ""
    i = 0
    str = openfile()
    str = str.lower()
    str = str.split()
    return str

def getchardict(str):
    dict = {}
    for s in str:
        for c in s:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
    return dict

def aggregate_char(dict):
    lst = []
    newdict = {}
    for s in dict:
        if s.isalpha():
            newdict["char"] = s
            newdict["num"] = dict[s]
            lst.append(newdict)
            newdict = {}
    return lst

def sort_on(dict):
    return dict["num"]

def printall(wordcnt, lst):
    print(f"{wordcnt} words found in document \n")
    for l in lst:
        print(f"letter {l["char"]} appeared {l["num"]} times .")

def main():
    str = cntword()
    wordcnt = len (str)
    dict = getchardict(str)
    lst = aggregate_char(dict)
    lst.sort(reverse=True, key=sort_on)
    printall(wordcnt,lst)


main()
