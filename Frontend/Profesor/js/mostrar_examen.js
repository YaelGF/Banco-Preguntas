function mostrar_examen(){
    var request = new XMLHttpRequest();
    request.open('GET', "http://147.182.172.184/examenes/", true);
    request.setRequestHeader("Content-type", "application/json");
    request.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('token'));

    const  tabla   = document.getElementById("examen");

    var tblBody = document.createElement("tbody");
    var tblHead = document.createElement("thead");

    tblHead.innerHTML = `
        <tr>
            <th>Nombre del profesor</th>
            <th>Apellido Paterno</th>
            <th>Apellido Materno</th>
            <th>Fecha</th>
            <th>Hora de inicio</th>
            <th>Hora de fin</th>

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
            //console.log(parseo_json);
            //regresa los datos en forma de tabla
            for (let i = 0; i < json.length; i++) {
                var tr = document.createElement('tr');
                var nombre_profesor = document.createElement('td');
                var apellido_paterno = document.createElement('td');
                var apellido_materno = document.createElement('td');
                var fecha = document.createElement('td');
                var hora_inicio = document.createElement('td');
                var hora_fin = document.createElement('td');

                id_examen                     = json[i].id_Examen;
                nombre_profesor.innerHTML     = json[i].nombre;
                apellido_paterno.innerHTML    = json[i].apellidoPaterno;
                apellido_materno.innerHTML    = json[i].apellidoMaterno;
                fecha.innerHTML               = json[i].fecha;
                hora_inicio.innerHTML         = json[i].horaInicio;
                hora_fin.innerHTML            = json[i].horaFin;

                //detalle.innerHTML       = "<a class='btn btn-info btn-sm' href='../templates/detalle_pregunta.html?"+id_Preguntas+"'><span class='glyphicon glyphicon-list-alt'></span>  Detalle</a>";

                tr.appendChild(nombre_profesor);
                tr.appendChild(apellido_paterno);
                tr.appendChild(apellido_materno);
                tr.appendChild(fecha);
                tr.appendChild(hora_inicio);
                tr.appendChild(hora_fin);

                tblBody.appendChild(tr);
            }
            tabla.appendChild(tblHead);
            tabla.appendChild(tblBody);
        }
    }
}

