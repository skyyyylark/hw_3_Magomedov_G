# class User:
#     id = 123
#     surname = "Ivanov"
#
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#
#
# u1 = User("John", 28)
# u2 = User("Yuryi", 26)
#
# print(u1.name, u1.age)
# print(u2.name, u2.age)




class Robot:
    """This is a program"""
    cpu = "intel"
    gpu = "nvidia"
    source = "metal"
    coef = 0.8 #коефициент выносливости металла


    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hardness = 20


    @classmethod
    def change_h(cls, num):
        cls.coef += num



    def wash_car(self):
        """this method shows the washing process"""
        print(f"Washing car by {self.name}")

    def change_name(self, new_name):
        print(f" {self.name}'s name has been changed to {new_name}")
        self.name = new_name


    @classmethod
    def change_cpu(cls):
        cls.cpu = "AMD"
        print(f"CPU has been upgraded to {cls.cpu}")

print(Robot.__doc__)

rob1 = Robot(312, "Sally")
rob2 = Robot(123, "Sam")

rob2.change_h(0.3)

print(f"Robot 1 - Name: {rob1.name}, ID: {rob1.id}, CPU: {rob1.cpu}, Endurance: {rob2.coef}; Robot2 - Name: {rob2.name}, ID: {rob2.id}, CPU: {rob2.cpu}, Endurance: {rob2.coef}")
rob1.change_name("Zach")
rob2.change_name("T5000")
print(" ")
print(f"Robot 1 - Name: {rob1.name}, ID: {rob1.id}, CPU: {rob1.cpu}, Endurance: {rob2.coef}; Robot2 - Name: {rob2.name}, ID: {rob2.id}, CPU: {rob2.cpu}, Endurance: {rob2.coef}")
# rob1.wash_car()

rob1.change_cpu()
print(f"Robot 1 - Name: {rob1.name}, ID: {rob1.id}, CPU: {rob1.cpu}, Endurance: {rob2.coef}; Robot2 - Name: {rob2.name}, ID: {rob2.id}, CPU: {rob2.cpu}, Endurance: {rob2.coef}")







