from django.db import models
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