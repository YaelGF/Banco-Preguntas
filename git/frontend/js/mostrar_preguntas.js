/*function mostrar_preguntas(){
    var request = new XMLHttpRequest();
    request.open('GET', "http://0.0.0.0:8000/preguntas/",true);


    request.onload = function(){
        var data = JSON.parse(this.response);
        
        console.log(data);
        
        const data     = request.responseText;
        const parseo_json   = JSON.parse(data);
        
        var html = "";

        
        for (var i = 0; i < data.length; i++) {
            html += "<div class='card'>";
            html += "<div class='card-body'>";
            html += "<h5 class='card-title'>" + data[i].pregunta + "</h5>";
            html += "<input type='text' value='" + data[i].preguntas_preg + "' preguntas='preguntas_preg' hpreguntasden>";
            console.log(data[i].preguntas_preg);
            html += "<input type='radio' name='respuesta' value='" + data[i].opcion1 + "'>" + data[i].opcion1 + "<br>";
            html += "<input type='radio' name='respuesta' value='" + data[i].opcion2 + "'>" + data[i].opcion2 + "<br>";
            html += "<input type='radio' name='respuesta' value='" + data[i].opcion3 + "'>" + data[i].opcion3 + "<br>";   
            html += "<input type='radio' name='respuesta' value='" + data[i].opcionc + "'>" + data[i].opcionc + "<br>";    
            html += "</div>";
            html += "</div>";
        }
        html += "<button type='button' class='btn btn-primary' onclick='calificar_preguntas()'>Calificar</button>";
        document.getElementBypreguntas("preguntas").innerHTML = html;

        
    }
    request.send();
}*/

function mostrar_preguntas() {

    var request = new XMLHttpRequest();
    request.open('GET', "http://0.0.0.0:8000/preguntas/",true);
    request.setRequestHeader("Accept", "application/json");
    //request.setRequestHeader("Authorization", "Bearer " + btoa(token));
    request.setRequestHeader("content-type", "application/json");
    

    request.onload = () => {
        // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente
        const response = request.responseText;
        const json = JSON.parse(response);

        //console.log(json);

        var html = "";

        if (request.status === 401 || request.status === 403) {
            alert("No tienes permiso para ver esta información");
        }
        
        else if (request.status == 202){
            const response      = request.responseText;
            const parseo_json   = JSON.parse(response);
            
            for (var key in parseo_json) {
                
                for (var preguntas in parseo_json[key]) {
                    //console.log(preguntas);
                    //console.log(parseo_json[key][preguntas].pregunta)

                    var id_pregunta = parseo_json[key][preguntas].id_preg;
                    var pregunta    = parseo_json[key][preguntas].pregunta;
                    var opcion1     = parseo_json[key][preguntas].opcion1;
                    var opcion2     = parseo_json[key][preguntas].opcion2;
                    var opcion3     = parseo_json[key][preguntas].opcion3;
                    var opcionc     = parseo_json[key][preguntas].opcionc;

                    html += "<div class='card'>";
                    html += "<div class='card-body'>";
                    html += "<form id='form_preguntas'>";
                    html += "<fieldset>";
                    html += "<legend>" + pregunta + "</legend>";
                    html += "<input type='hidden' value='" + id_pregunta + "' name='id_preg' id='id_preg'>";
                    html += "<input type='radio' name='respuesta' id='respuesta' value='" + opcion1 + "'>" + opcion1 + "<br>";
                    html += "<input type='radio' name='respuesta' id='respuesta' value='" + opcion2 + "'>" + opcion2 + "<br>";
                    html += "<input type='radio' name='respuesta' id='respuesta' value='" + opcion3 + "'>" + opcion3 + "<br>";   
                    html += "<input type='radio' name='respuesta' id='respuesta' value='" + opcionc + "'>" + opcionc + "<br>";    
                    html += "</fieldset>";
                    html += "</form>";
                    html += "</div>";
                    html += "</div>";
                    
                }
            }
            html += "<button type='button' class='btn btn-primary' onclick='calificar_preguntas()'>Calificar</button>";
            document.getElementById("preguntas").innerHTML = html;
        }
    };
    request.send();
}