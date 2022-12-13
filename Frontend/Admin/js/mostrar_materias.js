function mostrar_materias(){

    var request = new XMLHttpRequest();
    request.open('GET', "http://147.182.172.184/materias/", true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");

    const  tabla   = document.getElementById("materias");

    var tblBody = document.createElement("tbody");
    var tblHead = document.createElement("thead");

    tblHead.innerHTML = `
        <tr class="header">
            <th style="width:14%;">Materia</th>
            <th style="width:14%;">Nombre del profesor</th>
            <th style="width:14%;">Grupo</th>
            <th style="width:14%;">Carrera</th>
            <th style="width:14%;">Detalle</th>
            <th style="width:14%;">Editar</th>
            <th style="width:16%;">Eliminar</th>

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
                var materia = document.createElement('td');
                var nombre_profesor = document.createElement('td');
                var grupo = document.createElement('td');
                var carrera = document.createElement('td'); 
                var detalle = document.createElement('td');             
                var editar = document.createElement('td');
                var eliminar = document.createElement('td');
                
                id_materias                     = json[i].id_Materia;
                materia.innerHTML               = json[i].materia;
                nombre_profesor.innerHTML       = json[i].nombre;
                grupo.innerHTML                 = json[i].grupo;
                carrera.innerHTML               = json[i].carrera;
                detalle.innerHTML               = "<a class='btn btn-info btn-sm' href='detalle_materia.html?"+id_materias+"'><span class='glyphicon glyphicon-list-alt'></span>  Detalle</a>";
                editar.innerHTML                = "<a class='btn btn-success btn-sm' href='update_materia.html?"+id_materias+"'><span class='glyphicon glyphicon-pencil'></span>  Actualizar</a>";
                eliminar.innerHTML              = "<a class='btn btn-danger btn-sm' href='delete_materia.html?"+id_materias+"'><span class='glyphicon glyphicon-trash'>  Borrar</a>";

                //detalle.innerHTML       = "<a class='btn btn-info btn-sm' href='../templates/detalle_pregunta.html?"+id_Preguntas+"'><span class='glyphicon glyphicon-list-alt'></span>  Detalle</a>";
                tr.appendChild(materia);
                tr.appendChild(nombre_profesor);  
                tr.appendChild(grupo);
                tr.appendChild(carrera);
                tr.appendChild(detalle);
                tr.appendChild(editar);
                tr.appendChild(eliminar);
                tblBody.appendChild(tr);
            }
            tabla.appendChild(tblHead);
            tabla.appendChild(tblBody);
        }
    };
}