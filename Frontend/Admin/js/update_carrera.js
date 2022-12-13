function update_carrera() {
    var id = location.search.split('?')[1];
    
    var request = new XMLHttpRequest();
    request.open('PUT', 'http://147.182.172.184/carreras/' + id, true);
    request.setRequestHeader("Content-type", "application/json");
    request.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('token'));

    var carrera = $('#carrera').val()
    var id_coordinador1 = $('#id_coordinador').val()

    var id_coordinador = parseInt(id_coordinador1);

    var data = JSON.stringify({
        "carrera": carrera,
        "coordinador": id_coordinador
    });

    request.onload = () => {
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
                text: "Carrera actualizada correctamente",
                type: "success"
            }).then(function() {
                window.location = "../templates/mostrar_carreras.html";
            });
        }
    }
    request.send(data);    
}