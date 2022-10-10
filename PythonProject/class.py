class phone():
    def __init__(self,model,pro,price,cam):
        self.model=model
        self.pro=pro
        self.price=price
        self.cam=cam
    def spec(self):
        print("Model ={}\nProcessor ={}\nCamera ={}".format(self.model,self.pro,self.cam))
    def pri(self):
        print("Price =",self.price)

class laptop(phone):
    def __init__(self,model,pro,price,cam,st):
        super().__init__(model,pro,price,cam)
        self.st=st
    def store(self):
        print("Storage Type =",self.st)

realme=phone("XT","SD712",20000,"64MP")

mac=laptop("Air","M1",110000,"5MP","SSD")
mac.spec()
mac.store()

realme.spec()
realme.pri()
oneplus.spec()