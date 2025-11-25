# 5.2 Statement.md

## Problem Statement
Managing clinic appointments manually using registers, diaries, or spreadsheets often leads to errors such as double-booking, missing entries, and difficulty tracking patient schedules. Small clinics need a simple, efficient, and user-friendly system to streamline appointment scheduling, avoid conflicts, and maintain accurate patient records.

---

## Scope of the Project
This project focuses on creating a desktop-based Clinic Appointment Scheduler using Python, Tkinter, and SQLite.  
The scope includes:

- Booking new appointments  
- Storing appointment details in a secure database  
- Preventing overlapping appointments  
- Viewing and managing upcoming appointments  
- Canceling or exporting appointment data  
- A GUI designed for ease of use by clinic staff  

The project does **not** include:
- Online booking  
- Multi-branch clinic management  
- Advanced analytics or automated reminders (can be added in upgrades)

---

## Target Users
- Small and medium clinics  
- Clinic receptionists and administrative staff  
- Doctors who manage their own small practice  
- Medical assistants responsible for scheduling patient visits  

---

## High-Level Features
- **GUI-Based Appointment Booking:** User-friendly Tkinter interface to add appointments quickly.  
- **Input Validation:** Ensures correct date, time, and avoids missing fields.  
- **Doctor Selection:** Appointments assigned to specific doctors.  
- **Avoids Double Booking:** Automatically checks and prevents time conflicts.  
- **Upcoming Appointments View:** Displays all scheduled appointments in a table.  
- **Appointment Cancellation:** Allows removing selected appointments.  
- **CSV Export:** Saves appointment data for reporting or backup.  
- **SQLite Storage:** Lightweight and persistent backend database.  

