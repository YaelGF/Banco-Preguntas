function login(){

    let email = document.getElementById("email");
    let password = document.getElementById("password")

    var request = new XMLHttpRequest();
    request.open("GET","http://127.0.0.1:8000/login/validate",true);
    request.setRequestHeader("Authorization", "Basic " + btoa(email.value+":"+password.value));
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('accept', 'application/json');

    request.onload = function(){
        const status = request.status
        json = JSON.parse(request.responseText);

        if (status == 202) {
            getInformation(json.token);
        }

        else{
            alert(json.detail);
        }
    };
    request.send();
};

function getInformation(token){

    var request = new XMLHttpRequest();
    request.open("GET","http://127.0.0.1:8000/login/validateToken",true);
    request.setRequestHeader('Authorization', 'Bearer '+token);
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('accept', 'application/json');

    request.onload = function(){

        const status = request.status

        if (status == 202) {
            json = JSON.parse(request.responseText);
            username = json["user"]["nombre"];
            sessionStorage.setItem("token",token);
            console.log(json);
            if(json["user"]["rol"] == "Admin"){
                getInformationUsuario(1)
            }
            else if(json["user"]["rol"] == "Alumno"){
                getInformationUsuario(2)
            }
            else if(json["user"]["rol"] == "Profesor"){
                getInformationUsuario(3)
            }
            else{
                alert("Error");
            }
        }

        else{
            alert(json.detail);
        }
    }
    request.send();
}

function getInformationUsuario(id){
    var token = sessionStorage.getItem("token");
    var request = new XMLHttpRequest();
    request.open("POST","http://127.0.0.1:8000/usuarios/Login/",true);
    request.setRequestHeader('Authorization', 'Bearer '+token);
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('accept', 'application/json');

    request.onload = function(){

        const status = request.status

        if (status == 202) {
            json = JSON.parse(request.responseText);
                
            
                if(id == 1){
                    window.location.replace("Admin/dashboard_Admin.html");
                }
                else if(id == 2){
                    window.location.replace("Alumno/dashboard_Alumno.html");
                }
                else if(id == 3){
                    window.location.replace("Profesor/dashboard_Profesor.html");
                }
            
            
        }

        else{
            alert(json.detail);
        }
    }
    request.send();

}
