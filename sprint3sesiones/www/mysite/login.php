<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
$email_posted = $_POST['f_email'];
$password_posted = $_POST['f_password'];
$query = "SELECT id, contraseña, email FROM tUsuarios WHERE email = '".$email_posted."'";
$result = mysqli_query($db, $query) or die('Query error');
if (mysqli_num_rows($result) > 0) {
$only_row = mysqli_fetch_array($result);
if ($only_row[1] == $password_posted) {
session_start();
$_SESSION['user_id'] = $only_row[0];
//añadido:
$usuActivo=$only_row[2];
echo 'Iniciando sesión: '.$usuActivo;
?>
<!--<br><a href="/main.php">Ir a Inicio</a>-->
<form action="main.php" method="post">
<input name="usuActiv" type="text" value=<?php echo $usuActivo ?>><br>
<input type="submit" value="Ir a inicio">
</form>
<?php
//header('Location: main.php');
} else {
echo '<p>Contraseña incorrecta</p>';
}
} else {
echo '<p>Usuario no encontrado con ese email</p>';
}
?>
