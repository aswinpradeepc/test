<?php

$name = trim($_POST['name'] ?? " ");
echo htmlspecialchars("$name")
?>
<br>
<a href="http://localhost:8000">back</a>
