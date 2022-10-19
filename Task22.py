# Create a class called Hunt
# Create a private attribute called __weapon with the value "Assault Rifle" in the Hunt class
# Create a method get_weapon() that returns "Not Available" in the Hunt class
# Instantiate an object of the Hunt class
# Print the value of get_weapon() from the object instance

class Hunt:
    __weapon = "Assault Rifle"
    __bullet = 40

    def get_weapon(self):
       return "Hunt " + self.__weapon

    def get_bullet(self):
        value = self.__bullet * 6
        return value

Hunt = Hunt()
print(Hunt.get_weapon())
print(Hunt.get_bullet())