<?php
session_start();
session_destroy;
echo "Se ha cerrado sesión";
?><br><a href="/login.html">Iniciar sesión</a><?php
//header('Location: login.html');
?>
