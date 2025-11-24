Clinic Appointment Scheduler
============================

Description
-----------
Clinic Appointment Scheduler is a desktop application for managing basic clinic appointments. It provides a graphical interface to book new appointments and view upcoming ones stored in a local SQLite database. The app is a simple learning project for Python GUI development with Tkinter and database integration using SQLite.

Features
--------
- Book new appointments with:
  - Patient name
  - Appointment date (YYYY-MM-DD)
  - Appointment time (HH:MM, 24-hour format)
  - Doctor selection from a predefined list
- View upcoming appointments in a table (Treeview)
- Basic validation for empty fields, date format, and time format
- Automatic creation of the SQLite database and table on first run
- Separation of database logic (DatabaseManager) and GUI logic (ClinicApp)

Technology Stack
----------------
- Python 3.x
- Tkinter and ttk (standard GUI toolkit in the Python standard library)
- sqlite3 (SQLite database module from the Python standard library)
- datetime (for default date values and validation)

Project Structure
-----------------
- clinic_app.py (or your chosen filename)
  - DatabaseManager class:
    - Connects to the SQLite database
    - Creates the appointments table if it does not exist
    - Inserts new appointments
    - Fetches all appointments
  - ClinicApp class:
    - Main Tk window
    - Booking form (entries and combobox)
    - Treeview to display upcoming appointments
    - Methods for validation, booking, loading data, and clearing the form
  - Application entry point:
    - if __name__ == "__main__":
      - Creates a ClinicApp instance and runs mainloop()

- clinic_appointments.db
  - SQLite database file created automatically in the same directory as the script

Database Schema
---------------
The application uses a single table named "appointments" with the following columns:

- id              : INTEGER, PRIMARY KEY, AUTOINCREMENT
- patient_name    : TEXT, NOT NULL
- appointment_date: TEXT, NOT NULL (format: YYYY-MM-DD)
- appointment_time: TEXT, NOT NULL (format: HH:MM)
- doctor          : TEXT, NOT NULL
- status          : TEXT, NOT NULL, default value 'Scheduled'

How to Run
----------
1. Install Python 3 on your system if it is not already installed.
2. Save the provided code into a file, for example: clinic_app.py
3. Place clinic_app.py in a folder where you want the database file to be created.
4. Open a terminal or command prompt in that folder.
5. Run the script:

   On Windows:
   - python clinic_app.py

   On macOS / Linux:
   - python3 clinic_app.py

6. A window titled "Clinic Appointment Scheduler" will open.

Usage Instructions
------------------
1. Booking an appointment:
   - Enter the patient's name.
   - Enter the date in YYYY-MM-DD format (defaults to today).
   - Enter the time in HH:MM (24-hour) format (defaults to 09:00).
   - Select a doctor from the dropdown list.
   - Click the "Book Appointment" button.
   - On success, a confirmation message appears and the appointment list is refreshed.

2. Viewing appointments:
   - All appointments are displayed in the "Upcoming Appointments" section.
   - Each row shows: Patient Name, Date, Time, Doctor, and Status.

3. Closing the application:
   - Close the main window using the standard window controls.
   - The database connection is closed automatically before exit.

Configuration
-------------
At the top of the script you can configure:

- DATABASE_NAME:
  - Default: 'clinic_appointments.db'
  - Change this if you want a different database file name or location.

- DOCTORS:
  - Default:
    - "Dr. Smith (General Practice)"
    - "Dr. Jones (Pediatrics)"
    - "Dr. Lee (Dermatology)"
  - Edit this list to customize the doctor options shown in the dropdown.

Validation and Error Handling
-----------------------------
- All fields (name, date, time) are required.
- Date must be in the format YYYY-MM-DD; otherwise, an error message is shown.
- Time must be in the format HH:MM (24-hour); otherwise, an error message is shown.
- Database errors during insert or fetch are printed to the console, and critical errors may show an error message box.

Limitations
-----------
- Appointments cannot be edited, updated, or deleted via the GUI.
- No detection of overlapping or conflicting appointments.
- No authentication or user roles.
- Status is always set to 'Scheduled' and cannot be changed through the GUI.
- All data is stored locally in a single SQLite database file.

Intended Use
------------
This project is mainly for educational and demonstration purposes, particularly to understand:
- How to build a basic GUI with Tkinter
- How to use ttk widgets such as Frame, LabelFrame, Entry, Combobox, Button, and Treeview
- How to connect a Tkinter frontend with a SQLite backend for persistent data storage.
