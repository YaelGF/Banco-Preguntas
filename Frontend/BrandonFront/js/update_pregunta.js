function update_preg(){

    var id = window.location.search.substring(1);
    
    var request = new XMLHttpRequest();
    request.open('PUT', "http://147.182.172.184/preguntas/"+id,true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");


    var pregunta = document.getElementById("pregunta").value;
    var opcion1 = document.getElementById("opcion1").value;
    var opcion2 = document.getElementById("opcion2").value;
    var opcion3 = document.getElementById("opcion3").value;
    var opcion4 = document.getElementById("opcion4").value;
    var respuesta = document.getElementById("respuesta").value;
    var materia= document.getElementById("materia").value;

    materia2 = parseInt(materia);

    var data = {
        "pregunta": pregunta,
        "opcion1": opcion1,
        "opcion2": opcion2,
        "opcion3": opcion3,
        "opcion4": opcion4,
        "opcionCorrecta": respuesta,
        "id_Materia": materia2 //id_Materia
    };

    console.log(data);


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
                text: "Pregunta actualizada correctamente",
                type: "success"
            }).then(function() {
                window.location = "../templates/mostrar_preguntas.html";
            });
        }
        else{
            alert("Error al actualizar");
        }
    }
    request.send(JSON.stringify(data));
    
}