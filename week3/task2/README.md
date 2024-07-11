# Speech to Text Converter

This project is a simple web application that converts speech to text using the Web Speech API, saves the transcriptions to a MySQL database, and displays the transcriptions on the same web page. The project uses XAMPP for the server and database management.

## Features

- Converts speech to text using the Web Speech API.
- Saves transcriptions to a MySQL database.
- Displays saved transcriptions on the web page.

## Requirements

- XAMPP (Apache and MySQL)
- A modern web browser that supports the Web Speech API (e.g., Google Chrome)

## Installation

1. **Install XAMPP**:
   - Download and install XAMPP from [Apache Friends](https://www.apachefriends.org/index.html).

2. **Start XAMPP**:
   - Open the XAMPP Control Panel.
   - Start the Apache and MySQL services.

3. **Set Up the Database**:
   - Open phpMyAdmin by navigating to `http://localhost/phpmyadmin`.
   - Create a new database named `speech_to_text`.
   - Execute the following SQL command to create the `transcriptions` table:

     ```sql
     CREATE TABLE transcriptions (
         id INT AUTO_INCREMENT PRIMARY KEY,
         text VARCHAR(255) NOT NULL
     );
     ```

4. **Add Project Files**:
   - Download or clone this repository.
   - Copy the `index.html` and `save_transcription.php` files to the `htdocs` directory of your XAMPP installation (e.g., `C:\xampp\htdocs\`).

## Usage

1. **Open the Application**:
   - Open your web browser and navigate to `http://localhost/index.html`.

2. **Start Recording**:
   - Click the "Start Recording" button to begin speech recognition.
   - Speak into your microphone. The recognized text will appear on the page and be saved to the database.

3. **View Transcriptions**:
   - Transcriptions will be displayed on the same web page below the "Start Recording" button.

## Project Structure

- `index.html`: The main web page containing the user interface and JavaScript for speech recognition and handling.
- `save_transcription.php`: The PHP script that handles saving the transcriptions to the MySQL database.
