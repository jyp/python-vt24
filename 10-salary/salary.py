# program income.py

salary = 12345
raise_percentage = 3
taxrate = 22
rent = 4000

print("salary before raise: ",salary)

for year in range(10):
    salary = salary * (1 + raise_percentage/100)
    print("year:",year)
    print("salary:",salary)

tax = salary * taxrate/100
net = salary - tax
remains = net - rent

print("remains: ",remains)

