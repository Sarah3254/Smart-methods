# Robot Control System

## Description
This project allows users to control a robot's movement direction via a web interface. It also displays the last recorded movement direction.

## Installation
To run this project locally, follow these steps:
1. **Database Setup**: 
   - Create a database named `robot_control` in phpMyAdmin or any MySQL client.
   - Use the provided SQL script to create the `directions` table within the `robot_control` database.

2. **Web Server Setup**: 
   - Install XAMPP or any other local server environment that supports PHP and MySQL.
   - Place the PHP files (`control_robot.php` and `display_last_direction.php`) in the appropriate directory (`htdocs` for XAMPP).

3. **Accessing the Project**: 
   - Start your local server (e.g., Apache in XAMPP).
   - Navigate to `http://localhost/your_directory/control_robot.php` to control the robot.
   - Navigate to `http://localhost/your_directory/display_last_direction.php` to view the last recorded direction.

## Usage
- Open `control_robot.php` in your web browser.
- Click on the directional buttons (`Forward`, `Backward`, `Left`, `Right`) to send commands to the robot.
- The selected direction will be stored in the database (`directions` table).


## Screenshots
### Control Page
![Control Page](https://github.com/Sarah3254/Smart-methods/blob/main/week2/images/Screenshot%202024-07-09%20182720.png)
*Description: Screenshot of the control_robot.php page.*

### Display Page
![Display Page](https://github.com/Sarah3254/Smart-methods/blob/main/week2/images/Screenshot%202024-07-09%20182658.png)
*Description: Screenshot of the display_last_direction.php page.*


## Database Schema
The `directions` table schema:
```sql
CREATE TABLE directions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    direction VARCHAR(10) NOT NULL
);
```
