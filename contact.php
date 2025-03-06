<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST["name"]);
    $email = filter_var($_POST["email"], FILTER_SANITIZE_EMAIL);
    $message = htmlspecialchars($_POST["message"]);

    // Run Python script with user inputs
    $command = escapeshellcmd("python3 contact_email.py \"$email\" \"$name\" \"$message\"");
    $output = shell_exec($command);

    if (strpos($output, "success") !== false) {
        echo "success";
    } else {
        echo "error";
    }
}
?>
