from django.db import models

# -----------------------------------------------------------------
# Airport/Flights example
# ------------------------------------------------------------------
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures"
    )
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals"
    )
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

    def is_valid_flight(self):
        return self.origin != self.destination and self.duration > 0


# -----------------------------------------------------------------
# Student Class Example
# ------------------------------------------------------------------

class Student(models.Model):
    name = models.CharField(max_length=30)
    advisor = models.ForeignKey("Advisor", on_delete=models.CASCADE, related_name="advisor_students")
    student_residency = models.CharField(max_length=3, default="UNK")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def student_residency_status(self):
        if self.student_residency:
            if self.student_residency == "MA":
                return f"In-state student"
            elif self.student_residency != "MA" and len(self.student_residency) == 2:
                return f"Out-of-state student"
            else:
                return f"Foreign student"

class Course(models.Model):
    subject = models.CharField(max_length=15)
    students = models.ManyToManyField(Student, related_name="courses", blank=True)

    class Meta:
        ordering = ['subject']

    def __str__(self):
        return self.subject

class Advisor(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def student_with_longest_name(self):
        return max(self.advisor_students.all(), key=lambda student: len(student.name))


# -----------------------------------------------------------------
# Recursive m2m
# ------------------------------------------------------------------

class Employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=25)
    boss = models.BooleanField(default=False)
    supervisors = models.ManyToManyField("Employee", related_name="subordinates")

    class Meta:
        ordering = ["lname"]

    def __str__(self):
        return f"{self.lname}, {self.fname}, is a boss: {self.boss}"
    
    
    def is_boss_of_himself(self):
        return self.boss and self.supervisors.count() != 0
    
    def has_multiple_bosses(self):
        if self.supervisors.count() > 1:
            return True
        else: 
            return False
        
    def boss_has_subordinates(self):
        if self.boss and self.subordinates.count() != 0:
            return True
        else:
            return False
    
        
    

        
           

           
