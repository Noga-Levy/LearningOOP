"""
Written on 26 of June 2025, by Noga Levy.

This program is 1 out of 6 programs I made using Corey Schafer's (a YouTube channel) tutorials. These are the links to
the videos used for this program:
https://www.youtube.com/watch?v=ZDa-Z5JzLYM

"""
import random


# VOCAB
# Methods: A function associated with a class
# Attributes: Data associated with a class

# Let's just say that we are a company, and we want to know some information for each employee--what they do (methods),
# their name (attributes), etc. We don't want to have to redefine that "this is their job, this is there name..." for
# each employee/object, so we have a class that will serve as a blueprint for each employee.
# It's kind of like the DnD classes--XXX could be a WIZARD with brown eyes and the ability to cast fireball.
# Anyway, back to employees. We create a class like so (with two blank lines before):


class Employees:  # class [class name]
    pass  # If we want an empty class (for now), we can either do "..." or "pass". pass is the better option.

# For now, if we define anything as Employee, nothing will happen to it (the blueprint is nothing). So for the variable
# below, it's nothing... except for a class INSTANCE. It's an instance of a class. New thing to add to VOCAB:
# Class instance: Something that uses the class blueprint.


employee1 = Employees()  # Notice how there isn't anything to put in the parameter.

# Now, with this distinction, it is easier to understand another: the difference between instance variables and class
# variables. Instance variables only apply to the single instance it was made for. Here's an example

employee1.name = "John Doe"
# I can print this out:
print(employee1.name)

# But if I made an employee2, it would not come automatically with a name, as the name attribute was only referencing
# the employee it was created for--employee 1.
employee2 = Employees()

try:
    print(employee2.name)
except AttributeError:  # "There isn't this attribute in the class, nor in the instance itself--ERROR"
    print("Employee 2 did not set their name")  # Employee 2 does not have a name. Employee 2 is nameless.

# So now, let's create a new class, EmployeesV2, so we can add "name" (and a few other things) to the blueprint


class EmployeesV2:

    # Below is a special function/method--it defines the attributes/parameters of the class instances. If we add name,
    # it will be automatically added as an attribute (potentially with an empty value) to each class instance
    def __init__(self, name_last, name_first, monthly_pay):
        # Now, to do something with this. We define how to call each attribute, and what the call finds as the value.
        self.name_last = name_last  # If the instance is Mr. Doe, then the call is Doe.name_last, and the result is Doe.
        self.name_first = name_first
        # We can also create a method (without a partner from __init__)--here's an example:
        self.email = f"{name_first + name_last}@company.com"
        self.monthly_pay = monthly_pay
        self.salary = float(monthly_pay * 12)

        # NOTE: These are all ATTRIBUTES. Though you can call them, they don't do anything themselves.


# Let's give this new class a try:
employee3 = EmployeesV2("Smith", "John", 10567.35)
print(f"{employee3.name_last}\n"
      f"{employee3.name_first}\n"
      f"{employee3.email}\n"
      f"{employee3.monthly_pay}\n"
      f"{employee3.salary}")  # Here's why it gives so many decimals: https://0.30000000000000004.com/

# Huzzah! It works! Now, onto version 3: with methods (functions)!


class EmployeesV3:
    def __init__(self, name_last, name_first, monthly_pay):
        self.name_last = name_last
        self.name_first = name_first
        self.email = f"{name_first + name_last}@company.com"
        self.monthly_pay = monthly_pay
        self.salary = float(monthly_pay * 12)

    def review_signoff_request(self):  # If we don't add self, then we will be giving 1 parameter--the employee--when
        # the function only accepts 0. employee.review_signoff_request() contains a parameter in of itself.
        # This is not the case, though, for calling EmployeeV3.review_signoff_request(), though.

        percent_signoff = random.randrange(0, 2)

        if percent_signoff == 0:
            return f"{self.name_first} {self.name_last} will not sign off on this."
        else:
            return f"{self.name_first} {self.name_last} will sign off on this."


# As you can see, where attributes are for data, methods are for functions or actions. Let's make our final employee of
# the lesson to demonstrate this.

employee4 = EmployeesV3("Johnson", "John", 10000)
print(employee4.review_signoff_request())
