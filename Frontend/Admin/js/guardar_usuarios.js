function add_usuario(){

    var id = window.location.search.substring(1);
    console.log(id);

    var request = new XMLHttpRequest();
    request.open('POST', "http://147.182.172.184/login/singup/", true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");
    //request.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('token'));

    correo = $("#correo").val();
    pass   = $("#password").val();
    rol    = $("#id_rol").val();

    rol = parseInt(rol);

    if(rol == 1){
        rol = "Alumno";
    }
    else if(rol == 2){
        rol = "Profesor";
    }
    else if(rol == 3){
        rol = "Admin";
    }
    
    var data = {
        "email": correo,
        "password": pass,
        "rol": rol
    };

    console.log(data);
    
   request.onload = () => {
        // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente
        const response = request.responseText;
        const json = JSON.parse(response);
        if (request.status === 401 || request.status === 403) {
            Swal.fire({
                title: "Error al gurardar",
                text: json.detail,
                type: "error"
            });
        }
        else if (request.status == 202){
            Swal.fire({
                title: json.message,
                text: "Usuario Agregado correctamente",
                type: "success"
            }).then(function() {
                window.location = "usuarios.html";
            });
        }
        else{
            Swal.fire({
                title: "Error al crear",
                text: json.message,
                type: "error"
            });
        }
    }
    request.send(JSON.stringify([data]));
}