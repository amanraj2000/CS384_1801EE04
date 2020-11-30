import pandas as pd
import csv
import re
import math
import os
import itertools


# Function for seperating students branch-wise
def branch_seperator(student_roll_list , student_name , student_id, total_branch):
    for (i,j,k) in zip(student_roll_list, student_name, student_id):
        roll = re.compile(r'[a-zA-Z]+')
        branch = re.findall(roll,i)
        total_branch.append(branch[0])
        branch_name = branch[0]
        branch_file = branch_name + ".csv"
        if(os.path.isfile(branch_file) == False):
            with open(branch_file, 'a', newline = "" )as temp_branch_file:
                writer = csv.writer(temp_branch_file)
                writer.writerow(['Roll','Name','E-mail id'])
                writer.writerow([i, j, k])
        else:
            with open(branch_file, 'a', newline = "" )as temp_branch_file:
                writer = csv.writer(temp_branch_file)
                writer.writerow([i, j, k])




# Function for seperating students Group-wise
def group_allocation(total_branch, number_of_groups):
    total_branch = list(dict.fromkeys(total_branch))
    branchwise_left_students = list()
    print(number_of_groups)
    for i in total_branch:
       file_name = i + ".csv"
       temp_df = pd.read_csv(file_name)
       temp_df.drop_duplicates(subset = "Roll", keep = False, inplace = True)
       temp_size = math.floor(len(temp_df)/(number_of_groups))
       iterate = 0
       branchwise_left_students.append(len(temp_df) - (number_of_groups)*temp_size )
       for j in range(0, number_of_groups):
           for k in range(0, temp_size):
               group_number_padd = str(j+1)
               group_number_padd = group_number_padd.zfill(2)
               temp_group_filename = "G " + group_number_padd + ".csv"
               if(os.path.isfile(temp_group_filename) == False):
                   with open(temp_group_filename, 'a', newline = "" )as group_filename:
                       writer = csv.writer(group_filename)
                       writer.writerow(['Roll','Name','Branch','E-mail id'])
               with open(temp_group_filename, 'a', newline = "" )as group_filename:
                   writer = csv.writer(group_filename)
                   temp_name =  temp_df.loc[iterate, "Name"]
                   temp_roll =  temp_df.loc[iterate, "Roll"]
                   temp_Email = temp_df.loc[iterate, "E-mail id"]
                   writer.writerow([temp_roll, temp_name, i, temp_Email])
               iterate += 1
               cnt = 0
    for (i, jp) in zip(total_branch, branchwise_left_students):
        temp_filename = i + ".csv"
        left_df = pd.read_csv(temp_filename)
        iter = len(left_df)-jp
        for k in range(0, jp):
            group_number_left = str((cnt%12)+1)
            group_number_left = group_number_left.zfill(2)
            group_file = "G " + group_number_left + ".csv"
            with open(group_file, 'a', newline = "" )as group:
                writer = csv.writer(group)
                temp_names = left_df.loc[iter, "Name"]
                temp_rolls = left_df.loc[iter, "Roll"]
                temp_Emails = left_df.loc[iter, "E-mail id"]
                writer.writerow([temp_rolls, temp_names, i, temp_Emails])
            iter += 1
            cnt += 1







filename = "Btech_2020_master_data.csv"
df = pd.read_csv(filename)
student_roll_list = list()  # Roll number list of students
student_name = list()       # Name List of Students
student_id = list()         #  Students E-mail id
total_branch = list()      # Branch name list

number_of_groups = 12      # Number of groups in which students are divided

with open(filename , 'r')as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        student_roll_list.append(row[0])
        student_name.append(row[1])
        student_id.append(row[2])

# Function Call for seperating student branch wise
branch_seperator(student_roll_list , student_name , student_id, total_branch)

# Function call for allocating groups to each students
group_allocation(total_branch, number_of_groups)

# Removing any duplicates from the branch files and sorting them according to Roll Numbers
for i in total_branch:
    branch_file = i + ".csv"
    branch_df = pd.read_csv(branch_file)
    branch_df.drop_duplicates(subset = "Roll", keep = False, inplace = True)
    branch_df.sort_values("Roll", inplace = True)

# Removing any duplicates from Group Files and sorting them according to their Roll Numbers
for i in range(0,number_of_groups):
    group_numb = str(i+1)
    group_numb = group_numb.zfill(2)
    group_file = "G " + group_numb +".csv"
    group_df = pd.read_csv(group_file)
    group_df.drop_duplicates(subset = "Roll", keep =False, inplace = True)
    group_df.sort_values("Roll", inplace = True)


print(" Completed !! ")