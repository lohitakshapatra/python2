class Car(object):
    def __init__(self,company,model,color,speed_limit):
        self.company=company
        self.model=model
        self.color=color
        self.speed_limit=speed_limit

    def start(self) :
        print("started") 
    def stop(self):
        print("stopped")

    def accelerate(self) :
        print("acceleration")
    def change_gear(self,gear_type ):
        print("gear_changed")

audi=Car("audi","Q7","white",180)
print(audi.start())
print(audi.color)
print(audi.accelerate())