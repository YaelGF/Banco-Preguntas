function insert_grupo(){
    
    var grupo        = $("#grupo").val();
    var id_carrera1  = $("#carrera").val();
    var semestre     = $("#semestre").val();

    var id_carrera = parseInt(id_carrera1);
    console.log(id_carrera);
    
    var data = [
        {
            "grupo": grupo,
            "semestre": semestre,
            "id_Carrera": id_carrera
        }
    ];

    
    var request = new XMLHttpRequest();
    request.open('POST', "http://147.182.172.184/grupos/",true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");

    request.onload = () => {
        // Almacena la respuesta en una variable, si es 201 es que se obtuvo correctamente
        const response = request.responseText;
        const json = JSON.parse(response);
        const status = request.status;
        console.log("Status: " + status);
        if (request.status === 401 || request.status === 403) {
            Swal.fire({
                title: json.message,
                text: "No tienes permiso para realizar esta acción",
                type: "error"
            });
        }
        else if (request.status == 201){
            Swal.fire({
                title: json.message,
                text: "Grupo almacenado correctamente",
                type: "success"
            }).then(function() {
                window.location = "grupos.html";
            });
        }
        else if (request.status == 400){
            Swal.fire({
                title: json.message,
                text: "Error al almacenar el grupo",
                type: "error"
            });
        }
    }
    request.send(JSON.stringify(data));
}