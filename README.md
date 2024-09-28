# Canteen Information System

## Overview

The Canteen Information System is a user-friendly application designed to manage user registrations, logins, and provide relevant information about the canteen services. This system is built using Python with Tkinter for the GUI and MySQL for database management.

## Features

- **User Registration**: New users can register with their details.
- **User Login**: Registered users can log in to access the system.
- **Security Questions**: Users can select security questions for account recovery.
- **Data Management**: Interacts with a MySQL database to store user information securely.

## File Structure
<pre>Canteen-Information-System/ 
│ 
├── data.py # Data processing and analysis 
├── functions.py # Helper functions for various operations 
├── login.py # User login functionality 
├── main.py # Main application entry point 
└── register.py # User registration functionality
</pre>

## Detailed File Descriptions

### 1. `data.py`
This file is responsible for data processing and analysis within the application. It may include functions to load, clean, and analyze datasets relevant to the canteen operations. Depending on your implementation, it might also provide functionality to generate reports or statistics for the canteen's services.

- **Functions**: May include data loading, cleaning, and visualization functions.
- **Purpose**: To manage data efficiently and provide insights or summaries.

### 2. `functions.py`
This file contains helper functions that support various operations throughout the application. These functions might include validations, data formatting, or other utility functions that are reused in different parts of the system.

- **Functions**: Could include password encryption, input validations, or any repetitive task.
- **Purpose**: To keep the code DRY (Don't Repeat Yourself) by centralizing commonly used functionalities.

### 3. `login.py`
This file manages the user login process. It provides the functionality to authenticate users based on their registered credentials. The file includes GUI elements for the login interface and backend logic to check credentials against the MySQL database.

- **Functions**: May include the login function that verifies user credentials and displays appropriate messages for success or failure.
- **Purpose**: To allow registered users to access their accounts securely.

### 4. `main.py`
The main entry point of the application. This file initializes the application, sets up the GUI, and manages transitions between different screens (like registration and login). It serves as the starting point for running the entire program.

- **Functions**: Initializes the Tkinter root window, configures application settings, and calls other modules as needed.
- **Purpose**: To serve as the primary control for launching and managing the application.

### 5. `register.py`
This file handles the user registration functionality. It provides a GUI for new users to input their information, including first name, last name, contact number, email, security questions, and passwords. It also includes backend logic to store this information in a MySQL database.

- **Functions**: Validates input fields, checks if the email is already registered, and inserts new user data into the database.
- **Purpose**: To facilitate the registration of new users and ensure their data is securely stored.

## Technologies Used

- Python 3.x
- Tkinter (for GUI)
- MySQL Connector (for database interactions)
- Pillow (for image handling)

## Installation
Dowload zip file or clone this repository

### Usage
### 1. Run the application:
```bash
python login.py
```
### 2. Follow the on-screen instructions to register or log in
