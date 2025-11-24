# Clinic Appointment Scheduler

A simple desktop application for booking and viewing clinic appointments using Python, Tkinter, and SQLite. It demonstrates a clean separation between database operations and GUI presentation.[web:6][web:14]

## Features

- Book new appointments with:
  - Patient name
  - Appointment date (`YYYY-MM-DD`)
  - Appointment time (`HH:MM`, 24-hour)
  - Doctor selection from a predefined list
- View upcoming appointments in a table (Tkinter `ttk.Treeview`)
- Basic validation for empty fields, date format, and time format
- Automatic SQLite database and table creation on first run

## Tech Stack

- **Language:** Python 3.x
- **GUI:** Tkinter / ttk (standard library)
- **Database:** SQLite via `sqlite3` (standard library)
- **Other:** `datetime` for date/time handling[web:20]

## Project Structure

- `clinic_app.py` (example name)
  - `DatabaseManager` class
    - Handles DB connection, table creation, insert, and fetch operations
  - `ClinicApp` class
    - Tkinter `Tk` main window
    - Form fields for booking appointments
    - Treeview for displaying upcoming appointments
  - `if __name__ == "__main__":`
    - Creates `ClinicApp` instance and starts the main event loop
- `clinic_appointments.db`
  - SQLite database file created in the same directory as the script

## Database Schema

The application uses a single table called `appointments`:

| Column           | Type    | Description                                   |
|------------------|---------|-----------------------------------------------|
| `id`             | INTEGER | Primary key, auto-incremented                 |
| `patient_name`   | TEXT    | Patient's full name (required)                |
| `appointment_date` | TEXT  | Date in `YYYY-MM-DD` format (required)       |
| `appointment_time` | TEXT  | Time in `HH:MM` format (required)            |
| `doctor`         | TEXT    | Selected doctor name (required)              |
| `status`         | TEXT    | Appointment status, default `'Scheduled'`    |

## Getting Started

### Prerequisites

- Python 3 installed on your system.[web:20]
- No external libraries required (Tkinter and sqlite3 come with standard Python on most platforms).[web:20]

### Installation and Run

1. Save the provided Python code into a file, for example:
2. Open a terminal/command prompt in the folder containing `clinic_app.py`.

3. Run the script:

- Windows:

  ```
  python clinic_app.py
  ```

- macOS / Linux:

  ```
  python3 clinic_app.py
  ```

4. The **Clinic Appointment Scheduler** window should appear.

## Usage

1. **Book a new appointment**
- Enter the patient name.
- Adjust the date (`YYYY-MM-DD`) if needed (defaults to today).
- Adjust the time (`HH:MM`) if needed (defaults to `09:00`).
- Select a doctor from the dropdown.
- Click **Book Appointment**.
- A confirmation dialog appears on success, and the table is refreshed.

2. **View upcoming appointments**
- Check the **Upcoming Appointments** section (bottom half of the window).
- Each row shows patient name, date, time, doctor, and status.

3. **Exit**
- Close the window via the system window controls.
- The database connection is closed automatically.

## Configuration

At the top of the script:

- `DATABASE_NAME = 'clinic_appointments.db'`
- Change if you want a different database filename or location.
- `DOCTORS = [...]`
- Modify this list to change available doctors displayed in the doctor dropdown.

## Limitations and Ideas for Improvement

Current limitations:

- No edit/update/delete of existing appointments.
- No conflict detection for overlapping appointments.
- No user authentication or multi-user support.
- Status is fixed to `'Scheduled'` and not editable in the GUI.

Possible extensions:

- Add appointment editing and cancellation.
- Implement time-slot conflict checks.
- Add filters/search for appointments by doctor or date.
- Add login and role-based access (e.g., admin vs. receptionist).[web:1][web:4]

## License

Specify your preferred license here (e.g., MIT, GPL) depending on how you plan to share or reuse this code. Ensure compliance with any third-party dependencies or sample code you may incorporate.[web:19]
