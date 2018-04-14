global cWidth
global cHeight
cWidth =600
cHeight=600

class shot1(object):
    def __init__(self,a,b):
        self.x=20
        self.y=100
        self.up=0
        self.down=0
        self.left=0
        self.right=0
        
    def show(self):
        fill(0)
        rect(self.x,self.y,10,10)
    def update(self):
        self.y = self.y + self.up

    
#########################################
class player(object):
    def __init__(self):
        self.x=300
        self.y=300
        self.up=0
        self.down=0
        self.left=0
        self.right=0
        self.speed=3
        self.h = 30
        self.w = 20
        
    def show(self):
        fill(0)
        rect(self.x,self.y,self.w,self.h)
    def update(self):
        self.x=self.x +(self.right - self.left)*self.speed
        self.y=self.y +(self.down - self.up)*self.speed
        if not (self.x>=0):
            self.x=0
        if not(self.x <= (cWidth-self.w)):
            self.x = cWith-self.w
        if not (self.y>=0):
            self.y=0
        if not (self.y <=(cHeight-self.h)):
            self.y =(cHeight-self.h)
    
        
def setup():
    size(cWidth,cHeight)
    global p
    global s1,s2,s3,s4,s5
    p = player()
    s1 = shot1(-10,-10)
    s4 = shot2(-10,-10)
    s3 = shot3(-10,-10)
    s4 = shot4(-10,-10)
    
def draw():
    background(100)
    p.show()
    s1.show()
    p.update()
    s1.update()

        
    
def keyPressed():
    if keyCode == UP:
        p.up=1
    if keyCode == DOWN: 
        p.down=1   
    if keyCode == LEFT:
        p.left=1
    if keyCode == RIGHT:
        p.right=1
    if key == ' ':       
        s1.x=p.x
        s1.y=p.y
        s1.up=-1
        
        
      

def keyReleased():
    if keyCode == UP:
        p.up=0
    if keyCode == DOWN: 
        p.down=0   
    if keyCode == LEFT:
        p.left=0
    if keyCode == RIGHT:
        p.right=0  
        
################# not able yet to work with multiple instace of on e object
################# but still learning        
        
class shot(object):
    def __init__(self,a,b):
        self.x=20
        self.y=100
        self.up=0
        self.down=0
        self.left=0
        self.right=0
        
    def show(self):
        fill(0)
        rect(self.x,self.y,10,10)
    def update(self):
        self.y = self.y + s.up
        
class shot2(object):
    def __init__(self,a,b):
        self.x=20
        self.y=100
        self.up=0
        self.down=0
        self.left=0
        self.right=0
        
    def show(self):
        fill(0)
        rect(self.x,self.y,10,10)
    def update(self):
        self.y = self.y + s.up
        
class shot3(object):
    def __init__(self,a,b):
        self.x=20
        self.y=100
        self.up=0
        self.down=0
        self.left=0
        self.right=0
        
    def show(self):
        fill(0)
        rect(self.x,self.y,10,10)
    def update(self):
        self.y = self.y + s.up
        
class shot4(object):
    def __init__(self,a,b):
        self.x=20
        self.y=100
        self.up=0
        self.down=0
        self.left=0
        self.right=0
        
    def show(self):
        fill(0)
        rect(self.x,self.y,10,10)
    def update(self):
        self.y = self.y + s.up
