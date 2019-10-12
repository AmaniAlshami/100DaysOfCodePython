class Library:
    def __init__(self,book,shelf):
        self.book = book
        self.shelf = shelf 
    
class ScienceSection(Library):
    def __init__(self,book,shelf,name):
        super().__init__(book,shelf)
        self.name = name


obj = ScienceSection(book=300,shelf=45,name="Physics books")
print(obj.book,obj.shelf,obj.name)
obj.shelf = 4 
obj.book = 20
print(obj.book,obj.shelf,obj.name)

