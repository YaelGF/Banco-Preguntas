function detalle_materia() {
    var id_materia = location.search.substring(1);
    var request = new XMLHttpRequest();
    request.open('GET', 'http://147.182.172.184/materias/'+id_materia, true);
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
            //console.log(parseo_json);

            nombre  = parseo_json.nombre;
            materia = parseo_json.materia;
            grupo   = parseo_json.grupo;
            carrera = parseo_json.carrera;

            $("#nombre_profesor").val(nombre);
            $("#materia").val(materia);
            $("#grupo").val(grupo);
            $("#carrera").val(carrera);
            
        }
    };
}