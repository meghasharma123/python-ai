print("Hello world")

revenue = 50
expenses = 10

# int
profit = revenue - expenses
print(profit)

# float
margin = profit * 100 / revenue
print(margin)

# list
revenues = [50,80,60]
expenses = [30,50,40]

margins = []

print(revenues[-1]) # prinitng from backward
print(revenues[1:3]) # prinitng a particular index
print(len(revenues))

for i in range(len(revenues)):
    p = revenues[i] - expenses[i]
    m = p * 100 / revenues[i]
    margins.append(round(m,2))

# marigns: [40.0, 37.5, 33.33]

# Dictionary

financials = [
    {"rev": 50, "exp": 30},
    {"rev": 80, "exp": 50},
    {"rev": 60, "exp": 40},
]

for fin in financials:
    pr = fin["rev"] - fin["exp"]
    fin['margin'] = round(pr * 100 / fin['rev'],2)

# financials: [{'rev': 50, 'exp': 30, 'margin': 40.0}, {'rev': 80, 'exp': 50, 'margin': 37.5}, {'rev': 60, 'exp': 40, 'margin': 33.33}]

financialsQuater = {
    "Q1": {"rev": 50, "exp": 30},
    "Q2":{"rev": 80, "exp": 50},
    "Q3":{"rev": 60, "exp": 40},
}

for quater, data in financialsQuater.items():
    m = (data['rev'] - data['exp']) * 100 / data['rev']

# tuples:

user_profile = ("Alice", 28, "Engineer", True)
numbers = (1, 2, 3, 2, 4)

print(numbers.count(2))  # Output: 2
print(numbers.index(3))  # Output: 2
print(len(numbers))      # output: 5

# Exercise

students = {
    "Aarav":   [85, 90, 78],
    "Priya":   [72, 68, 75],
    "Rohan":   [45, 52, 48],
    "Sneha":   [95, 92, 98],
    "Manish":  [60, 65, 70],
}

topAvg = 0
topStudent = ''
totalSum = 0
totalStudent = len(students.keys())

print("====== Students Avg =========")

for k, d in students.items():
    avg = (d[0] + d[1] + d[2]) / 3

    totalSum += avg
    
    if(avg > topAvg):
        topAvg = avg
        topStudent = k

    if avg >= 80:
        print(f"{k} : {avg:.2f} - Topper")
    elif avg>= 60 and avg <=79:
        print(f"{k} : {avg:.2f} - Pass") 
    else:
        print(f"{k} : {avg:.2f} - Needs improvement")

print("====== Class Topper =========")
print(f"{topStudent} with average {topAvg}")

print("====== Class Average =========")
print(round(totalSum/totalStudent,2))
