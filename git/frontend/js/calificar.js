function CalificarRespuestas(){

    var pregunta = document.getElementById("pregunta").value;
    var respuesta = document.getElementById("respuesta").value;

    payload = {
        "pregunta": pregunta,
        "respuesta": respuesta
    }

    console.log(payload);

    var request = new XMLHttpRequest(); 
    request.open('POST', "http://0.0.0.0:8000/preguntas/",true);
    request.setRequestHeader("accept", "application/json");
    //request.setRequestHeader("Authorization", "Bearer " + btoa(token));
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
                text: "Pregunta guardada correctamente",
                type: "success"
            }).then(function() {
                window.location = "/templates/get_preguntas.html";
            });
            
        }
    };
    request.send(JSON.stringify(payload));

};