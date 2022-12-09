function mostrar_preguntas() {

    var request = new XMLHttpRequest();
    request.open('GET', "http://147.182.172.184/preguntas/",true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");
    
    const  tabla   = document.getElementById("preguntas");

    var tblBody = document.createElement("tbody");
    var tblHead = document.createElement("thead");

    tblHead.innerHTML = `
        <tr>
            <th>ID</th>
            <th>Materia</th>
            <th>Pregunta</th>
            <th>opcion 1</th>
            <th>opcion 2</th>
            <th>opcion 3</th>
            <th>opcion 4</th>
            <th>Respuesta</th>
            <th>Detalle</th>
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
                var id_pregunta = document.createElement('td');
                var materia = document.createElement('td');
                var pregunta = document.createElement('td');
                var opcion1 = document.createElement('td');
                var opcion2 = document.createElement('td');
                var opcion3 = document.createElement('td');
                var opcion4 = document.createElement('td');
                var respuesta = document.createElement('td');
                var detalle = document.createElement('td');
                var editar = document.createElement('td');
                var eliminar = document.createElement('td');
                
                id_Preguntas            = json[i].id_Pregunta;
                id_pregunta.innerHTML   = json[i].id_Pregunta;
                materia.innerHTML       = json[i].materia;
                pregunta.innerHTML      = json[i].pregunta;
                opcion1.innerHTML       = json[i].opcion1;
                opcion2.innerHTML       = json[i].opcion2;
                opcion3.innerHTML       = json[i].opcion3;
                opcion4.innerHTML       = json[i].opcion4;
                respuesta.innerHTML     = json[i].respuesta;
                detalle.innerHTML       = "<a class='btn btn-info btn-sm' href='../templates/detalle_pregunta.html?"+id_Preguntas+"'><span class='glyphicon glyphicon-list-alt'></span>  Detalle</a>";
                editar.innerHTML        = "<a class='btn btn-success btn-sm' href='../templates/update_pregunta.html?"+id_Preguntas+"'><span class='glyphicon glyphicon-pencil'></span>  Actualizar</a>";
                eliminar.innerHTML      = "<a class='btn btn-danger btn-sm' href='../templates/delete_pregunta.html?"+id_Preguntas+"'><span class='glyphicon glyphicon-trash'>  Borrar</a>";
    
                tr.appendChild(id_pregunta);
                tr.appendChild(materia);
                tr.appendChild(pregunta);
                tr.appendChild(opcion1);
                tr.appendChild(opcion2);
                tr.appendChild(opcion3);
                tr.appendChild(opcion4);
                tr.appendChild(respuesta);
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