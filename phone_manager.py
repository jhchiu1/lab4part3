# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone:

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None

    def assign(self, employee_id):
        self.employee_id = employee_id

    def is_assigned(self):
        return self.employee_id is not None

    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)


class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)


class PhoneAssignments:

    def __init__(self):
        self.phones = []
        self.employees = []

    def add_employee(self, employee):
        for e in self.employees:
            # Throw exception if two employees with same ID are added
            if e.id == employee.id:
                raise PhoneError
        self.employees.append(employee)

    def add_phone(self, phone):
        for p in self.phones:
            # Throw exception if two phones with same ID are added
            if p.id == phone.id:
                raise PhoneError
        self.phones.append(phone)

    # Find phone in phones list
    def assign(self, phone_id, employee):
        for phone in self.phones:
            if phone.id == phone_id:
                # If employee already has this phone, don't make any changes. This should NOT throw an exception.
                if phone.employee_id == employee.id:
                    return
                # If this phone is already assigned to an employee, do not change list, throw exception
                elif phone.employee_id is not None:
                    raise PhoneError
            # If employee already has a phone, do not change list, and throw exception
            if phone.employee_id == employee.id:
                raise PhoneError
            if phone.id == phone_id:
                phone.assign(employee.id)
                return

    # Find phone in list, set employee_id to None
    def un_assign(self, phone_id):
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)

    # Find phone for employee in phones list
    def phone_info(self, employee):
        if employee not in self.employees:
            raise PhoneError
        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone

        return None

class PhoneError(Exception):
    pass