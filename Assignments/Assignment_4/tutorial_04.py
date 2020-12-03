import csv
import pandas as pd
import os
import math


grade_file= "acad_res_stud_grades.csv"
records=pd.read_csv(grade_file)
print(records.columns)

Roll_numbers=list();

with open('acad_res_stud_grades.csv','r') as file:
    reader=csv.reader(file)
    print(reader)
    for row in reader:
        grade_file= 'grades/' + str(row[1]) + "_individual.csv"
        if(os.path.isfile(grade_file) == False):
            Roll_numbers.append(row[1])
            with open(grade_file, 'a') as file2:
                writer = csv.writer(file2)
                writer.writerow(['Roll', 'semester', 'Year', 'sub_code', 'total_credits',
       'credit_obtained', 'sub_type'])
        try:
            with open(grade_file, 'a') as file2:
                writer = csv.writer(file2)
                writer.writerow([row[1], row[2], row[3], row[4], row[5], row[6], row[8]])
        except:
            pass


for roll in Roll_numbers:
    total_credits=0
    credits_obtained=0
    grade_file = 'grades/' + str(roll) + "_individual.csv"
    datafile=pd.read_csv(grade_file)
    total_semester=datafile['semester'].unique().max()
    semesterwise_credit=0
    CPI=0
    print(
        'semester wise score for roll no: ', roll, 'and total semester are',total_semester
    )

    def grade_to_score(x):
        if x == 'AA':
            return 10
        if x == 'AB':
            return 9
        if x == 'BB':
            return 8
        if x == 'BC':
            return 7
        if x == 'CC':
            return 6
        if x == 'CD':
            return 5
        if x == 'DD':
            return 4
        else:
            return 0


    Semester = list()
    Semester_Credits = list()
    Semester_Credits_Cleared = list()
    SPI = list()
    Total_Credits = list()
    Total_Credits_Cleared = list()
    CPI_Obtained = list()
    temp = 0

    for sem in range(1,total_semester+1):
        Semester.append(sem)
        semester_particular=datafile[(datafile['semester'] == sem)]
        credit_array=list(semester_particular['credit_obtained'].apply(grade_to_score))
        particular_semester_total_credit=list(semester_particular['total_credits'])

        temp1 = 0
        for x in range(0,len(credit_array)):
            temp1 += (credit_array[x] * particular_semester_total_credit[x])
        temp= temp + temp1
        total_credits = total_credits + semester_particular['total_credits'].sum()
        Semester_Credits.append(semester_particular['total_credits'].sum())
        Semester_Credits_Cleared.append(semester_particular['total_credits'].sum())
        SPI.append(round(temp1 / semester_particular['total_credits'].sum(), 2))
        Total_Credits.append(total_credits)
        Total_Credits_Cleared.append(total_credits)
        CPI_Obtained.append(round(temp / total_credits, 2))
    dict={'Semester':Semester,'Semester Credits':Semester_Credits,'Semester_Credits_Cleared':Semester_Credits_Cleared,'SPI':SPI,
          'Total Credits':Total_Credits,'Total Credits Cleared':Total_Credits_Cleared,'CPI':CPI_Obtained}
    df=pd.DataFrame(dict)
    file_name= "grades/" + str(roll) + "_overall.csv"
    df.to_csv(file_name)

