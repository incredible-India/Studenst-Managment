
let assignmentNumber =  document.getElementById('id_assignNumber')

assignmentNumber.innerHTML = `

<option value="1">1</option>
<option value="2">2</option>
<option value="3">3</option>

`


let typeDate = document.getElementById('id_dueDate')

typeDate.setAttribute('type' , 'date')


let semester =  document.getElementsByClassName('semester')[0]
let sec = document.getElementsByClassName('sec')[0]


let mysection = document.getElementById('id_section')
let mysemester = document.getElementById('id_sem')

mysection.innerHTML = `
<option value="${sec.innerText}" selected>${sec.innerText}</option>

`

mysemester.innerHTML = `
<option value="${semester.innerText}" selected>${semester.innerText}</option>

`