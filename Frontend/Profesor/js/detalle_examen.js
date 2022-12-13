function detalle_examen (){

    var id_examen = window.location.search.substring(1);

    var request = new XMLHttpRequest();
    request.open('GET', 'http://147.182.172.184/examenes/'+id_examen, true);
    request.setRequestHeader("Content-type", "application/json");
    request.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('token'));
    request.send();
   
    request.onload = () => {
        const response = request.responseText;
        const json = JSON.parse(response);
        if (request.status === 401 || request.status === 403) {
            alert(json.detail);
        }
        else if (request.status == 202){
            const response      = request.responseText;
            const parseo_json   = JSON.parse(response);

            nombre          = parseo_json.nombre;
            apellidoPaaterno= parseo_json.apellidoPaterno;
            apellidoMaterno = parseo_json.apellidoMaterno;
            email           = parseo_json.email;
            matricula       = parseo_json.matricula;
            fecha           = parseo_json.fecha;
            horaInicio      = parseo_json.horaInicio;
            horaFin         = parseo_json.horaFin;
            tipoUsuario    = parseo_json.tipoUsuario;
            


            $("#nombre_profesor").val(nombre);
            $("#apellidoPaterno").val(apellidoPaaterno);
            $("#apellidoMaterno").val(apellidoMaterno);
            $("#email").val(email);
            $("#matricula").val(matricula);
            $("#fecha").val(fecha);
            $("#hora").val(horaInicio);
            $("#duracion").val(horaFin);
            $("#tipoUsuario").val(tipoUsuario);


        }
    }

}