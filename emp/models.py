from django.db import models


class model_employee(models.Model):
    first_name = models.CharField(max_length=50,blank=False,null=False )
    last_name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.CharField(max_length=50)
    hire_date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=100)
    phone = models.IntegerField(default=91,blank=False,null=False)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (
            self.first_name, self.last_name, self.dept, self.role, self.bonus, self.location, self.salary,
            self.hire_date)
