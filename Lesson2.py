"""
Written on 8 of July 2025, by Noga Levy.

This program is 2 out of 6 programs I made using Corey Schafer's (a YouTube channel) tutorials. This is the link to
the video used for this program:
https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2
All about class variables
"""

import random

# Let us retrieve our final class from Lesson 1 and play around with it...


class EmployeesV1:

    def __init__(self, name_last, name_first, monthly_pay):
        self.name_last = name_last
        self.name_first = name_first
        self.email = f"{name_first + name_last}@company.com"
        self.monthly_pay = monthly_pay
        self.salary = float(monthly_pay * 12)

    def review_signoff_request(self):

        percent_signoff = random.randrange(0, 2)

        if percent_signoff == 0:
            return f"{self.name_first} {self.name_last} will not sign off on this."
        else:
            return f"{self.name_first} {self.name_last} will sign off on this."

    # Alright, that's where we left off!
    # Now, let's just say our employees have been working hard in the debugging trenches and now all want the same
    # raise to their salary.
    # We could create a method that applies a hardcoded amount, like so

    def apply_raise(self):
        self.salary = round(self.salary * 1.02, 2)


# Test it out:
emp1 = EmployeesV1("Doe", "John", 9000)
print(emp1.salary)
emp1.apply_raise()
print(emp1.salary)
# 110160/108000 = 1.02; thus, our code works.

# However, hardcoding can cause use a headache later, like if we want to change the value, or figure out what it
# means. Usually, we would use a variable to replace the hard code, and problem solved. As the class version of a
# variable is an attribute, should we make a raise_amount attribute?
# No!
# Attributes are made for storing data SPECIFIC TO EACH INSTANCE, and this is just a set number. Although one COULD
# use an attribute, it is better to use a CLASS VARIABLE.

# VOCAB:
# Class variables: Variables that are shared between all instances of a class.

# So, instead, let us create a class variable in V2 of Employees.


class EmployeesV2:
    # To create a class variable, we place the definition here.
    raise_amount = 1.02

    def __init__(self, name_last, name_first, monthly_pay):
        self.name_last = name_last
        self.name_first = name_first
        self.email = f"{name_first + name_last}@company.com"
        self.monthly_pay = monthly_pay
        self.salary = float(monthly_pay * 12)

    def review_signoff_request(self):

        percent_signoff = random.randrange(0, 2)

        if percent_signoff == 0:
            return f"{self.name_first} {self.name_last} will not sign off on this."
        else:
            return f"{self.name_first} {self.name_last} will sign off on this."

    def apply_raise(self):
        # So now, instead of hardcoding 1.02 in here--and who knows where else!--we simply put self.raise_amount or
        # EmployeesV2.raise_amount().
        # Why do we need to do this?
        # Because class variables don't exist by themselves--we must call them from one of their containers, like the
        # class itself (EmployeesV2.raise_amount()), a class instance, or anything that had inherited from a class that
        # contained the variable.

        self.salary = round(self.salary * self.raise_amount, 2)
        # Let's give it a try


emp2 = EmployeesV2("Doe", "Jane", 9000)
print(f"\n{emp2.salary}")
emp2.apply_raise()
print(emp2.salary)
# Success!

# Now, just to highlight something, take a look at this:
print(f"\n{emp2.__dict__}")  # .__dict__ provides a dictionary of attributes
print(emp2.raise_amount)
# As you can see, raise_amount is NOT an attribute. It is simply being called from the class, which we can check here:
print(f"\n{EmployeesV2.raise_amount}")
print(EmployeesV2.__dict__)
# As shown in the terminal, one of the "attributes"--
# SIDE NOTE: .__dict__ returns class attributes, methods, and other class-level variables for classes
# --of EmployeeV2 is "raise_amount," whose corresponding value is 1.02, just like how we set it.

# The crème de la crème of this ability, though: we can change the value of the class variable OUTSIDE the class.

EmployeesV2.raise_amount = 1.05  # Increasing the amount is as simple as that!
print(f"\n{EmployeesV2.raise_amount}")
print(emp2.raise_amount)
# And it works! Now, what happens if emp3 wants a higher raise (since the other two are slacking off)? We change the
# raise amount, but instead of using with EmployeesV2, we use emp3:
emp3 = EmployeesV2("Hard", "Working", 10000)
emp4 = EmployeesV2("Infinite", "Coffee-break", 10000)
emp3.raise_amount = 1.1
# Now if we edit his salary, it will have an increase of 10%.
print(f"\n{emp3.salary}")
emp3.apply_raise()
print(emp3.salary)
# Versus
print(emp4.salary)
emp4.apply_raise()
print(emp4.salary)
# Huh, the change ONLY GOES FOR emp3! We defined the change specifically in emp3's instance; thus, it will only affect
# him. Let's check something, then...
print(emp3.__dict__)
print(emp4.__dict__)
# Aha! Here we see it more clearly: when we define a change in class variables for one instance, the instance adds it as
# an attribute, as it is specific to the instance.
# This also means, back in .apply_raise(), if we set the raise_amount-caller to Employee, it will remain as the general
# value for raises, whereas when we put self.raise_amount that takes from each instance's .raise_amount.
