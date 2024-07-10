# ESP32 HTTP Request to Fetch Data from Database

## Description

This project involves using an ESP32 to send an HTTP request to a web page that retrieves the last direction recorded in a database. The web page is hosted locally and displays the last direction from the database. The ESP32 simulation is run on Wokwi, where the link in the HTTP request is updated to point to the local web page.

## Prerequisites

- ESP32 development board
- Local web server with PHP support (e.g., XAMPP, WAMP)
- MySQL database with a table to store directions
- WiFi network

## Setup

### Database

1. Set up a MySQL database named `robot_control`.
2. Create a table named `directions` with the following structure:
   ```sql
   CREATE TABLE directions (
       id INT AUTO_INCREMENT PRIMARY KEY,
       direction VARCHAR(255) NOT NULL
   );
   ```

### Web Pages

#### Control Page

Create a PHP file named `control_robot.php` with the following content:
```html
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
```
Place this file in the root directory of your local web server (e.g., `C:\xampp\htdocs` for XAMPP).

#### Display Data Page

Create a PHP file named `display_data.php` with the following content:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Robot Last Direction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 20px;
            color: #333; 
            text-align: center; /* Center-align content */
        }
        h1 {
            color: #D67E5D; 
        }
        p {
            font-size: 18px;
            color: #D67E5D; 
        }
    </style>
</head>
<body>
    <h1>Last Direction</h1>
    <?php
    $conn = new mysqli('localhost', 'root', '', 'robot_control');
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "SELECT direction FROM directions ORDER BY id DESC LIMIT 1";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        echo "<p>The last direction was: <strong>" . $row['direction'] . "</strong></p>";
    } else {
        echo "<p>No directions recorded yet.</p>";
    }
    $conn->close();
    ?>
</body>
</html>
```
Place this file in the root directory of your local web server (e.g., `C:\xampp\htdocs` for XAMPP).

### ESP32 Simulation

1. Open the [Wokwi simulation link](https://wokwi.com/projects/393020133767191553).
2. Update the link in the simulation code to point to your `display_data.php` page.

```
#include<WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Wokwi-GUEST";
const char* pass = "";

unsigned const long interval = 2000;
unsigned long zero = 0;

void setup(){
  Serial.begin(115200);
  WiFi.begin(ssid, pass);
  while(WiFi.status() != WL_CONNECTED){
    delay(100);
    Serial.println(".");
  }
  Serial.println("WiFi Connected!");
  Serial.println(WiFi.localIP());
}

void loop(){

  if(millis()-zero > interval){

    HTTPClient http;
    http.begin("http://your-server-ip/display_data.php");  // Update this link
    int httpResponCode = http.GET();
    Serial.println(httpResponCode);
    if(httpResponCode > 0){
      String payload = http.getString();
      Serial.print(payload);
    }else{
      Serial.print("error ");
      Serial.println(httpResponCode);
    }

    zero = millis();
  }
  
}
```

## Usage

1. Open the Wokwi simulation link.
2. Update the link in the simulation code to your `display_data.php` page.
3. Start the simulation.
4. The ESP32 will connect to the WiFi network, send an HTTP GET request to the web page, and print the response to the Serial Monitor.

## Output

### Expected Output

When the ESP32 sends an HTTP request, you should see the last recorded direction displayed in the Serial Monitor.

![Output Screenshot](https://github.com/Sarah3254/Smart-methods/blob/main/week3/Screenshot%202024-07-10%20164710.png)

## Troubleshooting

- Ensure your local web server is running and accessible from the ESP32.
- Verify the IP address of the local web server and update the ESP32 code accordingly.
- Check the Serial Monitor for any error messages or debug information.

