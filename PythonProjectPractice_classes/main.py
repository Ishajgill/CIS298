
class Boat:
    def __init__(self,n,o):
        print("Hey there")
        self.name = n
        self.owner = o
    def info(self):
        print(f"{self.name} is a {self.owner}")
a = Boat('Sam','Taj')
a.info()


