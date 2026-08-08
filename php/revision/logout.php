<?php
session_start();


if (!isset($_SESSION['user'])){
	echo "user not logged in. <a href='http://localhost:8000/form.php'>login</a>";
}else{
	
	session_unset();
	session_destroy();
	echo "user successfully logged out<br>";
	echo "<a href='http://localhost:8000/form.php'>Login</a>";
}
