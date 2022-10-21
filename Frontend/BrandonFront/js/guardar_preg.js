function PostPreguntas(){

    var pregunta    = document.getElementById("pregunta").value;
    var opc1        = document.getElementById("opcion1").value;
    var opc2        = document.getElementById("opcion2").value;
    var opc3        = document.getElementById("opcion3").value;
    var opcionc     = document.getElementById("opcionc").value;
    var materia     = document.getElementById("materia").value;
    

    payload = {
        "pregunta":     pregunta,
        "opcion1":      opc1,
        "opcion2":      opc2,
        "opcion3":      opc3,
        "opcionc":      opcionc,
        "materia":      materia,
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
                window.location = "/templates/mostrar_preguntas.html";
            });
            
        }
    };
    request.send(JSON.stringify(payload));

};

/*
try {
    canvas.getContext('2d').drawImage(image_target, left, top, width, height, 0, 0, width, height);
    
     var dataUrl = canvas.toDataURL("image/png"); 

     $.ajax({
             url: '../php/saveFile.php',  
             data:{ 
                 img: dataUrl
             },                     
             type: 'POST',   
             success: function(data)
             {
               alert("Imagen guardada en servidor");                       
             }
         });                
}
catch(err) {
   alert("Ocurrio un error");
}  

/*

function PostPreguntas(){
    var check       = document.getElementById("check").checked;
    var imagen      = document.getElementById("imagen").value;
    var pregunta    = document.getElementById("pregunta").value;
    var opc1        = document.getElementById("opcion1").value;
    var opc2        = document.getElementById("opcion2").value;
    var opc3        = document.getElementById("opcion3").value;
    var opcionc     = document.getElementById("opcionc").value;
    var materia     = document.getElementById("materia").value;


    /*console.log("check: " + check);
    console.log("imagen: " + imagen);
    console.log("pregunta: " + pregunta);
    console.log("opc1: " + opc1);
    console.log("opc2: " + opc2);
    console.log("opc3: " + opc3);
    console.log("opcionc: " + opcionc);
    console.log("materia: " + materia);

    if (check == true){
        //guardar imagen en servidor
        var imagen      = document.getElementById("imagen").value;
        
        

        
        payload = {
            "imagen":       dataUrl,
            "pregunta":     pregunta,
            "opcion1":      opc1,
            "opcion2":      opc2,
            "opcion3":      opc3,
            "opcionc":      opcionc,
            "materia":      materia
        }
    }
    else{
        payload = {
            "pregunta":     pregunta,
            "opcion1":      opc1,
            "opcion2":      opc2,
            "opcion3":      opc3,
            "opcionc":      opcionc,
            "materia":      materia
        }
    }

    console.log(payload);
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