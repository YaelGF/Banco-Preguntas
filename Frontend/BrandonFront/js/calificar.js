function calificar_preguntas(){

  var id_preg = document.getElementById("id_preg").value;
  var respuesta = document.getElementsByName("respuesta").value;
  console.log(id_preg);
  console.log(respuesta);
  var payload = {
    "id_preg": id_preg,
    "respuesta": respuesta
  }
  console.log(payload);
  
}