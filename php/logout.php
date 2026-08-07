<?php
session_start();
if (!isset($_SESSION['user'])){
	echo "user not logged in. Login ";
	echo"<a href='http://localhost:8000/form.php'>here</a>";
	}else{
session_unset();
session_destroy();
echo "Logged out. Login <a href='http://localhost:8000/form.php'>here</a>";}
