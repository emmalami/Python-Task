# Create a class called Human
# Add an attribute leg_count with the value of 4
# Add a method called get_gender() that returns "Unknown" in the Human class
# Create another class called Man that extends Human

# Optionally you can instantiate the classes Man and Woman then print out the values of the get_gender() method
# in each object instance

class Human:
    race = "black"
    continent = "Afica"
    leg_count = 4
    can_walk = True

    def get_gender(self):
        print("\nHuman {", self.race, ",", self.leg_count, ",", self.continent + " }")


class Man(Human):
    pass


Man = Man()
Man.get_gender()
