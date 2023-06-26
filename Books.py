class Book:
    def __init__(self,name="",price=0,edition=0):
        self.name=name
        self.price=price
        self.edition=edition
    def __str__(self):
        return self.name+" "+str(self.price)+" "+str(self.edition)
    
