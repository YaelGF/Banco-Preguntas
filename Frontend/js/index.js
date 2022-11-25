function login(){

    let email = document.getElementById("email");
    let password = document.getElementById("password")

    var request = new XMLHttpRequest();
    request.open("GET","http://147.182.172.184/login/validate",true);
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
    request.open("GET","http://147.182.172.184/login/validateToken",true);
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
                window.location.replace("Admin/dashboard_Admin.html");
            }
            else if(json["user"]["rol"] == "Alumno"){
                window.location.replace("Alumno/dashboard_Alumno.html");
            }
            else if(json["user"]["rol"] == "Profesor"){
                window.location.replace("Profesor/dashboard_Profesor.html");
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