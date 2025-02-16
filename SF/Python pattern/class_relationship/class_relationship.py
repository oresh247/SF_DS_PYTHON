from __future__ import annotations
from enum import Enum

class Person:
    def __init__(self, name: str) -> None:
        self.name = name
    def __str__(self) -> str:
        return f' {self.name} is alive!'

class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'
    
class Man(Person):
    gender = Gender.MALE # association
    

class Woman(Person):
    gender = Gender.FEMALE # association


class Employee:
    def __init__(self, person: Person, company: Company, position: str) -> None:
        self.company = company # aggregation
        self.person = person # aggregation
        self.position = position
        
    def __str__(self) -> str:
        return f' -> {self.person.name} is "{self.position}"'
    

class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees = [] # composition
        
    def __str__(self) -> str:
        employees_count = len(self.employees)
        if employees_count > 0:
            return f'Company "{self.name}" has {employees_count} employees:'
        else:
            return f'Company with {employees_count} employees is out of busines :('
        
    def hire_emloyee(self, person: Person, position: str):
        employee = Employee(person=person, company=self, position=position)
        self.employees.append(employee)
        
    def list_employees(self):
        print(self)
        for employee in self.employees:
            print(employee)
    
    def liquidate(self):
        print(f'Company "{self.name}" is starting to liquidate ...')
        self.employees = []
        print(self)
        
        
if __name__ == '__main__':
    john = Man('John')
    jane = Woman('Jane')
    bill = Man('Bill')
    company = Company('CocaCola')
    company.hire_emloyee(john, 'manager')
    company.hire_emloyee(jane, 'accountant')
    company.hire_emloyee(bill, 'assistent')
    company.list_employees()
    company.liquidate()
    del company
    print(john, jane, bill, sep='\n')