from Books import Book
from pickle import *

# temporary m/y
myStore=[]

# myFile=open("myBookStore.doc","wb")
# myFile.close()

def readFile():
    try:
        myFile=open("myBookStore.doc","rb")
        return load(myFile)
    except EOFError as e:
        return []
    
def writeFile(what):
    myFile=open("myBookStore.doc","wb")
    dump(what,myFile)
    print("Book's are updated")
    myFile.close()
        

def create():
    name=input("Enter the book name ")
    price=int(input("Enter the price "))
    edition=int(input("Enter the edition "))
    book=Book(name,price,edition)
    
    # read
    myStore=readFile()
    
    # write
    myStore.append(book)
    writeFile(myStore)
    #myFile=open("myBookStore.doc","wb")
    #dump(myStore,myFile)
    #myFile.close()
    #print(name+" book has added to stock")


def view():
    myStore=readFile()
    for x in myStore:print(x)
    
        

#create();
view()