
fifthSem = ['ADP : Application Development using Python'
,'ME : Management ,Entrepreneurship for IT Industry',
'CNS : Computer Networks And Security',
'DBMS : Database Management System',
'ATC : Autometa Theory And Computability',
'UNIX : UNIX Programming',
'CNS LAB',
'DBMS LAB',
'EVS : Enviroment Studies' 
]


let sem =  document.getElementsByClassName('sem')[0];

sem.onchange = (event)=>{

    let subject =  new Array();
    let semester = sem.value;

    if(semester == 1)
    {



    }else if(semester ==2)
    {

    }else if(semester == 3 ){

    }else if(semester == 4)
    {

    }else if(semester == 5)
    {
        subject = fifthSem

    }else if(semester == 6)
    {

    }else if(semester == 7)
    {

    }else if(semester == 8)
    {

    }else
    {
        subject = ['No subject Available For This Semester']
    }
    document.getElementsByClassName('subjects')[0].innerHTML = ''
    for (i in subject)
    {
        document.getElementsByClassName('subjects')[0].innerHTML  += `
        
        <option value="${subject[i]}">${subject[i]}</option>
        
        
        `
    }

}