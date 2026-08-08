<?php
echo "admin page<br>";

$name = "hello";
$email = "hello@hello.com";

$pdo = new PDO('sqlite:app.db');
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$pdo->exec("CREATE TABLE IF NOT EXISTS users(
	id INTEGER PRIMARY KEY,
	name TEXT,
	email TEXT
	)");

$stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (?,?)");
$stmt->execute([$name, $email]);

foreach ($pdo->query("SELECT * FROM users") as $row) {
	echo htmlspecialchars($row['name']). "-"
	.htmlspecialchars($row['email'])."<br>";
}
