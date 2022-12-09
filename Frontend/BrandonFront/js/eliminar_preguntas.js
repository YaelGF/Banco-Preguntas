function delete_preg(){

    var id = window.location.search.substring(1);

    var request = new XMLHttpRequest();
    request.open('DELETE', "http://147.182.172.184/preguntas/"+id,true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");

    request.onload = () => {
        // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente
        const response = request.responseText;
        const json = JSON.parse(response);
        if (request.status === 401 || request.status === 403) {
            alert(json.detail);
        }
        else if (request.status == 202){
            Swal.fire({
                title: json.message,
                text: "Pregunta eliminada correctamente",
                type: "success"
            }).then(function() {
                window.location = "../templates/mostrar_preguntas.html";
            });
            //alert("Pregunta eliminada");
        }
        else{
            alert("Error al eliminar");
        }
    }
    request.send();
    
}