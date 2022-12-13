function detalle_carrera(){
    // Obtiene el id del grupo a mostrar
    var id_carrera = location.search.split('?')[1];
    //console.log(id_carrera);

    var request = new XMLHttpRequest();
    request.open('GET', 'http://147.182.172.184/carreras/' + id_carrera, true);
    request.setRequestHeader("Content-type", "application/json");
    request.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('token'));

    request.onload = () => {
        const response = request.responseText;
        const json = JSON.parse(response);
        if (request.status === 401 || request.status === 403) {
            alert(json.detail);
        }
        else if (request.status == 202){
            const response      = request.responseText;
            const parseo_json   = JSON.parse(response);

            carrera         = parseo_json.carrera;
            nombre          = parseo_json.nombre;
            apellidoPaterno = parseo_json.apellidoPaterno;
            apellidoMaterno = parseo_json.apellidoMaterno;
            email           = parseo_json.email;
            matricula       = parseo_json.matricula;
            ocupacion       = parseo_json.tipoUsuario;
            id_coordinador  = parseo_json.id_Usuario;


            $("#carrera").val(carrera);
            $("#nombre").val(nombre);
            $("#apellidoPaterno").val(apellidoPaterno);
            $("#apellidoMaterno").val(apellidoMaterno);
            $("#email").val(email);
            $("#matricula").val(matricula);
            $("#ocupacion").val(ocupacion);
            $("#id_coordinador").val(id_coordinador);
        }
    }
    request.send();
}

    