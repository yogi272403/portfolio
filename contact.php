<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// require 'vendor/autoload.php'; // If using Composer
require 'PHPMailer/PHPMailer.php'; // Uncomment if manually added
require 'PHPMailer/SMTP.php';
require 'PHPMailer/Exception.php';

$mail = new PHPMailer(true);

try {
    // Enable verbose debug output (for debugging)
    $mail->SMTPDebug = 2;  // Change to 0 when done debugging
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';  // SMTP server
    $mail->SMTPAuth = true;
    $mail->Username = 'your-email@gmail.com'; // Your Gmail
    $mail->Password = 'your-app-password';   // Use an App Password (DO NOT USE YOUR ACTUAL PASSWORD)
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port = 587;

    // Get user inputs
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    // Recipients
    $mail->setFrom($email, $name);
    $mail->addAddress('yogi.d360.2025@gmail.com'); // Your email

    // Email content
    $mail->isHTML(true);
    $mail->Subject = "New Contact Form Submission from $name";
    $mail->Body    = "<strong>Name:</strong> $name <br>
                      <strong>Email:</strong> $email <br><br>
                      <strong>Message:</strong> <br> $message";

    // Send email
    if ($mail->send()) {
        echo "Message sent successfully!";
    } else {
        echo "Mailer Error: " . $mail->ErrorInfo;
    }

} catch (Exception $e) {
    echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
}
?>
