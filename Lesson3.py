"""
Written on 9 of July 2025, by Noga Levy.

This program is 3 out of 6 programs I made using Corey Schafer's (a YouTube channel) tutorials. This is the link to
the video used for this program:
https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3
All about class methods
"""

import random

# From last time...


class Employees:
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
        self.salary = round(self.salary * self.raise_amount, 2)

    # Perfect, our class! You know what's missing from this class, though? Variety.
    # All these method parameters begin with self... BORING. But what else can we put it instead of self?
    # Answer: "cls," which stands for class (we can't use "class" itself, as it already has its own meaning in python).
    # It's used for class methods, which, unlike regular methods, work with the class, not the instance.
    # So, let's switch things up with a CLASS METHOD, which we define like so...

    @classmethod  # <-- This is one of many DECORATORS. The decorator, in this case, alters the functionality of the
    # method below, making it a class method with cls as the first parameter
    def change_raise_amt(cls, new_amount):
        previous_amount = cls.raise_amount
        # See how we replaced Employees.raise_amount cls.raise_amount?
        # They're the same--cls is Employees, and Employees is cls

        cls.raise_amount = new_amount
        return f"The raise amount has been changed from {previous_amount} to {new_amount}"

    # Let's give this a go!


emp1 = Employees("1", "Employee", 8000)

print(Employees.raise_amount)
print(emp1.raise_amount)

print("\n")

# Before, when we wanted to change the raise amount, we'd have to do this:
Employees.raise_amount = 1.05
print(Employees.raise_amount)
print(emp1.raise_amount)

print("\n")

# But, now, we can simply do this:
print(Employees.change_raise_amt(1.02))  # We call the class method with Employees
print(Employees.raise_amount)
print(emp1.raise_amount)

print("\n")

# Though, we could also call it with the instance emp1, and it will still be a class-wide change:
print(emp1.change_raise_amt(1.05))  # It just doesn't make much sense, and nobody really does this
print(Employees.raise_amount)

# Now, some people use class methods as "alternative constructors," or as an alternative way to make an instance of the
# class.
# Paused at 8:19
