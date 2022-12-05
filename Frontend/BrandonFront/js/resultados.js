function resultados_examen(){

    var request = new XMLHttpRequest();
    request.open('GET', "http://147.182.172.184/resultados/",true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");

    const  tabla   = document.getElementById("resultados");

    var tblBody = document.createElement("tbody");
    var tblHead = document.createElement("thead");

    tblHead.innerHTML = `
        <tr>
            <th>ID</th>
            <th>Alumno</th>
            <th>Materia</th>
            <th>Examen</th>
            <th>Fecha</th>
            <th>Hora de inicio de examen</th>
            <th>Hora de fin de examen</th>
            <th>Calificación</th>
            <th>Profesor</th>
            <th>Editar</th>
            <th>Eliminar</th>
            
        </tr>`;
    request.send();


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
                var id_resultado = document.createElement('td');
                var alumno = document.createElement('td');
                var materia = document.createElement('td');
                var examen = document.createElement('td');
                var fecha = document.createElement('td');
                var hora_inicio = document.createElement('td');
                var hora_fin = document.createElement('td');
                var calificacion = document.createElement('td');
                var profesor = document.createElement('td');
                var editar = document.createElement('td');
                var eliminar = document.createElement('td');


                id_resultado.innerHTML = json[i].id_Resultado;
                alumno.innerHTML = json[i].id_Alumno;
                materia.innerHTML = json[i].materia;
                examen.innerHTML = json[i].id_Examen;
                fecha.innerHTML = json[i].fecha;
                hora_inicio.innerHTML = json[i].horaInicio;
                hora_fin.innerHTML = json[i].horaFin;
                calificacion.innerHTML = json[i].calificacion;
                profesor.innerHTML = json[i].profesor;
                editar.innerHTML = `<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal" onclick="editar_resultado(${json[i].id_resultado})">Editar</button>`;
                eliminar.innerHTML = `<button type="button" class="btn btn-danger" onclick="eliminar_resultado(${json[i].id_resultado})">Eliminar</button>`;


                tr.appendChild(id_resultado);
                tr.appendChild(alumno);
                tr.appendChild(materia);
                tr.appendChild(examen);
                tr.appendChild(fecha);
                tr.appendChild(hora_inicio);
                tr.appendChild(hora_fin);
                tr.appendChild(calificacion);
                tr.appendChild(profesor);
                tr.appendChild(editar);
                tr.appendChild(eliminar);
                tblBody.appendChild(tr);
            }
            tabla.appendChild(tblHead);
            tabla.appendChild(tblBody);
        }
        else{
            alert("Error al obtener los resultados");
        }
    };
    
    
}


 

