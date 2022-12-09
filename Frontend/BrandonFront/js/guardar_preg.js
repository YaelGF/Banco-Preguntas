function PostPreguntas(){

    const token = sessionStorage.getItem('token');
    
    console.log(token);

    
    var request = new XMLHttpRequest(); 
    request.open('POST', "http://147.182.172.184/preguntas/Front/",true);
    request.setRequestHeader("accept", "application/json");
    request.setRequestHeader("Authorization", "Bearer " +token);
    request.setRequestHeader("Content-Type", "application/json");


    var pregunta    = document.getElementById("pregunta").value;
    var opc1        = document.getElementById("opcion1").value;
    var opc2        = document.getElementById("opcion2").value;
    var opc3        = document.getElementById("opcion3").value;
    var opc4        = document.getElementById("opcion4").value;
    var opcionc     = document.getElementById("opcionc").value;
    var materia     = document.getElementById("materia").value;
    //convierte la materia en entero
    materia2 = parseInt(materia);

    var payload = {
        "pregunta":         pregunta,
        "opcion1":          opc1,
        "opcion2":          opc2,
        "opcion3":          opc3,
        "opcion4":          opc4,
        "opcionCorrecta":   opcionc,
        "id_Materia":       materia2
    }


    console.log(payload);

    request.onload = () => {
        const response  = request.responseText;
        const json      = JSON.parse(response);
        const status    = request.status;

        const mensaje  = json.message;

        if (request.status === 401 || request.status === 403) {
            Swal.fire({
                title: "Error",
                text: json.detail,
                type: "error"
            });
            //imprime el error en la consola
            console.log("Response: " + response);
        }
        else if (request.status == 202 && mensaje == "Pregunta insertada correctamente"){
            Swal.fire({
                title: "Exito",
                text: "Pregunta almacenada correctamente",
                type: "success"
            }).then(function() {
                window.location = "../templates/mostrar_preguntas.html";
            });
        }
        else if (request.status == 202 && mensaje == "Error al obtener las preguntas"){

            console.log("Response: " + response);
            console.log("JSON: " + json);
            console.log("Status: " + status);

            Swal.fire({
                title: "Error al insertar la pregunta",
                text: "Error vuelve a intentarlo",
                type: "error"
            });

        }
    };
    request.send(JSON.stringify(payload));

}


/*
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

            Swal.fire({
                title: json.message,
                text: "Pregunta guardada correctamente",
                type: "success"
            }).then(function() {
                window.location = "/templates/get_preguntas.html";
            });

        }
    };*/

    /*payload = {
        "pregunta":     pregunta,
        "opcion1":      opc1,
        "opcion2":      opc2,
        "opcion3":      opc3,
        "opcionc":      opcionc,
        "materia":      materia,
        "carrera":      carrera,
        "imagen":       imagen
    }

    console.log(payload);*/



/*
    payload = {
        "pregunta":     pregunta,
        "opcion1":      opc1,
        "opcion2":      opc2,
        "opcion3":      opc3,
        "opcionc":      opcionc,
        "materia":      materia,
        "carrera":      carrera
    }check

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

    2 check button  si la respuesta es si, guarda la imagen y si es no pos nada 

};*/