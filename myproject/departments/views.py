from django.shortcuts import get_object_or_404, redirect, render

from .models import Department, Employee


def department_list(request):
    """Функция отвечают за отображения списка подразделения."""
    departments = Department.objects.all()
    return render(request, 'departments/department_list.html', {'departments': departments})


def department_detail(request, department_id):
    """Функция отвечают за отображения списка подразделения и деталей конкретного подразделения."""
    department = get_object_or_404(Department, id=department_id)
    return render(request, 'departments/department_detail.html', {'department': department})


def employee_create(request, department_id):
    """Функция, отвечающая за добавление сотрудников."""
    department = get_object_or_404(Department, id=department_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        position = request.POST.get('position')
        hire_date = request.POST.get('hire_date')
        salary = request.POST.get('salary')
        department_id = department_id

        employee = Employee(name=name, position=position, hire_date=hire_date, salary=salary, department_id=department_id)
        employee.save()
        return redirect('department_detail', department_id=department.id)

    return render(request, 'departments/employee_create.html', {'department': department})


def employee_update(request, employee_id):
    """Функция, отвечающая за изменение сотрудников."""
    employee = get_object_or_404(Employee, id=employee_id)
    department = employee.department

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.position = request.POST.get('position')
        employee.hire_date = request.POST.get('hire_date')
        employee.salary = request.POST.get('salary')
        employee.save()
        return redirect('department_detail', department_id=department.id)

    return render(request, 'departments/employee_update.html', {'employee': employee})


def employee_delete(request, employee_id):
    """Функция, отвечающая за удаление сотрудников."""
    employee = get_object_or_404(Employee, id=employee_id)
    department = employee.department

    if request.method == 'POST':
        employee.delete()
        return redirect('department_detail', department_id=department.id)

    return render(request, 'departments/employee_delete.html', {'employee': employee})
