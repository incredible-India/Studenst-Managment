from .models import Student
def checkStudentFrom(data):
    if data['fname'] == '' or len(data['fname']) < 3 :
        return [0,'First Name shoud be greater than 3 characters']
    elif data['lname'] == '' or len(data['lname']) < 3 :
        return [0,'Last Name shoud be greater than 3 characters']
    elif data['mobile'] == '' or len(str(data['mobile'])) < 10 :
        return [0,'Incorrect Mobile Number']
    elif '@gmail.com' not in data['email']:
        return [0,'Invalid Email']
    elif '1SP' not in data['usn'].upper():
        return [0,'Invalid USN Number']
    elif len(data['usn']) != 10 :
        return [0,'Invalid Usn Number']
    elif (data['sem'] == '1') and (data['cycle'] == '1'):
      
        return [0,'For 1st sem or 2nd sem cycle cannot be None']
    elif data['sem'] == '2' and (data['cycle'] == '1'):
        return [0,'For 1st sem or 2nd sem cycle cannot be None']

    elif( int(data['sem'] ) > 3 ) and data['cycle'] != '1':
    
        return [0,'Please select None cycle for above 1st and 2nd sem']
    

    
    elif data['password'] == '12345' or len(data['password']) < 5:
        return [0,'Password Should be contain at least 6 characters'] 
    

    else :

        studentUSN = Student.objects.filter(usn = data['usn'])

        if len(studentUSN) !=0:
            return [0,'Usn Already Exists']
        else:
            return [1,data]

        

