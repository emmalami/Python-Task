# Create a class called Human
# Add an attribute leg_count with the value of 4
# Add a method called get_gender() that returns "Unknown" in the Human class
# Create another class called Man that extends Human
# Create another class called Woman that extends Human
# In the class, Man create the method get_gender() which should return "man"
# In the class, Woman create the method get_gender() which should return "woman"
# Instantiate the Man and Woman classes
# Print out the value of get_gender() from the Man and Woman object instances
class Human:
    race = "black"
    continent = "Afica"
    leg_count = 4
    can_walk = True

    def get_gender(self):
        print("Human")


class Man(Human):

    def get_gender(self):
        print("Man")


class Woman(Human):

    def get_gender(self):
        print("Woman")

man = Man()
Man.get_gender("self")

Woman = Woman()
Woman.get_gender()