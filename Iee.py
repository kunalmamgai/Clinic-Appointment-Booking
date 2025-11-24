import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# --- Configuration ---
DATABASE_NAME = 'clinic_appointments.db'
DOCTORS = ["Dr. Smith (General Practice)", "Dr. Jones (Pediatrics)", "Dr. Lee (Dermatology)"]


# ==============================================================================
# 1. Database Management Layer (Data Logic)
# ==============================================================================

class DatabaseManager:
    """Handles all database connections and operations (CRUD)."""

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._connect()
        self._create_table()

    def _connect(self):
        """Establishes a connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            messagebox.showerror("DB Error", "Failed to connect to the database.")

    def _create_table(self):
        """Creates the appointments table if it doesn't exist."""
        sql = """
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            doctor TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Scheduled'
        );
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def insert_appointment(self, name, date, time, doctor):
        """Inserts a new appointment record."""
        sql = """
        INSERT INTO appointments (patient_name, appointment_date, appointment_time, doctor) 
        VALUES (?, ?, ?, ?);
        """
        try:
            self.cursor.execute(sql, (name, date, time, doctor))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error inserting appointment: {e}")
            return False

    def fetch_appointments(self):
        """Fetches all scheduled appointments."""
        sql = "SELECT patient_name, appointment_date, appointment_time, doctor, status FROM appointments ORDER BY appointment_date, appointment_time;"
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching appointments: {e}")
            return []

    def close(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()


# ==============================================================================
# 2. Application and GUI Layer (Presentation Logic)
# ==============================================================================

class ClinicApp(tk.Tk):
    """The main application window."""

    def __init__(self):
        super().__init__()
        self.title("Clinic Appointment Scheduler")
        self.geometry("800x600")

        # Initialize Database Manager
        self.db = DatabaseManager(DATABASE_NAME)
        self.protocol("WM_DELETE_WINDOW", self._on_closing)  # Handle window close event

        # Setup main layout frames
        self.main_frame = ttk.Frame(self, padding="10 10 10 10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.setup_ui()
        self.load_appointments()

    def setup_ui(self):
        """Configures the UI elements (Booking Form and Display Treeview)."""

        # --- Frame for Booking Form (Top Half) ---
        booking_frame = ttk.LabelFrame(self.main_frame, text="Book New Appointment", padding="15")
        booking_frame.pack(fill=tk.X, pady=10)

        # Labels and Entry Fields

        # Patient Name
        ttk.Label(booking_frame, text="Patient Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_var = tk.StringVar()
        ttk.Entry(booking_frame, textvariable=self.name_var, width=40).grid(row=0, column=1, padx=5, pady=5,
                                                                            sticky="ew")

        # Date (Simple Text Input for YYYY-MM-DD)
        ttk.Label(booking_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))  # Default to today
        ttk.Entry(booking_frame, textvariable=self.date_var, width=40).grid(row=1, column=1, padx=5, pady=5,
                                                                            sticky="ew")

        # Time (Simple Text Input for HH:MM)
        ttk.Label(booking_frame, text="Time (HH:MM):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.time_var = tk.StringVar(value="09:00")
        ttk.Entry(booking_frame, textvariable=self.time_var, width=40).grid(row=2, column=1, padx=5, pady=5,
                                                                            sticky="ew")

        # Doctor Selection (Combobox)
        ttk.Label(booking_frame, text="Select Doctor:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.doctor_var = tk.StringVar(value=DOCTORS[0])
        self.doctor_combobox = ttk.Combobox(booking_frame, textvariable=self.doctor_var, values=DOCTORS, width=37,
                                            state="readonly")
        self.doctor_combobox.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        # Book Button
        ttk.Button(booking_frame, text="Book Appointment", command=self.book_appointment, style="Accent.TButton").grid(
            row=4, column=0, columnspan=2, pady=15)

        # Configure grid weights for responsive form
        booking_frame.grid_columnconfigure(1, weight=1)

        # --- Frame for Appointment List (Bottom Half) ---
        list_frame = ttk.LabelFrame(self.main_frame, text="Upcoming Appointments", padding="15")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Treeview Widget for List Display
        self.tree = ttk.Treeview(list_frame, columns=("Name", "Date", "Time", "Doctor", "Status"), show='headings')
        self.tree.heading("Name", text="Patient Name")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Time", text="Time")
        self.tree.heading("Doctor", text="Doctor")
        self.tree.heading("Status", text="Status")

        # Define column widths
        self.tree.column("Name", width=150, stretch=tk.YES)
        self.tree.column("Date", width=90, stretch=tk.NO)
        self.tree.column("Time", width=70, stretch=tk.NO)
        self.tree.column("Doctor", width=200, stretch=tk.YES)
        self.tree.column("Status", width=80, stretch=tk.NO)

        # Scrollbar for the Treeview
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Pack Treeview and Scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Apply a modern style (requires Tk 8.5+)
        style = ttk.Style()
        style.configure("TFrame", background="#f5f5f5")
        style.configure("TLabel", font=("Arial", 10))
        style.configure("TEntry", fieldbackground="white")
        style.configure("Accent.TButton", font=("Arial", 10, "bold"), background="#4CAF50", foreground="black")

    def validate_input(self, name, date_str, time_str):
        """Performs basic validation on the form input."""
        if not all([name, date_str, time_str]):
            messagebox.showerror("Input Error", "All fields are required.")
            return False

        # Validate Date format (YYYY-MM-DD)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Input Error", "Date must be in YYYY-MM-DD format.")
            return False

        # Validate Time format (HH:MM)
        try:
            datetime.strptime(time_str, "%H:%M")
        except ValueError:
            messagebox.showerror("Input Error", "Time must be in HH:MM format.")
            return False

        return True

    def book_appointment(self):
        """Called when the Book button is clicked. Handles validation and DB insertion."""
        name = self.name_var.get().strip()
        date = self.date_var.get().strip()
        time = self.time_var.get().strip()
        doctor = self.doctor_var.get()

        if self.validate_input(name, date, time):
            if self.db.insert_appointment(name, date, time, doctor):
                messagebox.showinfo("Success", f"Appointment booked for {name} with {doctor} on {date} at {time}.")
                self.load_appointments()  # Refresh the list
                self.clear_form()
            else:
                messagebox.showerror("Error", "Failed to save appointment to the database.")

    def load_appointments(self):
        """Fetches appointments from the DB and updates the Treeview display."""

        # Clear existing entries in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch and insert new entries
        appointments = self.db.fetch_appointments()
        for appointment in appointments:
            # appointment is a tuple: (name, date, time, doctor, status)
            self.tree.insert("", tk.END, values=appointment)

    def clear_form(self):
        """Resets the form fields."""
        self.name_var.set("")
        self.date_var.set(datetime.now().strftime("%Y-%m-%d"))
        self.time_var.set("09:00")
        self.doctor_var.set(DOCTORS[0])

    def _on_closing(self):
        """Clean up database connection before closing the application."""
        self.db.close()
        self.destroy()


if __name__ == "__main__":
    app = ClinicApp()
    app.mainloop()
