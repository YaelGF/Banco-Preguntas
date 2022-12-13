function delete_materia() {
    var id_materia = location.search.substring(1);
    var request = new XMLHttpRequest();
    request.open('DELETE', "http://147.182.172.184/materias/"+id_materia, true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");

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
                text: "Se le redireccionará a la página de materias",
                type: "success"
            }).then(function() {
                window.location = "materias.html";
            });
        }
        else{
            Swal.fire({
                title: "Error al eliminar",
                text: json.message,
                type: "error"
            });
        }
    }
    request.send();
}