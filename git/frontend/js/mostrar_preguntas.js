function mostrar_preguntas(){
    var request = new XMLHttpRequest();
    request.open('GET', "http://0.0.0.0:8000/preguntas/",true);
    request.onload = function(){
        var data = JSON.parse(this.response);
        
        console.log(data);
        var html = "";
        for (var i = 0; i < data.length; i++) {
            html += "<div class='card'>";
            html += "<div class='card-body'>";
            html += "<h5 class='card-title'>" + data[i].pregunta + "</h5>";
            html += "<p class='card-text'>" + data[i].opcion1 + "</p>";
            html += "<p class='card-text'>" + data[i].opcion2 + "</p>";
            html += "<p class='card-text'>" + data[i].opcion3 + "</p>";
            html += "<p class='card-text'>" + data[i].opcionc + "</p>";
            html += "<p class='card-text'>" + data[i].materia + "</p>";
            html += "</div>";
            html += "</div>";
        }
        document.getElementById("preguntas").innerHTML = html;
    }
    request.send();
}