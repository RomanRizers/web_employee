from flask import Flask, request, render_template, redirect, url_for
from .io.web_io import WebIO
from .models.manager import Manager
from .models.cashier import Cashier
from .models.picker import Picker
from .models.director import Director
from .models.employee import Employee
from .storage.pickle_storage import PickleStorage

app = Flask(__name__)
web_io = WebIO()
storage = PickleStorage()


@app.route('/')
def index():
    employees = storage.get_items()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        web_io = WebIO()
        name = web_io.input('name')
        age_str = web_io.input('age')
        experience_str = web_io.input('experience')
        employee_type = web_io.input('employee_type')

        try:
            age = int(age_str)
            experience = int(experience_str)
        except (ValueError, TypeError):
            return render_template('add_employee.html', error="Пожалуйста, введите корректные данные.")
        
        employee = Employee(name=name, age=age, experience=experience)
        
        if employee_type == 'manager':
            department = web_io.input('department')
            employee = Manager(name=name, age=age, experience=experience, department=department)
            

        elif employee_type == 'cashier':
            shift = web_io.input('shift')
            employee = Cashier(name=name, age=age, experience=experience, shift=shift)

        elif employee_type == 'picker':
            zone = web_io.input('zone')
            employee = Picker(name=name, age=age, experience=experience, zone=zone)

        elif employee_type == 'director':
            employee = Director(name=name, age=age, experience=experience)

        storage.add(employee)
        return redirect(url_for('index'))

    return render_template('add_employee.html')

@app.route('/delete/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    print(f"Запрос на удаление сотрудника с ID {employee_id}")
    storage.delete_item(employee_id)
    return redirect(url_for('index'))

@app.route('/delete_all', methods=['POST'])
def delete_all_employees():
    storage.delete() 
    return redirect(url_for('index'))

@app.route('/edit/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    employee = storage.get_item(employee_id)
    
    if request.method == 'POST':
        name = request.form.get('name')
        employee_type = request.form.get('employee_type')
        try:
            age = int(request.form.get('age'))
            experience = int(request.form.get('experience'))
        except (ValueError, TypeError):
            return render_template('edit_employee.html', employee=employee, error="Пожалуйста, введите корректные данные.")

        employee.name = name
        employee.age = age
        employee.experience = experience

        if employee_type == 'manager':
            new_employee = Manager(id=employee_id, name=name, age=age, experience=experience,
                                           department=request.form.get('department'))
        elif employee_type == 'cashier':
            new_employee = Cashier(id=employee_id, name=name, age=age, experience=experience,
                                           shift=request.form.get('shift'))
        elif employee_type == 'picker':
            new_employee = Picker(id=employee_id, name=name, age=age, experience=experience,
                                          zone=request.form.get('zone'))
        elif employee_type == 'director':
            new_employee = Director(id=employee_id, name=name, age=age, experience=experience)
        else:
            return render_template('edit_employee.html', employee=employee, error="Неизвестный тип сотрудника.")

        storage.edit(employee_id, new_employee)
        return redirect(url_for('index'))

    return render_template('edit_employee.html', employee=employee)


@app.route('/save', methods=['POST'])
def save_employees():
    storage.save()
    return redirect(url_for('index'))
    

@app.route('/load', methods=['POST'])
def load_employees():
    storage.load()
    employees = storage.get_items()
    return render_template('index.html', employees=employees)


if __name__ == '__main__':
    app.run(debug=True)