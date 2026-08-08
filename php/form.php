<?php
$prefill = $_COOKIE['last_email'] ?? '';
?>
<form action="process.php" method="POST">
	name: <input type="text" name="name"><br>
	email: <input type="email" name="email" value="<?php echo htmlspecialchars($prefill);?>"><br>
	password: <input type="password" name="passwd"><br>
	<button type="submit">Submit</button>
</form>
