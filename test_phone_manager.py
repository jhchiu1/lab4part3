import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order. (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)

    # add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
    def test_create_and_add_phone_with_duplicate_id(self):
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)

    # add some employees and verify they are present in the PhoneAssignments.employees list
    def test_create_and_add_new_employee(self):
        testEmployee1 = Employee(1, "Julie")
        testEmployee2 = Employee(2, "Bob")

        testEmployees = [testEmployee1, testEmployee2]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)

        self.assertCountEqual(testEmployees, testAssignmentMgr.employees)

    def test_create_and_add_employee_with_duplicate_id(self):
        testEmployee1 = Employee(1, "Julie")
        testEmployee2 = Employee(1, "Bob")

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testEmployee2)

    def test_assign_phone_to_employee(self):
        testPhone = Phone(1, "iPhone", "i7")
        testEmployee = Employee(1, "Julie")

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.assign(testPhone.id, testEmployee)
        self.assertEqual(testPhone.employee_id, testEmployee.id)

    # If a phone is already assigned to an employee, it is an error to assign it to a different employee.
    # A PhoneError should be raised.
    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        testPhone = Phone(1, "iPhone", "i7")
        testEmployee1 = Employee(1, "Julie")
        testEmployee2 = Employee(2, "Bob")

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.assign(1, testEmployee1)

        self.assertRaises(PhoneError, testAssignmentMgr.assign(1, testEmployee2))

    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        testEmployee = Employee(1, "Julie")
        testPhone1 = Phone(1, "iPhone", "i7")
        testPhone1 = Phone(2, "iPhone", "i7")

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.assign(1, testEmployee)

        self.assertRaises(PhoneError, testAssignmentMgr.assign(2, testEmployee))

    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # The method should not make any changes but NOT raise a PhoneError if a phone is assigned to the same user it is currently assigned to.
        testEmployee = Employee(1, "Julie")
        testPhone = Phone(1, "iPhone", "i7")

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.assign(1, testEmployee)

        try:
            testAssignmentMgr.assign(1, testEmployee)
        except PhoneError:
            self.fail()

    # Assign a phone, unassign the phone, verify the employee_id is None
    def test_un_assign_phone(self):
        testPhone = Phone(1, "iPhone", "i7")
        testEmployee = Employee(1, "Julie")

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.assign(1, testEmployee)
        testAssignmentMgr.un_assign(1)

        self.assertEqual(testPhone.employee_id, None)

    # Verify correct phone info is returned
    # Check that the method returns None if the employee does not have a phone
    # Check that the method raises an PhoneError if the employee does not exist
    def test_get_phone_info_for_employee(self):

        testPhone1 = Phone(1, "iPhone", "i7")
        testPhone2 = Phone(2, "Android", "Galaxy")
        testPhone3 = Phone(3, "Windows", "3")

        testEmployee1 = Employee(1, "Julie")
        testEmployee2 = Employee(2, "Bob")
        testEmployee3 = Employee(3, "Chris")

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.employees.append(testEmployee1)
        testAssignmentMgr.employees.append(testEmployee2)
        testAssignmentMgr.phones.append(testPhone1)
        testAssignmentMgr.phones.append(testPhone2)
        testAssignmentMgr.phones.append(testPhone3)
        testAssignmentMgr.assign(2, testEmployee1)

        self.assertEqual(testAssignmentMgr.phone_info(testEmployee1), testPhone2)
        self.assertEqual(testAssignmentMgr.phone_info(testEmployee2), None)
        self.assertRaises(PhoneError, testAssignmentMgr.phone_info, testEmployee3)