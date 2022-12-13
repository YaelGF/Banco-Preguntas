function delete_carrera() {
    var id = location.search.substring(1);

    var request = new XMLHttpRequest();
    request.open('DELETE', 'http://147.182.172.184/carreras/' + id, true);
    request.setRequestHeader("Content-type", "application/json");
    request.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('token'));

    request.onload = () => {
        const response = request.responseText;
        const json = JSON.parse(response);
        if (request.status === 401 || request.status === 403) {
            Swal.fire({
                title: "Error al eliminar",
                text: json.detail,
                type: "error"
            });
        }
        else if (request.status == 202){
            Swal.fire({
                title: json.message,
                text: "Carrera eliminada correctamente",
                type: "success"
            }).then(function() {
                //window.location = "../templates/mostrar_carreras.html";
            });
        }
        else if (request.status == 202 && json.message == "Error al eliminar la carrera"){
            Swal.fire({
                title: json.message,
                text: "La carrera no se puede eliminar porque tiene grupos asociados",
                type: "success"
            }).then(function() {
                //window.location = "../templates/mostrar_carreras.html";
            });
        }
    }
    request.send();
}