function update_grupo (){
    var id = window.location.search.substring(1);
    console.log(id);

    var request = new XMLHttpRequest();
    request.open('PUT', "http://147.182.172.184/grupos/"+id, true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");
    //request.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('token'));

    grupo       = $("#grupo").val();
    carrera1    = $("#carrera").val();
    semestre    = $("#semestre").val();

    carrera = parseInt(carrera1);

    var data = {
        "grupo": grupo,
        "semestre": semestre,
        "id_Carrera": carrera
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
                text: "Grupo actualizado correctamente",
                type: "success"
            }).then(function() {
                window.location = "grupos.html";
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