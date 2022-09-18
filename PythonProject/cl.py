class rock():
    def __init__(self,name,age,dia):
        self.name=name
        self.age=age
        self.dia=dia
    def intro(self):
        print("Hey,I am",self.name,"and i am",self.age,"years old\nDialogue:",self.dia)
    def sound(self):
        print("Bark...!")
'''mil=rock("Eleven",14,"Bitching")
mil.intro()
mil.sound()'''

class paper(rock):
    def __init__(self,name,age,color):
        super().__init__(name,age,color)
        self.color=color
    def sound(self):
        print("Meow...!")
mike=paper("Mike",12,"Blue")
mike.intro()
mike.sound()
jake=rock("Jake",17,"Biatch")
jake.intro()
jake.sound()