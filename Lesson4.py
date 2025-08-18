"""
Written on 14 of August 2025, by Noga Levy.

This program is 4 out of 6 programs I made using Corey Schafer's (a YouTube channel) tutorials. This is the link to
the video used for this program:
https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4
All about inheritance and creating subclasses
"""

# Q: Why do we need inheritance/what does it do?
# A: Inheritance allows us to create SUBCLASSES from an original parent class, giving the child class the same
# functionality as the parent. But, now with the child class, we can overwrite/add new functionality ontop of the
# previous class's.

# Let's make an example. Previously, we made a class for company employees and a class for company events. Wouldn't it
# be nice if we could now use that Employees class for a developer and manager class?
# (NOTE: What makes these good candidates for inheriting is the fact that they can need the same __init__ parameters
# as the original Employee class)

# Previous class...
import random


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

    @classmethod
    def from_slashed_str(cls, string):
        lastname, firstname, pay = string.split("/")
        return cls(lastname, firstname, int(pay))


# Now, to create a subclass: We start by calling class and naming the new class:


class Developer(Employees):  # But, this time, we add a bracket and Employees to signify "THESE ARE THE PARENT CLASSES"
    # If we wanted, we could add a comma after Employees and add another parent class
    pass  # We'll do pass for now--let's test something


developer1 = Employees("Billy", "Bob", 9000)
# If we print the monthly pay and email of Mr. Billy, we will get our expected result of 9000 and BobBilly@company.com:

print(f"{developer1.monthly_pay}, {developer1.email}")

# And, now, if we make an identical employee, but with the Developer class instead of, it will return the exact same
# result as before

developer1 = Developer("Billy", "Bob", 9000)  # Developer has the same functionality as
# Employees, since we accessed Employees from it.
print(f"{developer1.monthly_pay}, {developer1.email}")  # Returns: 9000, BobBilly@company.com.

# What Python does is check the __init__ method for the .monthly_pay and .email methods, and after finding nothing, it
# goes up the chain of parents until it reaches the closest definition. This is called the "METHOD RESOLUTION CHAIN."
# We can visualize this with the "help" command:

print(help(Developer))  # We can get lots of good information from this, but the one were interested in right now is


# almost at the very top: "Method resolution order." It shows where Python is searching for the attributes and methods,
# starting with Developer (the newest child class), Employees (the parent class to Developer), and, finally,
# builtins.object, which is the base parent class that all Python classes inherit from automatically.

# This is cool and all, but we don't need an Employees clone. We need a new class using the functionality of the parent,
# plus some new abilities. So, we'll make a DeveloperV2 class, but this, add the dev's primary programming language:


class DeveloperV2(Employees):

    def __init__(self, name_last, name_first, monthly_pay, programming_lang: str):  # We make take the __init__ from
        # Employees, adding programming_lang as a parameter
        # Now we have the parameters, we need to let Python know that Employees should handle name_last,
        # name_first, and monthly_pay, and DeveloperV2 will define programming_lang. For the Employee part, we use
        # super().__init__(para1, para2, ... , paraX) to let the parent class handle the parameters specified:
        super().__init__(name_last, name_first, monthly_pay)

        # We could have also done "Employee.__init__(self, name_first, monthly_pay)", but when we have multiple
        # inheritances, it becomes a must to use super.

        # As for the programming_lang parameter, we just define it as usual:
        self.programming_lang = programming_lang


# Let's test this out!

developer2 = DeveloperV2("Dev", "Two", 9225, "Python")  # The best
# langauge for the best developer so far, of course.

print(f"\n{developer2.monthly_pay}, {developer2.email}")  # Returns: 9225, TwoDev@company.com.
print(f"{developer2.programming_lang}")


# As a recap, we'll now make a manager:


class Manager(Employees):
    def __init__(self, name_last, name_first, monthly_pay, subordinates: list = None):  # The new parameter will take a
        # list of the employees that the manager is assigned to (with it set to None if no employees report to the
        # manager
        super().__init__(name_last, name_first, monthly_pay)

        # It's bad practice to set mutable data as a default values, so we define self.subordinates = [] like so:
        if subordinates is None:
            self.subordinates = []
        else:
            self.subordinates = subordinates

        """
        Side Note:
        Here's and example why it is a bad idea to put mutable values as defaults 
        
        
        def add_to_list(item, my_list=[]):
            my_list.append(item)
            return my_list
        
        print(add_to_list(1))  # Output: [1]
        print(add_to_list(2))  # Output: [1, 2] - Unexpected!
        print(add_to_list(3, [4])) # Output: [4, 3] - This works as expected
        
        
        The common practice to initialize the default as None and change it within the function if the value is None. 
        This is exactly what we did above with self.subordinates.
        
        TL;DR: The changes in mutable carry over to subsequent calls and causes errors. The best practice is to set the
        default to None and change it later in the function
        """

    def add_emp(self, emp):
        if emp in self.subordinates:
            return f"Employee {emp.name_last}, {emp.name_first} already exists"
        else:
            self.subordinates.append(emp)
            return f"{emp.name_last}, {emp.name_first} is now an employee for {self.name_last}, {self.name_first}"

    def remove_emp(self, emp):
        if emp not in self.subordinates:
            return (f"{emp.name_last}, {emp.name_first} was not an employee of {self.name_last}, {self.name_first}"
                    f"--they cannot be removed.")

        else:
            self.subordinates.remove(emp)
            return (f"{emp.name_last}, {emp.name_first} is now no longer an employee of {self.name_last}, "
                    f"{self.name_first}")

    def print_employees(self):
        print(f"The subordinates of {self.name_last}, {self.name_first} are as follows:")
        for emp in self.subordinates:
            print(f"--> {emp.name_last}, {emp.name_first}")


# We test the class:

testDev = DeveloperV2("For", "Example", 1234, "Java")

print("\n")
managerMolly = Manager("Mol", "Molly", 10000, [developer2])
print(managerMolly.email)  # Check that original functionality still exist
print("\n")

# Check that adding an employee is successful
print(managerMolly.add_emp(testDev))
managerMolly.print_employees()
print("\n")

# Check add_emp error handling
print(managerMolly.add_emp(testDev))
managerMolly.print_employees()
print("\n")

# Check remove_emp functionality
print(managerMolly.remove_emp(testDev))
managerMolly.print_employees()
print("\n")

# Check remove_emp error handling
print(managerMolly.remove_emp(testDev))
managerMolly.print_employees()

# All successes! Woohoo!
