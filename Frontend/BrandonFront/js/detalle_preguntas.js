function detalle_preguntas() {

    var id_Pregunta = window.location.search.substring(1);
    
    console.log(id_Pregunta);

    var request = new XMLHttpRequest();
    request.open('GET', "http://147.182.172.184/preguntas/"+id_Pregunta,true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("content-type", "application/json");

    //devuelve un formulario con los datos de la pregunta
    request.onload = () => {
        
        const status    = request.status;

        if (request.status === 401 || request.status === 403) {
            alert(json.detail);
        }

        else if (request.status == 202){
            const response  = request.responseText;
            const json      = JSON.parse(response);

            console.log(json);

            var pregunta    = json.pregunta;
            var materia     = json.materia;
            var opcion1     = json.opcion1;
            var opcion2     = json.opcion2;
            var opcion3     = json.opcion3;
            var opcion4     = json.opcion4;
            var respuesta   = json.respuesta;



            let pregunta_html  = document.getElementById("pregunta");
            let materia_html   = document.getElementById("materia");
            let opcion1_html   = document.getElementById("opcion1");
            let opcion2_html   = document.getElementById("opcion2");
            let opcion3_html   = document.getElementById("opcion3");
            let opcion4_html   = document.getElementById("opcion4");
            let respuesta_html = document.getElementById("respuesta");

            pregunta_html.value     = pregunta;
            materia_html.value      = materia;
            opcion1_html.value      = opcion1;
            opcion2_html.value      = opcion2;
            opcion3_html.value      = opcion3;
            opcion4_html.value      = opcion4;
            respuesta_html.value    = respuesta;
            

            
        }
        /*else if(status==404){
            let nombre  = document.getElementById("nombre");
            let email   = document.getElementById("email");

            nombre.value    = "None";
            email.value     = "None";
            alert("Cliente no encontrado");
        
        }*/
    }
    request.send();

}