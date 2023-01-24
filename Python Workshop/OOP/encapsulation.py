# Python has no concept of private variables
# No way of hiding and securing variables so modules and code can't change

# Encapsulation - Only trusted code should have limited access to functionality and variables
# - grouping together all functions and methods of getting and setting data

# Leading underscore suggests to devs that this is a private variable


class bankAccount():
    
    _pin = 1234
    _money = 500
    
    # getter
    def displayMoney(self,pin):
       if(pin == self._pin):
           return self._money
       else:
           return "Invalid Pin"
       
    def getMoney(self):
        return self._money
    
    # setter
    def depositMoney(self, pin, money):
        if(pin == self._pin):
            self._money += money
            return f"Total money : {self._money}"
        else:
            return "Invalid pin"
    
acc1 = bankAccount()
print(acc1._pin)

print(acc1.displayMoney(9999))
print(acc1.displayMoney(1234))
print(acc1.depositMoney(1234,750))
print(acc1.depositMoney(1234,750))