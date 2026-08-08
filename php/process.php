<?php
session_start();
$errors = [];

$name = trim($_POST['name'] ?? " ");
$email = trim($_POST['email'] ?? " ");
$pass = $_POST['passwd'];

if (strlen($pass) <6){
	$errors["pass"] = "Password should be longer than 6 chars";
}

if ($name==""){
	$errors["name"] = "name is required";
	}
	
if (!filter_var($email, FILTER_VALIDATE_EMAIL)){
	$errors["email"] = "email should be valid";
	}

if (empty($errors)){
	setcookie('last_email', $_POST['email'], time() + 3600);
	$_SESSION['user'] = $name;
	echo "<p>you entered your name: ".htmlspecialchars($name)."</p>";
	echo "<p>your email: ". htmlspecialchars($email)."</p>";
	echo "<p>your pass: ". htmlspecialchars($pass)."</p>";
}else{
	foreach($errors as $field => $msg){
	echo "<p>".htmlspecialchars($msg)."</p>";
}}


echo "<a href='http://localhost:8000/logout.php'>logout</a><br>";

echo "<a href='http://localhost:8000/form.php'>back to the form</a>";
