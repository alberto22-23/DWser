<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<body>
<h1>Conexión establecida</h1>
<?php
//Lanzar una query
$query = 'SELECT * FROM tPeliculas';
$result = mysqli_query($db, $query) or die('Query error');
//Recorrer el resultado
while ($row = mysqli_fetch_array($result)){
echo $row['id'];
echo '<br>';
echo $row['nombre'];
echo '<br>';
?>
<img src="<?php echo $row['url_imagen'];?>" title="<?php echo $row['nombre']?>">
<?php
echo '<br>';
echo $row['año'];
echo '<br>';
echo $row['tema'];
echo '<br>';
}
mysqli_close($db);
?>
</body>
</html>
