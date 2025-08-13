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

    @classmethod  # <-- This is one of many DECORATORS. The decorator, in this case, alters the functionality of
    # the method below, making it a class method with cls as the first parameter
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

# But now, we can simply do this:
print(Employees.change_raise_amt(1.02))  # We call the class method with Employees
print(Employees.raise_amount)
print(emp1.raise_amount)

print("\n")

# Though, we could also call it with the instance emp1, and it will still be a class-wide change:
print(emp1.change_raise_amt(1.05))  # It just doesn't make sense, and nobody really does this
print(Employees.raise_amount)

# Now, some people use class methods as "alternative constructors," or as an alternative way to make an instance of the
# class.

# How can we do this?

# Well, we'll get back our class:


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

    @classmethod
    def change_raise_amt(cls, new_amount):
        previous_amount = cls.raise_amount
        cls.raise_amount = new_amount
        return f"The raise amount has been changed from {previous_amount} to {new_amount}"

    # And now, we make our alternative constructor (and figure our why we want it).

    # Let's just say that, at the beginning, we receive the employee's name and pay in the form of "Last/First/Pay."
    # Instead of transforming that string into three separate strings, and then adding those to an instance definition,
    # we can create a class method--that returns an instance--that does it for us.

    @classmethod
    def from_slashed_str(cls, string):  # The general convention is to use "from" to denote an alternative constructor.
        lastname, firstname, pay = string.split("/")
        return cls(lastname, firstname, int(pay))


# We can test this out:
example_string = "Doe/John/9000"
emp3 = Employees.from_slashed_str(example_string)

# And we double-check to see if it worked:
print(f"\nExpected result vs actual"
      f"\nLast: Doe vs {emp3.name_last}"
      f"\nFirst: John vs {emp3.name_first}"
      f"\nMonthly pay: 9000 vs {emp3.monthly_pay}")

# Success!

# And, you know what else we can do? Instead of having the starting parameter be either self or cls, we can have NO
# parameter. We call these "static methods," as they don't regard the class or the instance. Static methods are,
# basically, just functions that we include in the class because they have some sort of logical connection. Here's an
# example:


class CompanyEvents:
    num_attending_weekend = 0

    def __init__(self, interest: bool, free_on_weekends: bool):
        self.free_on_weekends = free_on_weekends
        self.interested = interest

        if self.free_on_weekends and self.interested:
            CompanyEvents.num_attending_weekend += 1

    # Method
    def weekend_event(self):
        if self.free_on_weekends and self.interested:
            events = ["dinner party", "barbecue", "skill session"]

            return f"This weekend, you will be going to the company {random.choice(events)} event."
        else:
            return None

    # Class Method
    @classmethod
    def num_attendees_weekend(cls):
        return f"There will be {cls.num_attending_weekend} employees attending this event."

    # And now, a static method (which is, of course, related to company events, but doesn't need to have any fancy cls
    # or self parameters)
    @staticmethod  # Using this decorator, we tell Python "Don't worry about accessing information from the class or
    # instance--all we need is the information from the parameters."
    def taco_day(cheesy_tacos: bool = None):
        business_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        if cheesy_tacos:
            return f"Free cheesy tacos will be given out on {random.choice(business_days)}"

        elif cheesy_tacos is False:
            return f"Free cheese-less tacos will be given out on {random.choice(business_days)}."

        else:
            return f"Free tacos will be given out on {random.choice(business_days)}."


# Just making some space in the terminal for the next part
print("\n \n")

BillyBob = CompanyEvents(True, True)

print(BillyBob.weekend_event())  # Will return the "This weekend, ..." message
print(BillyBob.num_attendees_weekend())  # Will return 1 as there is only one instance that is both interested and
# available to attend the company event
print(BillyBob.taco_day())  # If Billy Bob just wanted to know when they company was going to give out, say, free tacos
# to all of its employees, he could just call the method and find out. (Whether they are serving cheesy, cheeseless, or
# both kinds of taco, Billy Bob doesn't care.)
# If Billy Bob specifically wanted to know when the cheesy tacos were/weren't being given out, he could insert a bool
# into the cheesy_tacos parameter:

print(f"\n{BillyBob.taco_day(True)}")
print(BillyBob.taco_day(False))
