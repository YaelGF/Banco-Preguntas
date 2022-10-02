<?php 

include "sql/preguntas.sqlite";

$resultado= $db->query("SELECT * FROM preguntas");

?>

    <!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Calificar preguntas</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container">
            <h2>Calificar preguntas</h2>
            <form action="/calificar_preguntas" method="post">
                <div class="form-group">
                    <label for="pregunta">Pregunta:</label>
                        <?php
                            while ($row = $result->fetch_assoc()) {
                                echo "<input type='text' class='form-control' id='pregunta' name='pregunta' value='" . $row['pregunta'] . "'>";
                                echo "<input type='radio' name='opc1' value='1'> " . $row['opc1'] . "<br>";
                                echo "<input type='radio' name='opc2' value='2'> " . $row['opc2'] . "<br>";
                                echo "<input type='radio' name='opc3' value='3'> " . $row['opc3'] . "<br>";
                                echo "<input type='radio' name='opc4' value='4'> " . $row['respuesta'] . "<br>";
                            }
                        ?>
                </div>
                 <input type="button" value="Calificar" onclick="CalificarRespuestas()" class="btn btn-success btn-block btn-lg">
                <script type="text/javascript" src="../js/calificar.js"></script>
            </form>
        </div>
</html>