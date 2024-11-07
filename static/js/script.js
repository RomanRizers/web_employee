function updateUniqueAttributeField() {
    const employeeType = document.querySelector('select[name="employee_type"]').value;
    const managerField = document.getElementById('managerField');
    const cashierField = document.getElementById('cashierField');
    const pickerField = document.getElementById('pickerField');

    // Скрываем все поля
    managerField.style.display = 'none';
    cashierField.style.display = 'none';
    pickerField.style.display = 'none';

    // Показываем нужное поле в зависимости от выбранного типа сотрудника
    if (employeeType === 'manager') {
        managerField.style.display = 'block';
    } else if (employeeType === 'cashier') {
        cashierField.style.display = 'block';
    } else if (employeeType === 'picker') {
        pickerField.style.display = 'block';
    }
}

// Инициализируем видимость полей при загрузке страницы
document.addEventListener('DOMContentLoaded', updateUniqueAttributeField);
