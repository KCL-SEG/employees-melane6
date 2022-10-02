"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name ,contractType , commissionType):
        self.name = name
        self.contract=contractType
        self.commission = commissionType;
        self.monthly_salary = self.contract.get_pay()
        self.total_salary = 0
        self.set_pay()

    def set_pay(self):
        self.total_salary = self.contract.get_pay() + self.commission.get_pay()

    def get_pay(self):
        return self.total_salary

    def __str__(self):
        return f'{self.name} {self.contract}{self.commission} Their total pay is {self.total_salary}.'


class Contract:
    def __init__(self):
        self.monthly_salary = 0

    def get_pay(self):
        return self.monthly_salary

class MonthlyContract(Contract):
    def __init__(self, monthly_salary): #Constructor
        Contract.__init__(self) #subclass hence initializes superclass
        self.contractType = 'monthly'
        self.monthly_salary =  monthly_salary
    def __str__(self):
        return f'works on a monthly salary of {self.monthly_salary}'
class HourlyContract(Contract):
    def __init__(self, hourly_wage , hours): #Constructor
        Contract.__init__(self) #subclass hence initializes superclass
        self.contractType = 'hourly'
        self.hourly_wage = hourly_wage
        self.hours = hours
        self.set_pay()

    def set_pay(self):
        self.monthly_salary = self.hourly_wage * self.hours

    def __str__(self):
        return f'works on a contract of {self.hours} hours at {self.hourly_wage}/hour'
class Commission:
    def __init__(self):
        self.commissionType = 'none'
        self.commission_pay = 0

    def get_pay(self):
        return self.commission_pay

    def __str__(self):
        return '. '

class BonusCommission(Commission):
    def __init__(self, bonus):
        Commission.__init__(self)
        self.commissionType = 'bonus'
        self.commission_pay = bonus

    def __str__(self):
        return f' and receives a bonus commission of {self.commission_pay}. '

class ContractCommission(Commission):
    def __init__(self, num_contracts, commission):
        Commission.__init__(self)
        self.commissionType = 'contract'
        self.num_contracts = num_contracts
        self.commission = commission
        self.set_pay()

    def set_pay(self):
        self.commission_pay = self.num_contracts * self.commission

    def __str__(self):
        return f' and receives a commission for {self.num_contracts} contract(s) at {self.commission}/contract. '


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie' , MonthlyContract(4000), Commission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25,100), Commission())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyContract(3000), ContractCommission(4,200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25,150) , ContractCommission(3,220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30,120), BonusCommission(600))
