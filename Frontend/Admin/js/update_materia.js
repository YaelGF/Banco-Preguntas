function update_materia(){

    var id = window.location.search.substring(1);
    console.log(id);

    var request = new XMLHttpRequest();
    request.open('PUT', "http://147.182.172.184/materias/"+id, true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");
    //request.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('token'));

    profesor1 = $("#id_profesor").val();
    materia   = $("#materia").val();
    grupo1    = $("#id_grupo").val();
    carrera   = $("#carrera").val();

    profesor = parseInt(profesor1);
    grupo    = parseInt(grupo1);
    
    //imprime los tipo de datos de las variables
    console.log(typeof profesor);
    console.log(typeof materia);
    console.log(typeof grupo);

    var data = {
        "profesor": profesor,
        "id_Grupo": grupo,
        "materia": materia
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
                text: "Materia actualizada correctamente",
                type: "success"
            }).then(function() {
                window.location = "materias.html";
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