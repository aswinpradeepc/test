<?php
session_start();

$errors=[];

$name=trim($_POST['name'] ?? '');
$email=trim($_POST['email'] ?? '');
$password=$_POST['password'] ?? '';

if (empty($name)){
	$errors[] = "Name is required";
}
if (!filter_var($email, FILTER_VALIDATE_EMAIL)){
	$errors[] = "email is invalid";
}
if (strlen($password) < 6){
	$errors[] = "password should be more that 6 chars";
}

if (empty($errors)){
	setcookie("email",$email,time()+3600);
	setcookie("name",$name,time()+3600);
	$_SESSION['user']=$name;	
	echo "<p>name is ".htmlspecialchars($name)."</p>";
	echo "<p>email is ".htmlspecialchars($email)."</p>";
	echo "<p>entered pass :".htmlspecialchars($password)."</p><br>";
	echo "<a href='http://localhost:8000/logout.php'>Logout</a>";	
}else{
	foreach ($errors as $e){
		echo "error: ".htmlspecialchars($e)."<br>";
	}
}
