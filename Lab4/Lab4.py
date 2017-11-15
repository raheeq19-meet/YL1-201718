#class Animal(object):
    #def __init__(self,sound,name,age,favorite_color):
        #self.sound=sound
       # self.name=name
      #  self.age=age
     #   self.favorite_color=favorite_color
    #def eat(self,food):
     #   print("yummy!"+self.name+"is eating"+food)
    #def description(self):
   #     print(self.name+"is"+self.age+"years old and loves the color"+self.favorite_color)
  #  def make_sound(self,sound):
 #       print(self.sound*3)
#cat=Animal("meow","defo",1,"white")
#cat.eat("milk")
#cat.make_sound("meow")


class Person(object):
    def __init__(self,name,age,city,gender):
        self.name=name
        self.age=age
        self.city=city
        self.gender=gender
    def eat(self,food):
        print(self.name+"is eating"+food)
    def sport(self,sport):
        print(self.name+"loves playing"+sport)
    
Raheeq=Person("Raheeq",15,"Iksal","female")
Raheeq.eat("pancakes")
Raheeq.sport("volleyball")




