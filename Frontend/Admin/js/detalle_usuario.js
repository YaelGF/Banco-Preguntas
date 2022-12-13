function detalle_usuario() {
    var id_materia = location.search.substring(1);
    var request = new XMLHttpRequest();
    request.open('GET', 'http://147.182.172.184/usuarios/'+id_materia, true);
    request.setRequestHeader("Content-type", "application/json");
    
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
            //console.log(parseo_json);

            nombre  = parseo_json.nombre;
            apellidoP = parseo_json.apellidoPaterno;
            apellidoM = parseo_json.apellidoMaterno;
            email = parseo_json.email;
            uid = parseo_json.uid;
            matricula = parseo_json.matricula;
            rol = parseo_json.tipoUsuario;

            $("#nombre").val(nombre);
            $("#apellidoP").val(apellidoP);
            $("#apellidoM").val(apellidoM);
            $("#correo").val(email);
            $("#uid").val(uid);
            $("#matricula").val(matricula);
            $("#rol").val(rol);
            
        }
    };
}