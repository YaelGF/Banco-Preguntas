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
    request.open("GET","http://127.0.0.1:8000/login/info",true);
    request.setRequestHeader('Authorization', 'Bearer '+token);
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('accept', 'application/json');

    request.onload = function(){

        const status = request.status

        if (status == 202) {
            json = JSON.parse(request.responseText);
            username = json["user"]["nombre"];
            sessionStorage.setItem("token",token);
            if(json["user"]["rol"] == "Admin"){
                window.location.replace("/dashboard_Admin.html");
            }
            else if(json["user"]["rol"] == "Alumno"){
                window.location.replace("/dashboard_Alumno.html");
            }
            else if(json["user"]["rol"] == "Profesor"){
                window.location.replace("/dashboard_Profesor.html");
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