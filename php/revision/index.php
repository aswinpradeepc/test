<?php
session_start();
$name="Guest";
if (isset($_COOKIE['name'])){
	$name=trim($_COOKIE['name'] ?? '');
}
echo "Hello $name";?><br>
<a href="http://localhost:8000/form.php"> Login here</a>
