function PostPreguntas(){

    payload = {
        "pregunta": $("#pregunta").val(),
        "imagen": $("#imagen").val(),
        "opc1" : $("#opc1").val(),
        "opc2" : $("#opc2").val(),
        "opc3" : $("#opc3").val(),
        "respuesta" : $("#respuesta").val(),
        "materia" : $("#materia").val(),
        "carrera" : $("#carrera").val(),
        
    }

    /*$.ajax({
        url: "http://localhost:3000/api/preguntas",
        type: "POST",
        data: JSON.stringify(payload),
        contentType: "application/json",
        success: function(data){
            alert("Pregunta guardada");
            console.log(data);
        },
        error: function(error){
            alert("Error al guardar pregunta");
            console.log(error);
        }
    });*/


    var request = new XMLHttpRequest(); 
    request.open('POST', "http://0.0.0.0:8000//preguntas/",true);
    request.setRequestHeader("accept", "application/json");
    request.setRequestHeader("Content-Type", "application/json");

    request.onload = () => {
        
        const response  = request.responseText;
        const json      = JSON.parse(response); 
        
        const status    = request.status;

        if (request.status === 401 || request.status === 403) {
            alert(json.detail);
        }

        else if (request.status == 202){

            console.log("Response: " + response);
            console.log("JSON: " + json);
            console.log("Status: " + status);

            Swal.fire({
                title: json.message,
                text: "Regresar a la lista de clientes ",
                type: "success"
            }).then(function() {
                window.location = "";
            });
            
        }
    };
    request.send(JSON.stringify(payload));
};