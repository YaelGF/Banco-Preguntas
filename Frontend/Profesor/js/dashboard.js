function Dashboard(){
    var token = sessionStorage.getItem("token");
    var request = new XMLHttpRequest();
    request.open('GET', "http://147.182.172.184/Dashboard/Profesor/", true);
    request.setRequestHeader("Content-type", "application/json");
    request.setRequestHeader("Authorization", "Bearer " + token);
    
    request.send();
    
    const  tabla   = document.getElementById("resultados");

    var tblBody = document.createElement("tbody");
    var tblHead = document.createElement("thead");

    tblHead.innerHTML = `
        <tr class="header">
            <th style="width:50%;">Materia</th>
            <th style="width:50%;">Grupo</th>
        </tr>`;


    request.onload = () => {
        // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente
        const response = request.responseText;
        const json = JSON.parse(response);
        if (request.status === 401 || request.status === 403) {
            alert(json.detail);
        }
        else if (request.status == 202){
            const response      = request.responseText;
            const parseo_json   = JSON.parse(response);
            console.log(parseo_json);
            //regresa los datos en forma de tabla
            for (let i = 0; i < json.length; i++) {
                var tr = document.createElement('tr');
                var materia = document.createElement('td');
                var grupo = document.createElement('td');

            
                materia.innerHTML           = json[i].materia;
                grupo.innerHTML             = json[i].grupo;
                
                tr.appendChild(materia);
                tr.appendChild(grupo);
                tblBody.appendChild(tr);
            }
            tabla.appendChild(tblHead);
            tabla.appendChild(tblBody);
        }
        else{
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Algo salió mal!',
            })
        }
    };
    
    
}