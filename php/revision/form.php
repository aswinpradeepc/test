<?php
session_start();

if (isset($_COOKIE['name'])){
	$name=$_COOKIE['name'];
	$email=$_COOKIE['email'];
	echo "user has logged in before";
} ?>

<style>
.container{
display: flex;
flex-direction: column;
width: 10rem;
}
</style>
<form action="process.php" method="POST" class="container">
	Name: <input type="text" name="name" value="<?php echo htmlspecialchars($name)?>">
	email: <input type="email" name="email" value="<?php echo htmlspecialchars($email)?>">
	password: <input type="password" name="password"><br>
	<button type="submit">sign up/Login</button>
</form>
