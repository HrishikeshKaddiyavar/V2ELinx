<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $subject = $_POST["subject"];
    $message = $_POST["message"];

    // Set the recipient email address
    $to = "kaddiyavar.hrishikesh@gmail.com";

    // Build the email message
    $email_message = "Name: $name\n";
    $email_message .= "Email: $email\n";
    $email_message .= "Subject: $subject\n";
    $email_message .= "Message:\n$message";

    // Set additional headers
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";

    // Send the email
    mail($to, $subject, $email_message, $headers);

    // You can redirect the user to a thank you page or display a success message
    echo "Message sent successfully!";
} else {
    // Handle the case where the form is not submitted properly
    echo "Error: Form not submitted.";
}
?>
