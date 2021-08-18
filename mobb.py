
import rectangulop
v=10
class Kilo:
    def __init__(self,a,figure):
        self.x = 0
        self.y = 0
        self.base =a
        self.bso =a
        self.xVelocity=0.5
        self.yVelocity=0.5
        self.rectangle = self.base.create_rectangle(figure[0], figure[1], figure[2], figure[3], fill = figure[4])
        self.pelota = self.bso.create_rectangle(100,100,110,110,fill='red')

        self.movement()
    def movement(self):
        self.bso.move(self.pelota,self.xVelocity,self.yVelocity)
        self.base.move(self.rectangle, self.x, self.y)
        coor_a=self.base.coords(self.rectangle)
        print(coor_a)
        coorp = self.bso.coords(self.pelota)
        print(coorp)
        self.avc=rectangulop.rectangulop(coor_a,coorp)
        print(self.avc)
        if self.avc ==True :
            self.xVelocity*=-1
        if(coorp[2]>=(self.bso.winfo_width())or coorp[0]<0):
            self.xVelocity *=(-1)
        if(coorp[3]>=(self.bso.winfo_height())or coorp[1]<0):
            self.yVelocity *=(-1)
        #self.canvas.move(self.image,self.xVelocity,self.yVelocity)


        self.x=0
        self.y=0
        self.base.after(1, self.movement)
    def left(self, event):
        print(event.keysym)
        self.x = -v
        self.y = 0
    def right(self, event):
        print(event.keysym)
        self.x = v
        self.y = 0
    def up(self, event):
        print(event.keysym)
        self.x = 0
        self.y = -v
    def down(self, event):
        print(event.keysym)
        self.x = 0
        self.y = v
    def o(self,event):
        print(event.keysym)
        self.x = 0
        self.y = 0
