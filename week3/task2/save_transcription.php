<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $text = $_POST['text'];

    // Database connection
    $conn = new mysqli('localhost', 'root', '', 'speech_to_text');

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Insert text into database
    $sql = "INSERT INTO transcriptions (text) VALUES ('$text')";

    if ($conn->query($sql) === TRUE) {
        echo "Transcription saved successfully.";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}
?>
