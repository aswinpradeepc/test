<?php

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
	echo "<p>you entered your name: ".htmlspecialchars($name)."</p>";
	echo "<p>your email: ". htmlspecialchars($email)."</p>";
	echo "<p>your pass: ". htmlspecialchars($pass)."</p>";
	session_start();
	$_SESSION['user'] = $name;
}else{
	foreach($errors as $e){
	echo "$e and $errors[$e]";
}}


echo "<a href='http://localhost:8000/logout.php'>logout</a><br>";

echo "<a href='http://localhost:8000/form.php'>back to the form</a>";
