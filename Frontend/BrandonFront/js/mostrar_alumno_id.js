function mostrar_alumno_id(){
  
    fetch('http://147.182.172.184/usuarios/alumnos/')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        let html = '';
        data.forEach(alumno => {
            html += `
            <center>
                <div class="col-md-4">
                    <div class="card mb-4 shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">${alumno.nombre} ${alumno.apellidoPaterno} ${alumno.apellidoMaterno}</h5>
                            <p class="card-text">Matrícula: ${alumno.matricula}</p>
                            <p class="card-text">Correo: ${alumno.email}</p>
                            <p class="card-text">Carrera: ${alumno.carrera}</p>
                            <p class="card-text">Semestre: ${alumno.semestre}</p>
                            <p class="card-text">Grupo: ${alumno.grupo}</p>
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="btn-group">
                                    <button type="button" class="btn btn-sm btn-outline-secondary">Ver</button>
                                    <button type="button" class="btn btn-sm btn-outline-secondary">Editar</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </center>
            `;
        });
        document.getElementById('alumnos').innerHTML = html;
    })

}