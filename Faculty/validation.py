
def validateTeacherForm(data):
    
    for i in range(0,10):
        if str(i) in data['fname']:
                 return [0,'First name  connot contains numbers or special characters']
    for i in range(0,10):
        if str(i) in data['lname']:
                 return [0,'Last name  connot contains numbers or special characters']

    if data['fname'] == '' or len(data['fname']) <= 2 :

        return [0,'First name  connot be empty or less then 2 characters']
    elif data['lname'] == '' or len(data['lname']) <= 2 :
        return [0,'Last name  connot be empty or less then 2 characters']
    elif  '@gmail.com' not in data['email']: 
        return [0,'Ivalid Email']
    elif len(data['essn']) <=3:
        return [0,'Invalid essn number']    
    elif len(data['password']) <=5 or data['password'] == '12345':
        return [0,'Password should contain at least one special character']
    elif data['degree'] == '' or len(data['degree']) <= 2 :
        return [0,'Invalid given degree']
    else :
        return [1]
