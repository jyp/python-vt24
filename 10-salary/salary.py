# program income.py


def compute_salary(salary, raise_percentage, taxrate, rent):
   # print("salary before raise: ",salary)

   for year in range(10):
       salary = salary * (1 + raise_percentage/100)
       # print("year:",year)
       # print("salary:",salary)

   tax = salary * taxrate/100
   net = salary - tax
   remains = net - rent
   return remains
   # print("remains: ",remains)

# compute_salary(salary = 12345, taxrate = 22, raise_percentage = 3, rent = 4000)
# compute_salary(12345,3,22,4000)
print(compute_salary(12345,4,22,4000))
