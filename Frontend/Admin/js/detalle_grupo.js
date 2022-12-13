function detalle_grupo() {
    var id_grupo = location.search.substring(1);

    var request = new XMLHttpRequest();
    request.open('GET', 'http://147.182.172.184/grupos/'+id_grupo, true);
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

            grupo   = parseo_json.grupo;
            carrera = parseo_json.carrera;
            semestre = parseo_json.semestre;

            $("#grupo").val(grupo);
            $("#carrera").val(carrera);
            $("#semestre").val(semestre);
            
        }
    }


}