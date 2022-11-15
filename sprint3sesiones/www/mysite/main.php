<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<head>
<style>
h2:hover{
background-color: yellow;
}
h2{
transition: background-color 0.8s linear 0.2s;
}
</style>
</head>
<body>
<h2>---Conexión establecida---</h2>
<h1>Películas</h1>
<hr>
<h3>Sesión iniciada por: <?php
$nuevoUsuario = $_POST['usuActiv'];
echo $nuevoUsuario; ?></h3>
<a href="/login.html">Iniciar sesión</a><br>
<a href="/logout.php">Cerrar sesión</a><br>
<hr>
<?php
//Lanzar una query
$query = 'SELECT * FROM tPeliculas';
$result = mysqli_query($db, $query) or die('Query error');
//Recorrer el resultado
while ($row = mysqli_fetch_array($result)){
echo '<h2>'.$row['id'].' - '.$row['nombre'].'</h2>';
echo '<br>';
?>
<img src="<?php echo $row['url_imagen'];?>" title="<?php echo $row['nombre']?>">
<?php
echo '<br>';
echo '<h3>'.$row['año'].' - '. $row['tema'].'</h3>';
echo '<br>';
}
mysqli_close($db);
?>
</body>
</html>
