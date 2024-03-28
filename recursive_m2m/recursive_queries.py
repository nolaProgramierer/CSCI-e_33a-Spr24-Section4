# Import Employee model
from flights.models import *


# Make 3 employees
e1 = Employee(fname="Caroline", lname="Bower")
e1.save()

e2 = Employee(fname="Heather", lname="Bond")
e2.save()

e3 = Employee(fname="Dominic", lname="Blake")
e3.save()

# Return the first names of all employees
e1.fname
e2.fname
e3.fname

# Make Dominic a boss
e3.boss= True
e3.save()

#Confirm Dominic is a boss
e3.boss

# Make Dominic the supervisor of Caroline (front side of relationship)
e1.fname
e3.fname
e1.supervisors.add(e3)
e1.save()

# Confirm Caroline has Dominic as a boss
e1.fname
e1.supervisors.all()

# Make Dominic the supervisor of Heather (opposite side of the relationship)
e3.fname
e2.fname
e3.subordinates.add(e2)
e3.save()

# Confirm the Dominic is the supervisor of Heather
e2.fname
e2.supervisors.all()

# Return all of Dominics subordinates
e3.fname
e3.subordinates.all()

# Make Dominic his own boss
e3.fname
e3.subordinates.add(e3)
e3.save()

# Confirm Dominic is his own boss
e3.is_boss_of_himself()

# Confirm that Dominic as a boss has subordinates
boss = Employee.objects.get(boss=True)
boss.boss_has_subordinates()


# --------------------------------------------------
#                   Q queries
# --------------------------------------------------

# Let's add 3 more employees
e4 = Employee(fname="Phil", lname="Russel")
e4.save()

e5 = Employee(fname="Grace", lname="White")
e5.save()

e6 = Employee(fname="Liam", lname="Rees")
e6.save()

# Let's make sure we have these objects saved
e4.fname
e5.fname
e6.fname

# Import Django Q objects
from django.db.models import Q

# Return employees whose last name contains 'ee' and first name contain 'i'
liam = Employee.objects.filter(lname__contains="ee", fname__contains="i")
liam

# Return employees whose last name contains 'ee' OR lname contains 'ss'
double_ltrs = Employee.objects.filter(Q(lname__contains="ee") | Q(fname__startswith="P"))
double_ltrs

# Return employees who's not a boss AND whose last names begin with either 'r' OR 'w' case insensitive
special_employees = Employee.objects.filter( Q(lname__istartswith="R") | Q(lname__istartswith="W", boss=False))
special_employees
