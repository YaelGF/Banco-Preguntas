

function myFunction() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }       
    }
}
getExamInfo();
function getExamInfo(){
    token = sessionStorage.getItem("token");
    console.log(token);
    var request = new XMLHttpRequest();
      request.open("GET",'http://147.182.172.184/ValidateExamen/',true);
      request.setRequestHeader('Authorization', 'Bearer '+token);
      request.setRequestHeader('Content-Type', 'application/json');
      request.setRequestHeader('accept', 'application/json');
  
      request.onload = function(){
  
          const status = request.status
  
          if (status == 202) {
              json = JSON.parse(request.responseText);
              statusE = json['status'];
              if(statusE == true){
                if (confirm("Examen disponible, ¿Desea realizarlo?")) {
                  window.location.replace("/Alumno/examen.html");
                } 
              }
              else{
                  alert("No hay examenes activos");
              }
          }
          else{
              alert(json.detail);
          }
      }
      request.send();
}
