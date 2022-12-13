function delete_grupo() {

    var id = window.location.search.substring(1);
   
    var request = new XMLHttpRequest();
    request.open('DELETE', "http://147.182.172.184/grupos/"+id, true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");
    //request.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('token'));

    request.onload = () => {
        // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente
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
                text: "Grupo eliminado correctamente",
                type: "success"
            }).then(function() {
                window.location = "grupos.html";
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