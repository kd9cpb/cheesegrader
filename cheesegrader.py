#/usr/bin/env python3
# based off https://www.geeksforgeeks.org/program-create-grade-calculator-in-python/
# and https://github.com/tomulent/learning-python/blob/master/Grade%20Book%20Challenge.py
# and https://gist.github.com/Temmyhlee/5a795a5e9d9eedc47ead87f9f62e5108
# and help from https://stackoverflow.com/questions/23309657/python-total-sum-of-a-list-of-numbers-with-the-for-loop/23309832 too

import yaml

# pull in students.yml
grades = "students.yml"
with open(grades) as f:
    students = yaml.load(f, Loader=yaml.FullLoader)

# pull in weights.yml
weights = "weights.yml"
with open(weights) as f:
    weight = yaml.load(f, Loader=yaml.FullLoader)

# pull in lettergrades.yml
lettergrades = "lettergrades.yml"
with open(lettergrades) as f:
    letter = yaml.load(f, Loader=yaml.FullLoader)

# Function calculates average  
def get_average(marks): 
    total_sum = sum(marks) 
    total_sum = float(total_sum) 
    return total_sum / len(marks) 
  
# Function calculates total average using students.yml and weights.yml
def calculate_total_average(students): 
    newgrade = 0
    for k, v in weight.items():
        k = get_average(students[k])
        newgrade = k * v + newgrade
    return newgrade
  
# Calculate letter grade of each student using lettergrades.yml
def assign_letter_grade(score): 
    if score >= (letter["A"]): return "A"
    elif score >= (letter["B"]): return "B"
    elif score >= (letter["C"]): return "C"
    elif score >= (letter["D"]): return "D"
    else : return "E"
  
# Function to calculate the total 
# average marks of the whole class 
def class_average_is(student_list): 
    result_list = [] 
  
    for student in student_list: 
        stud_avg = calculate_total_average(student) 
        result_list.append(stud_avg) 
        return get_average(result_list) 
  
# Iterate through the students list 
# and calculate their respective 
# average marks and letter grade 
for i in students : 
    print(i["name"]) 
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=") 
    print("Average marks of %s is : %s " %(i["name"], 
                         calculate_total_average(i))) 
                           
    print("Letter Grade of %s is : %s" %(i["name"], 
    assign_letter_grade(calculate_total_average(i)))) 
      
    print() 
  
  
# Calculate the average of whole class 
class_av = class_average_is(students) 
  
print( "Class Average is %s" %(class_av)) 
print("Letter Grade of the class is %s " 
        %(assign_letter_grade(class_av)))