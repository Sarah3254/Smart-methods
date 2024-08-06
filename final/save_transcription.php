<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Robot Control</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 20px;
            text-align: center;
        }
        h1 {
            color: #D67E5D;
        }
        button {
            background-color: #8A997D;
            color: white;
            padding: 10px 20px;
            margin: 5px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            font-size: 16px;
        }
        button:hover {
            background-color: #6B7B69;
        }
        p.error {
            color: red;
        }
        p.success {
            color: #8A997D;
        }
    </style>
</head>
<body>
    <h1>Control the Robot</h1>
    <form method="POST" action="">
        <button name="direction" value="forward">Forward</button>
        <button name="direction" value="backward">Backward</button>
        <button name="direction" value="left">Left</button>
        <button name="direction" value="right">Right</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $direction = $_POST['direction'];

        // Database connection
        $conn = new mysqli('localhost', 'root', '', 'robot_control');

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Insert direction into database
        $sql = "INSERT INTO directions (direction) VALUES ('$direction')";

        if ($conn->query($sql) === TRUE) {
            echo "<p class='success'>Direction recorded: $direction</p>";
        } else {
            echo "<p class='error'>Error: " . $sql . "<br>" . $conn->error . "</p>";
        }

        $conn->close();
    }
    ?>
</body>
</html>
