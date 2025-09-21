import tkinter as tk  # Import main tkinter library for GUI creation
from tkinter import ttk, messagebox  # Import themed widgets and message dialog boxes
from datetime import datetime, date  # Import date and time handling classes
import os  # Import operating system interface for file operations
import calendar  # Import calendar module for calendar display functionality

class BIRValidityChecker:  # Define main application class for BIR validity checking
    def __init__(self, root):  # Constructor method that takes root window as parameter
        self.root = root  # Store reference to the main window
        self.root.title("BIR Validity Checker")  # Set window title text
        self.root.geometry("500x400")  # Set window size to 500 pixels wide by 400 pixels tall
        self.root.resizable(False, False)  # Disable window resizing in both directions
        
        style = ttk.Style()  # Create style object for widget theming
        style.theme_use('clam')  # Apply the 'clam' theme for modern appearance
        
        main_frame = ttk.Frame(root, padding="40")  # Create main container frame with 40px padding on all sides
        main_frame.pack(fill=tk.BOTH, expand=True)  # Pack frame to fill entire window and expand with window
        
        title_label = ttk.Label(main_frame, text="BIR Validity Checker",   # Create title label with text
                               font=("Arial", 20, "bold"))  # Set font to Arial, 20pt, bold
        title_label.pack(pady=(0, 40))  # Pack label with 40px bottom margin
        
        start_frame = ttk.Frame(main_frame)  # Create frame container for start date controls
        start_frame.pack(fill=tk.X, pady=8)  # Pack frame to fill width with 8px vertical margin
        ttk.Label(start_frame, text="Start Date:", font=("Arial", 12, "bold")).pack(side=tk.LEFT)  # Create and pack start date label on left side
        
        self.start_date_var = tk.StringVar()  # Create string variable to hold start date value
        self.start_date_entry = ttk.Entry(start_frame, textvariable=self.start_date_var,   # Create entry widget bound to string variable
                                         width=20, font=("Arial", 11), state="readonly")  # Set width, font, and read-only state
        self.start_date_entry.pack(side=tk.LEFT, padx=(15, 10))  # Pack entry on left with specific horizontal padding
        self.start_date_entry.insert(0, "Click to select date")  # Insert placeholder text at position 0
        self.start_date_entry.bind("<Button-1>", lambda e: self.open_calendar("start"))  # Bind left mouse click to open calendar
        
        start_btn = ttk.Button(start_frame, text="📅",   # Create button with calendar emoji
                              command=lambda: self.open_calendar("start"))  # Set command to open start date calendar
        start_btn.pack(side=tk.LEFT)  # Pack button on left side of frame
        
        end_frame = ttk.Frame(main_frame)  # Create frame container for end date controls
        end_frame.pack(fill=tk.X, pady=8)  # Pack frame to fill width with 8px vertical margin
        ttk.Label(end_frame, text="End Date:", font=("Arial", 12, "bold")).pack(side=tk.LEFT)  # Create and pack end date label on left side
        
        self.end_date_var = tk.StringVar()  # Create string variable to hold end date value
        self.end_date_entry = ttk.Entry(end_frame, textvariable=self.end_date_var,   # Create entry widget bound to string variable
                                       width=20, font=("Arial", 11), state="readonly")  # Set width, font, and read-only state
        self.end_date_entry.pack(side=tk.LEFT, padx=(15, 10))  # Pack entry on left with specific horizontal padding
        self.end_date_entry.insert(0, "Click to select date")  # Insert placeholder text at position 0
        self.end_date_entry.bind("<Button-1>", lambda e: self.open_calendar("end"))  # Bind left mouse click to open calendar
        
        end_btn = ttk.Button(end_frame, text="📅",   # Create button with calendar emoji
                            command=lambda: self.open_calendar("end"))  # Set command to open end date calendar
        end_btn.pack(side=tk.LEFT)  # Pack button on left side of frame
        
        
        save_frame = ttk.Frame(main_frame)  # Create frame container for save button
        save_frame.pack(pady=15)  # Pack frame with 15px vertical margin
        
        submit_btn = ttk.Button(save_frame, text="💾 Save",   # Create save button with floppy disk emoji
                               command=self.submit_dates, style="Accent.TButton")  # Set command and apply accent styling
        submit_btn.pack()  # Pack button in center of frame
        
        self.status_label = ttk.Label(main_frame, text="", foreground="green", font=("Arial", 10))  # Create status label with green text
        self.status_label.pack(pady=8)  # Pack label with 8px vertical margin
        
        self.save_location = r"C:\POS_BIR"  # Set default directory path for saving files
        
    def ensure_save_directory(self):  # Method to ensure the save directory exists
        if not os.path.exists(self.save_location):  # Check if directory doesn't exist
            os.makedirs(self.save_location)  # Create directory and any necessary parent directories
            
    def log_activity(self, start_date, end_date):  # Method to log activity to a text file
        try:  # Begin try block for error handling
            log_file = os.path.join(self.save_location, "BIRPermitLogs.txt")  # Create full path to log file
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp formatted as string
            
            start_formatted = datetime.strptime(start_date, "%Y-%m-%d").strftime("%B %d, %Y")  # Convert start date to readable format
            end_formatted = datetime.strptime(end_date, "%Y-%m-%d").strftime("%B %d, %Y")  # Convert end date to readable format
            
            log_entry = f"[{current_time}] BIR Validity Created - Start: {start_formatted} | End: {end_formatted}\n"  # Create formatted log entry string
            
            with open(log_file, 'a', encoding='utf-8') as f:  # Open log file in append mode with UTF-8 encoding
                f.write(log_entry)  # Write log entry to file
                
        except Exception as e:  # Catch any exceptions that occur
            pass  # Silently ignore errors (continue execution)
        
    def open_calendar(self, date_type):  # Method to open calendar popup window
        self.current_date_type = date_type  # Store which date type is being selected (start or end)
        
        cal_window = tk.Toplevel(self.root)  # Create new popup window as child of main window
        cal_window.title(f"Select {date_type.title()} Date")  # Set window title with capitalized date type
        cal_window.geometry("300x350")  # Set popup window size
        cal_window.resizable(False, False)  # Disable resizing of popup window
        cal_window.grab_set()  # Make window modal (blocks interaction with parent)
        
        cal_window.transient(self.root)  # Make window stay on top of parent
        cal_window.geometry("+%d+%d" % (  # Set window position relative to parent
            self.root.winfo_rootx() + 100,  # Horizontal offset from parent window
            self.root.winfo_rooty() + 50  # Vertical offset from parent window
        ))  # Close geometry positioning
        
        main_frame = ttk.Frame(cal_window, padding="15")  # Create main frame for calendar with 15px padding
        main_frame.pack(fill=tk.BOTH, expand=True)  # Pack frame to fill entire popup window
        
        today = datetime.now()  # Get current date and time
        self.current_year = today.year  # Set current year for calendar display
        self.current_month = today.month  # Set current month for calendar display
        
        nav_frame = ttk.Frame(main_frame)  # Create frame for navigation controls
        nav_frame.pack(fill=tk.X, pady=(0, 10))  # Pack frame to fill width with bottom margin
        
        prev_btn = ttk.Button(nav_frame, text="◀", width=3,  # Create previous month button with left arrow
                             command=lambda: self.change_month(-1, cal_window))  # Set command to go back one month
        prev_btn.pack(side=tk.LEFT)  # Pack button on left side
        
        self.month_year_label = ttk.Label(nav_frame, text="", font=("Arial", 12, "bold"))  # Create label for month/year display
        self.month_year_label.pack(side=tk.LEFT, expand=True)  # Pack label in center with expansion
        
        next_btn = ttk.Button(nav_frame, text="▶", width=3,  # Create next month button with right arrow
                             command=lambda: self.change_month(1, cal_window))  # Set command to go forward one month
        next_btn.pack(side=tk.RIGHT)  # Pack button on right side
        
        self.cal_frame = ttk.Frame(main_frame)  # Create frame to hold calendar grid
        self.cal_frame.pack(fill=tk.BOTH, expand=True)  # Pack frame to fill remaining space
        
        btn_frame = ttk.Frame(main_frame)  # Create frame for action buttons
        btn_frame.pack(fill=tk.X, pady=(10, 0))  # Pack frame to fill width with top margin
        
        ttk.Button(btn_frame, text="Today",   # Create "Today" button
                  command=lambda: self.select_today(cal_window)).pack(side=tk.LEFT, padx=(0, 5))  # Pack on left with right padding
        ttk.Button(btn_frame, text="Cancel",   # Create "Cancel" button
                  command=cal_window.destroy).pack(side=tk.RIGHT)  # Pack on right, command destroys window
        
        self.create_calendar(cal_window)  # Call method to populate calendar with dates
        
    def change_month(self, direction, cal_window):  # Method to change displayed month
        self.current_month += direction  # Add direction value (-1 or +1) to current month
        if self.current_month > 12:  # Check if month exceeded December
            self.current_month = 1  # Reset to January
            self.current_year += 1  # Increment year
        elif self.current_month < 1:  # Check if month went before January
            self.current_month = 12  # Reset to December
            self.current_year -= 1  # Decrement year
        
        self.create_calendar(cal_window)  # Recreate calendar display with new month/year
        
    def create_calendar(self, cal_window):  # Method to create and display calendar grid
        for widget in self.cal_frame.winfo_children():  # Loop through all existing widgets in calendar frame
            widget.destroy()  # Destroy each widget to clear calendar
            
        month_name = calendar.month_name[self.current_month]  # Get full month name from month number
        self.month_year_label.config(text=f"{month_name} {self.current_year}")  # Update month/year label text
        
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]  # Define day abbreviations for header
        for i, day in enumerate(days):  # Loop through day names with index
            label = ttk.Label(self.cal_frame, text=day, font=("Arial", 9, "bold"))  # Create day header label
            label.grid(row=0, column=i, padx=1, pady=1)  # Place label in grid at row 0, column i
        
        cal_data = calendar.monthcalendar(self.current_year, self.current_month)  # Get calendar data as list of weeks
        
        for week_num, week in enumerate(cal_data):  # Loop through weeks with index
            for day_num, day in enumerate(week):  # Loop through days in week with index
                if day == 0:  # Check if day is 0 (empty cell for previous/next month)
                    continue  # Skip to next iteration
                    
                btn = ttk.Button(self.cal_frame, text=str(day), width=3,  # Create button for each day
                               command=lambda d=day: self.select_date(d, cal_window))  # Set command to select this date
                btn.grid(row=week_num + 1, column=day_num, padx=1, pady=1)  # Place button in grid
                
                today = datetime.now()  # Get current date for highlighting
                if (day == today.day and   # Check if this day matches today's day
                    self.current_month == today.month and   # And month matches today's month
                    self.current_year == today.year):  # And year matches today's year
                    btn.configure(style="Accent.TButton")  # Apply accent styling to highlight today
                    
    def select_date(self, day, cal_window):  # Method to handle date selection
        selected_date = datetime(self.current_year, self.current_month, day)  # Create datetime object for selected date
        formatted_date = selected_date.strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD string
        
        if self.current_date_type == "start":  # Check if selecting start date
            self.start_date_var.set(formatted_date)  # Set start date variable
            self.start_date_entry.delete(0, tk.END)  # Clear start date entry field
            self.start_date_entry.insert(0, formatted_date)  # Insert formatted date into entry
        else:  # Otherwise selecting end date
            self.end_date_var.set(formatted_date)  # Set end date variable
            self.end_date_entry.delete(0, tk.END)  # Clear end date entry field
            self.end_date_entry.insert(0, formatted_date)  # Insert formatted date into entry
            
        cal_window.destroy()  # Close calendar popup window
            
    def select_today(self, cal_window):  # Method to quickly select today's date
        today = datetime.now()  # Get current date and time
        self.select_date(today.day, cal_window)  # Call select_date with today's day number
            
    def submit_dates(self):  # Method to validate and save selected dates
        start_date = self.start_date_var.get()  # Get start date from string variable
        end_date = self.end_date_var.get()  # Get end date from string variable
        
        if not start_date or start_date == "Click to select date" or not end_date or end_date == "Click to select date":  # Check if dates are missing or placeholder
            messagebox.showerror("Error", "Please select both start and end dates.")  # Show error message
            return  # Exit method early
            
        try:  # Begin try block for error handling
            self.ensure_save_directory()  # Ensure save directory exists
            start_formatted = self.convert_date_format(start_date)  # Convert start date to YYYYMMDD format
            end_formatted = self.convert_date_format(end_date)  # Convert end date to YYYYMMDD format
            
            if not start_formatted or not end_formatted:  # Check if date conversion failed
                messagebox.showerror("Error", "Please enter dates in YYYY-MM-DD format (e.g., 2025-09-11)")  # Show format error
                return  # Exit method early

            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")  # Parse start date string to datetime object
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")  # Parse end date string to datetime object
            today = datetime.now().date()  # Get today's date for comparison
            
            date_difference = (end_date_obj - start_date_obj).days  # Calculate difference in days between dates
            
            if date_difference < 0:  # Check if end date is before start date
                messagebox.showerror("Invalid Date Range", "End date cannot be before start date.")  # Show error message
                return  # Exit method early
            
            if date_difference > 14:  # Check if date range exceeds 14 days (15-day limit)
                messagebox.showerror("BIR Validity Error", "POS BIR validity date accepts 15 days validity only.")  # Show BIR-specific error
                return  # Exit method early
            
            if end_date_obj.date() < today:  # Check if end date is in the past
                messagebox.showerror("Date Out of Range", "Date Out of Range")  # Show error message
                return  # Exit method early
            
            notepad_file = os.path.join(self.save_location, "ReferenceValidityDate.txt")  # Create full path to output file
            
            dates_to_save = [start_formatted, end_formatted]  # Create list of formatted dates
            dates_to_save.sort()  # Sort dates in chronological order
            
            with open(notepad_file, 'w') as f:  # Open file in write mode (overwrites existing content)
                for date in dates_to_save:  # Loop through dates to save
                    f.write(date + '\n')  # Write each date on a new line
            
            self.log_activity(start_date, end_date)  # Log this activity to the log file
            start_display = datetime.strptime(start_date, "%Y-%m-%d").strftime("%B %d, %Y")  # Format start date for display
            end_display = datetime.strptime(end_date, "%Y-%m-%d").strftime("%B %d, %Y")  # Format end date for display
            
            self.status_label.config(text=f"✅ Saved {len(dates_to_save)} date(s) to {notepad_file}")  # Update status label
            messagebox.showinfo("Success", f"Successfully saved validity dates:\n\nStart Date: {start_display}\nEnd Date: {end_display}\n\nSaved to: {notepad_file}")  # Show success message
            
            self.start_date_var.set("")  # Clear start date variable
            self.end_date_var.set("")  # Clear end date variable
            self.start_date_entry.delete(0, tk.END)  # Clear start date entry field
            self.start_date_entry.insert(0, "Click to select date")  # Reset start date placeholder text
            self.end_date_entry.delete(0, tk.END)  # Clear end date entry field
            self.end_date_entry.insert(0, "Click to select date")  # Reset end date placeholder text
            
        except Exception as e:  # Catch any exceptions that occur during save process
            messagebox.showerror("Error", f"Failed to save dates: {str(e)}")  # Show error message with exception details
            
    def convert_date_format(self, date_str):  # Method to convert date from YYYY-MM-DD to YYYYMMDD format
        try:  # Begin try block for error handling
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")  # Parse date string to datetime object
            return date_obj.strftime("%Y%m%d")  # Return date formatted as YYYYMMDD string
        except ValueError:  # Catch value error if date parsing fails
            return None  # Return None to indicate conversion failure
            

def main():  # Main function to start the application
    root = tk.Tk()  # Create root tkinter window
    app = BIRValidityChecker(root)  # Create instance of BIR validity checker application
    root.mainloop()  # Start GUI event loop to keep window open and responsive

if __name__ == "__main__":  # Check if script is being run directly (not imported)
    main()  # Call main function to start application