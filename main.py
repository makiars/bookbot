
def openfile():
    with open("books/frankenstein.txt") as f:
        return f.read()

def cntword():
    str = ""
    i = 0
    str = openfile()
    str = str.split()
    return len(str)

def main():
    num = cntword()
    print(num)

main()
