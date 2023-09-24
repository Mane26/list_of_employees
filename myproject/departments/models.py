from django.db import models


class Department(models.Model):
    """Department - это модель для отделов, она имеет поля name (название отдела) и parent (ссылка на родительский отдел)."""
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Employee - это модель сотрудника, она содержит ссылку на отдел (department), позицию (position), дату начала работы (hire_date) и зарплату (salary)."""
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.position} ({self.salary})"
