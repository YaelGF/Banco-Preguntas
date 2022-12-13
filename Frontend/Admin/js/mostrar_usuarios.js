function mostrar_usuarios(){

    var request = new XMLHttpRequest();
    request.open('GET', "http://147.182.172.184/usuarios/", true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");

    const  tabla   = document.getElementById("usuarios");

    var tblBody = document.createElement("tbody");
    var tblHead = document.createElement("thead");

    tblHead.innerHTML = `
        <tr class="header">
            <th style="width:14%;">Nombre</th>
            <th style="width:14%;">Apellido Paterno</th>
            <th style="width:14%;">Correo</th>
            <th style="width:14%;">Rol</th>
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
                var nombre = document.createElement('td');
                var apellido_paterno = document.createElement('td');
                var correo = document.createElement('td');
                var rol = document.createElement('td'); 
                var detalle = document.createElement('td');             
                var editar = document.createElement('td');
                var eliminar = document.createElement('td');
                
                id_usuario = json[i].id_Usuario;
                nombre.innerHTML = json[i].nombre;
                apellido_paterno.innerHTML = json[i].apellidoPaterno;
                correo.innerHTML = json[i].email;
                rol.innerHTML = json[i].tipoUsuario;
                detalle.innerHTML               = "<a class='btn btn-info btn-sm' href='detalle_usuario.html?"+id_usuario+"'><span class='glyphicon glyphicon-list-alt'></span>  Detalle</a>";
                editar.innerHTML                = "<a class='btn btn-success btn-sm' href='update_usuario.html?"+id_usuario+"'><span class='glyphicon glyphicon-pencil'></span>  Actualizar</a>";
                eliminar.innerHTML              = "<a class='btn btn-danger btn-sm' href='delete_usuario.html?"+id_usuario+"'><span class='glyphicon glyphicon-trash'>  Borrar</a>";

                //detalle.innerHTML       = "<a class='btn btn-info btn-sm' href='../templates/detalle_pregunta.html?"+id_Preguntas+"'><span class='glyphicon glyphicon-list-alt'></span>  Detalle</a>";
                tr.appendChild(nombre);
                tr.appendChild(apellido_paterno);
                tr.appendChild(correo);
                tr.appendChild(rol);
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