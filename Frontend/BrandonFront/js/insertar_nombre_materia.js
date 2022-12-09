function post_materias(){

    var nombre_materia = document.getElementById("nombre_materia").value;
    var data = {
        'materia': nombre_materia
    };
    
    var request = new XMLHttpRequest();
    request.open('POST', "http://147.182.172.184/nombre_materias/",true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");

    request.onload = () => {
        // Almacena la respuesta en una variable, si es 201 es que se obtuvo correctamente
        const response = request.responseText;
        const json = JSON.parse(response);
        if (request.status === 401 || request.status === 403) {
            alert(json.detail);
        }
        else if (request.status == 201){
            Swal.fire({
                title: json.message,
                text: "Materia creada correctamente",
                type: "success"
            }).then(function() {
                window.location = "../templates/mostrar_materias.html";
            });
        }
        else{
            Swal.fire({
                title: json.message,
                text: "Error al crear la materia",
                type: "error"
            }).then(function() {
                window.location = "../templates/insertar_nombre_materia.html";
            });
        }
    }
    request.send(JSON.stringify(data));
}