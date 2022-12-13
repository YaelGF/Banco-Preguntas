var json;
function getExamInfo(){
  token = sessionStorage.getItem("token");
  console.log(token);
  var request = new XMLHttpRequest();
    request.open("GET",'http://147.182.172.184/GenerarExamen/',true);
    request.setRequestHeader('Authorization', 'Bearer '+token);
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('accept', 'application/json');

    request.onload = function(){

        const status = request.status

        if (status == 202) {
            json = JSON.parse(request.responseText);
            btnn = document.getElementById("btn");
            for (var i = 0; i < json.length; i++) {
                fexamen = document.getElementById("examen");
                var p = document.createElement("p");

                p.innerHTML = json[i]['pregunta'];
                p.setAttribute("id", "p"+json[i]['id']);
                fexamen.appendChild(p);
                var input = document.createElement("input");
                input.setAttribute("type", "radio");
                input.setAttribute("id", "epcion1");
                input.setAttribute("name", "opcion"+i);
                input.setAttribute("value", json[i]['opcion1']);
                fexamen.appendChild(input);
                var label = document.createElement("label");
                label.setAttribute("for", "opcion1");
                label.innerHTML = json[i]['opcion1'];
                fexamen.appendChild(label);
                var br = document.createElement("br");
                fexamen.appendChild(br);
                var input = document.createElement("input");
                input.setAttribute("type", "radio");
                input.setAttribute("id", "opcion2");
                input.setAttribute("name", "opcion"+i);
                input.setAttribute("value", json[i]['opcion2']);
                fexamen.appendChild(input);
                var label = document.createElement("label");
                label.setAttribute("for", "opcion2");
                label.innerHTML = json[i]['opcion2'];
                fexamen.appendChild(label);
                var br = document.createElement("br");
                fexamen.appendChild(br);
                var input = document.createElement("input");
                input.setAttribute("type", "radio");
                input.setAttribute("id", "opcion3");
                input.setAttribute("name", "opcion"+i);
                input.setAttribute("value", json[i]['opcion3']);
                fexamen.appendChild(input);
                var label = document.createElement("label");
                label.setAttribute("for", "opcion3");
                label.innerHTML = json[i]['opcion3'];
                fexamen.appendChild(label);
                var br = document.createElement("br");
                fexamen.appendChild(br);
                var input = document.createElement("input");
                input.setAttribute("type", "radio");
                input.setAttribute("id", "opcion4");
                input.setAttribute("name", "opcion"+i);
                input.setAttribute("value", json[i]['opcion4']);
                fexamen.appendChild(input);
                var label = document.createElement("label");
                label.setAttribute("for", "opcion4");
                label.innerHTML = json[i]['opcion4'];
                fexamen.appendChild(label);
                var br = document.createElement("br");
                fexamen.appendChild(br);
            }
            var br = document.createElement("br");
            fexamen.appendChild(br);
            var button = document.createElement("button");
            button.setAttribute("onclick", "calificar()");
            button.innerHTML = "Calificar";
            btnn.appendChild(button);

        }

        else{
            alert(json.detail);
        }
    }
    request.send();
}
function calificar(){
    console.log(json[0]);
    console.log(json[1]);
    console.log(json.length);
    token = sessionStorage.getItem("token");
    var lis = [];
    var data = {};
    for (var i = 0; i < json.length; i++) {
        id = json[i]['id_Pregunta'];
        idE = json[i]['id_Examen'];
        data['id_Examen'] = idE;
        data['id_Pregunta'] = id;
        
        var radios = document.getElementsByName('opcion'+i);
        for (var j = 0, length = radios.length; j < length; j++) {
            if (radios[j].checked) {
                data['respuesta'] = radios[j].value;
                lis.push(data);
                data = {};
                break;
            }
        }
    }
    var request = new XMLHttpRequest();
    request.open("POST",'http://147.182.172.184/CalificarExamen/',true);
    request.setRequestHeader('Authorization', 'Bearer '+token);
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('accept', 'application/json');
    request.onload = function(){
        const status = request.status
        if (status == 202) {
            json = JSON.parse(request.responseText);
            alert(json.message);
            window.location.replace("dashboard_Alumno.html");

        }
        else{
            alert(json.detail);
        }
    }
    request.send(JSON.stringify(lis));
}
