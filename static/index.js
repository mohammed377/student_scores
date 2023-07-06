const searchInput = document.getElementById('student-search') 
            
searchInput.addEventListener('change', search)

function search() {
  const searchTerm = searchInput.value
  
  const url = ''  
  const data = {search: searchTerm}  
  
  fetch(url, {
    method: 'GET',  
    headers: {      
      'Content-Type': 'application/json'
    },  
    body: JSON.stringify(data)   
  })
  .then(response => response.json())   
  .then(data => {
    let html = ''
    
    if (data.grades.length > 0) {
      // Students found, output results  
      data.grades.forEach(grade => {
        html += `
    <tr>   
      <td>${grade.total_grade}</td>
      <td>${grade.name}</td>  
      <td>${grade.student_id}</td>
    </tr>  
  `
      })    
    } else {  
      // No students found, show message      
      html = '<tr><td colspan="3">No students found.</td></tr>' 
    }
      
    document.getElementById('student-table').innerHTML = html  
  })  
}