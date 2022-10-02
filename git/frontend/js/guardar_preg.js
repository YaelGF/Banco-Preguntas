function PostPreguntas(){

    var pregunta    = document.getElementById("pregunta").value;
    var imagen      = document.getElementById("imagen").value;
    var opc1        = document.getElementById("opc1").value;
    var opc2        = document.getElementById("opc2").value;
    var opc3        = document.getElementById("opc3").value;
    var respuesta   = document.getElementById("respuesta").value;
    var materia     = document.getElementById("materia").value;
    var carrera     = document.getElementById("carrera").value;


    payload = {
        "pregunta":     pregunta,
        "imagen":       imagen,
        "opcion1":      opc1,
        "opcion2":      opc2,
        "opcion3":      opc3,
        "respuesta":    respuesta,
        "materia":      materia,
        "carrera":      carrera
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
