<!--sprint_3.1 Ejercicios Sesiones web-->
<?php
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>

<body>
    <?php
    session_start();
    $user_id_a_insertar = 'NULL';
    if (!empty($_SESSION['user_id'])) {
        $user_id_a_insertar = $_SESSION['user_id'];
    }
    $pelicula_id = $_POST['pelicula_id'];
    $comentario = $_POST['new_comment'];

    $query = "INSERT INTO tComentarios(comentario, pelicula_id, usuario_id) 
    VALUES ('" . $comentario . "'," . $pelicula_id . "," . $user_id_a_insertar . ")";

    mysqli_query($db, $query) or die('Error');

    echo "<p>Nuevo comentario ";
    echo mysqli_insert_id($db);
    echo " añadido</p>";
    
    echo "<a href='/detail.php?pelicula_id=" . $pelicula_id . "'>Volver</a>";
    mysqli_close($db);
    ?>
</body>

</html>