import requests
import pdb; pdb.set_trace()

def add(a, b):
    return a+b

def divide(a, b):
    if b==0:
        raise ValueError("Cannot divide by zero!")
    else:
        return a / b

class Employee:

    Raise = 1.05

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    @property
    def get_email(self):
        return "{}{}@gmail.com".format(self.name, self.surname)
         

    def get_raise(self):
        return (self.Raise*self.salary)
    
    def get_schedule(self, month):
        response = requests.get(f'http://company.com/{self.name}/{month}')
        if response.ok:
            return response.text
        else:
            return "Bad response"
    

def str_to_bool(String):
    if String in ['yes', 'y', ' ']:
        return True
    else:
        return False

def write_value(value, path):
    with open(path, 'w') as f:
        f.write(value)
    f.close


if __name__ == "__main__":
    print("hi")