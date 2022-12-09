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
            <th>Matricula</th>
            <th>Alumno</th>
            <th>Carrera</th>
            <th>Semestre</th>
            <th>Grupo</th>
            <th>Materia</th>
            <th>Fecha</th>
            <th>Hora de inicio</th>
            <th>Hora de fin</th>
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
                var matricula_alumno = document.createElement('td');
                var alumno = document.createElement('td');
                var carrera = document.createElement('td');
                var semestre = document.createElement('td');
                var grupo = document.createElement('td');
                var materia = document.createElement('td');
                var fecha = document.createElement('td');
                var hora_inicio = document.createElement('td');
                var hora_fin = document.createElement('td');
                var calificacion = document.createElement('td');
                var profesor = document.createElement('td');
                var editar = document.createElement('td');
                var eliminar = document.createElement('td');


                id_resultado.innerHTML      = json[i].id_Resultado;
                matricula_alumno.innerHTML  = json[i].Matricula_Alumno;
                alumno.innerHTML            = json[i].Alumno;
                carrera.innerHTML           = json[i].Carrera;
                semestre.innerHTML          = json[i].Semestre;
                grupo.innerHTML             = json[i].Grupo;
                materia.innerHTML           = json[i].Materia;
                fecha.innerHTML             = json[i].Fecha;
                hora_inicio.innerHTML       = json[i].Hora_Inicio;
                hora_fin.innerHTML          = json[i].Hora_Fin;
                calificacion.innerHTML      = json[i].Calificacion;
                profesor.innerHTML          = json[i].Profesor;
                editar.innerHTML            = `<a class='btn btn-success btn-s' href='../templates/update_pregunta.html?"+id_Preguntas+"'><span class='glyphicon glyphicon-pencil'></span>Editar</a>`;
                eliminar.innerHTML          = `<a class='btn btn-danger btn-sm' href='../templates/delete_pregunta.html?"+id_Preguntas+"'><span class='glyphicon glyphicon-trash'>  Borrar</a>`;


                tr.appendChild(id_resultado);
                tr.appendChild(matricula_alumno);
                tr.appendChild(alumno);
                tr.appendChild(carrera);
                tr.appendChild(semestre);
                tr.appendChild(grupo);
                tr.appendChild(materia);
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
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Algo salió mal!',
            })
        }
    };
    
    
}


 

