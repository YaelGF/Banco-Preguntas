function mostrar_alumnos(){

    var request = new XMLHttpRequest();
    request.open('GET', "http://147.182.172.184/usuarios/alumnos/",true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");
    
    const  tabla   = document.getElementById("alumnos");

    var tblBody = document.createElement("tbody");
    var tblHead = document.createElement("thead");

    tblHead.innerHTML = `
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellido Paterno</th>
            <th>Apellido Materno</th>
            <th>Matrícula</th>
            <th>Correo</th>
            <th>Carrera</th>
            <th>Grupo</th>
            <th>Vista</th>
            <th>Editar</th>
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
            for (var i = 0; i < parseo_json.length; i++) {
                var tr = document.createElement('tr');
                var id_alumno= document.createElement('td');
                var nombre_alumno = document.createElement('td');
                var apellidoP_alumno = document.createElement('td');
                var apellidoM_alumno = document.createElement('td');
                var matricula_alumno = document.createElement('td');
                var email_alumno = document.createElement('td');
                var carrera_alumno = document.createElement('td');
                var grupo_alumno = document.createElement('td');
                var vista_alumno = document.createElement('td');
                var editar_alumno = document.createElement('td');
                var btn_vista = document.createElement('button');
                var btn_editar = document.createElement('button');
                btn_vista.setAttribute('type','button');
                btn_vista.setAttribute('class','btn btn-sm btn-outline-secondary');
                btn_vista.innerHTML = 'Ver';
                btn_editar.setAttribute('type','button');
                btn_editar.setAttribute('class','btn btn-sm btn-outline-secondary');
                btn_editar.innerHTML = 'Editar';
                

                id_alumno.innerHTML = parseo_json[i].id_Alumno;
                nombre_alumno.innerHTML = parseo_json[i].nombre;
                apellidoP_alumno.innerHTML = parseo_json[i].apellidoPaterno;
                apellidoM_alumno.innerHTML = parseo_json[i].apellidoMaterno;
                matricula_alumno.innerHTML = parseo_json[i].matricula;
                email_alumno.innerHTML = parseo_json[i].email;
                carrera_alumno.innerHTML = parseo_json[i].carrera;
                grupo_alumno.innerHTML = parseo_json[i].grupo;
                btn_vista.innerHTML = "Ver";
                btn_vista.setAttribute("class", "btn btn-sm btn-outline-secondary");
                btn_vista.setAttribute("onclick", "ver_alumno("+parseo_json[i].id_alumno+")");
                vista_alumno.appendChild(btn_vista);
                editar_alumno.innerHTML = "Editar";
                editar_alumno.setAttribute("class", "btn btn-sm btn-outline-secondary");
                editar_alumno.setAttribute("onclick", "editar_alumno("+parseo_json[i].id_alumno+")");
                
                tr.appendChild(id_alumno);
                tr.appendChild(nombre_alumno);
                tr.appendChild(apellidoP_alumno);
                tr.appendChild(apellidoM_alumno);
                tr.appendChild(matricula_alumno);
                tr.appendChild(email_alumno);
                tr.appendChild(carrera_alumno);
                tr.appendChild(grupo_alumno);
                tr.appendChild(vista_alumno);
                tr.appendChild(editar_alumno);
                tblBody.appendChild(tr);

            }
            tabla.appendChild(tblHead);
            tabla.appendChild(tblBody);
        }
    };
}