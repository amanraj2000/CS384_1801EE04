<<<<<<< HEAD
import csv
import re
import  os
import  operator
import shutil
File_students=os.getcwd()+"/analytics"
def std(x):
    if x == '01':
        return 'B.tech'
    elif x == '11':
        return "M.tech"
    elif x == '12':
        return "Msc"
    elif x == '21':
        return "Phd"
=======


def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    pass

>>>>>>> 1a7ce81470ad38f1c9e4586a53478b0c6c53b9d3

def course():
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
                roll = re.split('[A-Z]+', row[0])
                branch = (re.split('[0-9]+', row[0]))
                try:
                   var =str(std( roll[0][-2:len(roll[0])]))
                   ri=roll[0][0]+roll[0][1]
                   try:

                       os.makedirs(File_students + "/course/" + var)
                       f = open(
                        
                        File_students + "/course/" + var + "/" + ri + "" + str.lower(branch[1]) + "" + var + ".csv",
                           'a')
                       write = csv.writer(f)
                       write.writerow(['id','full_name','country','email','gender','dob','blood_group','state'])
                   except:
                       pass
                   
                   f=open(File_students+"/course/"+var+"/"+ri+""+str.lower(branch[1])+""+var+".csv",'a')
                   write=csv.writer(f)
                   write.writerow(row)

                except:
                    f=open(File_students+"/course/"+"misc.csv",'a')
                    write=csv.writer(f)
                    write.writerow(row)

def country():
    c=File_students+"/country"
    try:
        os.makedirs(c)
    except:
        pass
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            country = str.lower(row[2])
            try:
                f=open(File_students+"/"+"country/"+country+".csv",'a')
                writer=csv.writer(f)
                writer.writerow(row)
            except:
                pass


def email_domain_extract():
    try:
     os.makedirs(File_students+"/email_domain")
    except:
     pass
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:

            try:
                x = (row[3].split('@'))

                f=open(File_students+"/email_domain/"+(x[1].split('.')[0])+".csv",'a')

                writer=csv.writer(f)
                writer.writerow(row)
            except:
                pass

def gender():
    try:
        os.makedirs(File_students+'/gender')
    except:
        pass
    with open('studentinfo_cs384.csv','r') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            f=open(File_students+'/gender/'+row[-4]+".csv",'a')
            writer=csv.writer(f)
            writer.writerow(row)




def dob():
    filename=File_students+'/dob'
    try:
        os.makedirs(filename)
    except:
        pass
    f1=open(filename+'/bday_1995_1999.csv','a')
    f2=open(filename+'/bday_2000_2004.csv','a')
    f3=open(filename + '/bday_2005_2009.csv','a')
    f4=open(filename + '/bday_2010_2014.csv','a')
    f5=open(filename + '/bday_2015_21995020.csv','a')
    with open('studentinfo_cs384.csv','r') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            x=row[-3]
            y=x.split('-')[-1]
            if y>='2015':
                reader=csv.writer(f1)
                reader.writerow(row)
            elif y>='2010':
                reader = csv.writer(f2)
                reader.writerow(row)
            elif y>='2005':
                reader = csv.writer(f3)
                reader.writerow(row)
            elif y>='2000':
                reader = csv.writer(f4)
                reader.writerow(row)
            elif y>='1995':
                reader = csv.writer(f5)
                reader.writerow(row)


def state():
    try:
        os.makedirs(File_students + '/state')
    except:
        pass
    with open('studentinfo_cs384.csv', 'r') as file:
       reader = csv.reader(file)
       next(reader)
       for row in reader:
           states=(row[-1])
           t=File_students+'/state/'+states+".csv"
           f=open(t,'a')
           writer=csv.writer(f)
           writer.writerow(row)


def blood_group():
    try:
        os.makedirs(File_students + '/blood_group')
    except:
        pass
    with open('studentinfo_cs384.csv', 'r') as file:

        reader = csv.reader(file)
        for row in reader:
            blood=(row[-2])
            r=File_students+"/blood_group/"+str.lower(blood)+'.csv'
            f=open(r,'a')
            writer=csv.writer(f)
            writer.writerow(row)


def new_file():
    with open('studentinfo_cs384_names_split.csv','w') as file:
        writer=csv.writer(file)
        writer.writerow(['id','first_name','last_name','country','email','gender','dob','blood_group','state'])
        with open('studentinfo_cs384.csv','r') as file2:
            reader=csv.reader(file2)
            next(reader)
            for read in reader:
                id=read[0]
                newname=read[1].split(' ')
                country=read[2]
                email=read[3]
                gender=read[4]
                dob=read[5]
                blood_group=read[6]
                state=read[7]
                writer.writerow([id,newname[0],newname[-1],country,email,gender,dob,blood_group,state])



def new_file_sort():
    data = csv.reader(open('studentinfo_cs384_names_split.csv','r'))
    next(data)
    writer=csv.writer(open('studentinfo_cs384_names_split_sorted_first_name.csv','w'))
    writer.writerow(['id','first_name','last_name','country','email','gender','dob','blood_group','state'])
    sortedlist = sorted(data, key=operator.itemgetter(1))
    for x in sortedlist:
        writer.writerow(x)


# Function to delete folder.
#def del_create_analytics_folder():
 #   shutil.rmtree('analytics')