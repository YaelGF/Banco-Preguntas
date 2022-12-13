function update_usuario(){

    var id = window.location.search.substring(1);
    console.log(id);

    var request = new XMLHttpRequest();
    request.open('PUT', "http://147.182.172.184/usuarios/"+id, true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");
    //request.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('token'));

    

    nombre = $("#nombre").val();
    apellidop = $("#apellidoP").val();
    apellidom = $("#apellidoM").val();
    correo = $("#correo").val();
    uid = $("#uid").val();
    matricula = $("#matricula").val();
    rol = $("#id_rol").val();
    rol = parseInt(rol);


    var data = {
        "nombre": nombre,
        "apellidoPaterno": apellidop,
        "apellidoMaterno": apellidom,
        "email": correo,
        "uid": uid,
        "matricula": matricula,
        "id_TipoUsuario": rol
    };

    console.log(data);
    
   request.onload = () => {
        // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente
        const response = request.responseText;
        const json = JSON.parse(response);
        if (request.status === 401 || request.status === 403) {
            Swal.fire({
                title: "Error al actualizar",
                text: json.detail,
                type: "error"
            });
        }
        else if (request.status == 202){
            Swal.fire({
                title: json.message,
                text: "Usuario actualizado correctamente",
                type: "success"
            }).then(function() {
                window.location = "usuarios.html";
            });
        }
        else{
            Swal.fire({
                title: "Error al actualizar",
                text: json.message,
                type: "error"
            });
        }
    }
    request.send(JSON.stringify(data));
}