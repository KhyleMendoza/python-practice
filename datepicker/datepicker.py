import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
import os
import calendar

class BIRValidityChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("BIR Validity Checker")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        style = ttk.Style()
        style.theme_use('clam')
        
        main_frame = ttk.Frame(root, padding="40")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(main_frame, text="BIR Validity Checker", 
                               font=("Arial", 20, "bold"))
        title_label.pack(pady=(0, 40))
        
        start_frame = ttk.Frame(main_frame)
        start_frame.pack(fill=tk.X, pady=8)
        ttk.Label(start_frame, text="Start Date:", font=("Arial", 12, "bold")).pack(side=tk.LEFT)
        
        self.start_date_var = tk.StringVar()
        self.start_date_entry = ttk.Entry(start_frame, textvariable=self.start_date_var, 
                                         width=20, font=("Arial", 11), state="readonly")
        self.start_date_entry.pack(side=tk.LEFT, padx=(15, 10))
        self.start_date_entry.insert(0, "Click to select date")
        self.start_date_entry.bind("<Button-1>", lambda e: self.open_calendar("start"))
        
        start_btn = ttk.Button(start_frame, text="📅", 
                              command=lambda: self.open_calendar("start"))
        start_btn.pack(side=tk.LEFT)
        
        end_frame = ttk.Frame(main_frame)
        end_frame.pack(fill=tk.X, pady=8)
        ttk.Label(end_frame, text="End Date:", font=("Arial", 12, "bold")).pack(side=tk.LEFT)
        
        self.end_date_var = tk.StringVar()
        self.end_date_entry = ttk.Entry(end_frame, textvariable=self.end_date_var, 
                                       width=20, font=("Arial", 11), state="readonly")
        self.end_date_entry.pack(side=tk.LEFT, padx=(15, 10))
        self.end_date_entry.insert(0, "Click to select date")
        self.end_date_entry.bind("<Button-1>", lambda e: self.open_calendar("end"))
        
        end_btn = ttk.Button(end_frame, text="📅", 
                            command=lambda: self.open_calendar("end"))
        end_btn.pack(side=tk.LEFT)
        
        
        save_frame = ttk.Frame(main_frame)
        save_frame.pack(pady=15)
        
        submit_btn = ttk.Button(save_frame, text="💾 Save", 
                               command=self.submit_dates, style="Accent.TButton")
        submit_btn.pack()
        
        self.status_label = ttk.Label(main_frame, text="", foreground="green", font=("Arial", 10))
        self.status_label.pack(pady=8)
        
        self.save_location = r"C:\POS_BIR"
        
    def ensure_save_directory(self):
        if not os.path.exists(self.save_location):
            os.makedirs(self.save_location)
            
    def log_activity(self, start_date, end_date):
        try:
            log_file = os.path.join(self.save_location, "BIRPermitLogs.txt")
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            start_formatted = datetime.strptime(start_date, "%Y-%m-%d").strftime("%B %d, %Y")
            end_formatted = datetime.strptime(end_date, "%Y-%m-%d").strftime("%B %d, %Y")
            
            log_entry = f"[{current_time}] BIR Validity Created - Start: {start_formatted} | End: {end_formatted}\n"
            
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
                
        except Exception as e:
            pass
        
    def open_calendar(self, date_type):
        self.current_date_type = date_type
        
        cal_window = tk.Toplevel(self.root)
        cal_window.title(f"Select {date_type.title()} Date")
        cal_window.geometry("300x350")
        cal_window.resizable(False, False)
        cal_window.grab_set()
        
        cal_window.transient(self.root)
        cal_window.geometry("+%d+%d" % (
            self.root.winfo_rootx() + 100,
            self.root.winfo_rooty() + 50
        ))
        
        main_frame = ttk.Frame(cal_window, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        today = datetime.now()
        self.current_year = today.year
        self.current_month = today.month
        
        nav_frame = ttk.Frame(main_frame)
        nav_frame.pack(fill=tk.X, pady=(0, 10))
        
        prev_btn = ttk.Button(nav_frame, text="◀", width=3,
                             command=lambda: self.change_month(-1, cal_window))
        prev_btn.pack(side=tk.LEFT)
        
        self.month_year_label = ttk.Label(nav_frame, text="", font=("Arial", 12, "bold"))
        self.month_year_label.pack(side=tk.LEFT, expand=True)
        
        next_btn = ttk.Button(nav_frame, text="▶", width=3,
                             command=lambda: self.change_month(1, cal_window))
        next_btn.pack(side=tk.RIGHT)
        
        self.cal_frame = ttk.Frame(main_frame)
        self.cal_frame.pack(fill=tk.BOTH, expand=True)
        
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(btn_frame, text="Today", 
                  command=lambda: self.select_today(cal_window)).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Cancel", 
                  command=cal_window.destroy).pack(side=tk.RIGHT)
        
        self.create_calendar(cal_window)
        
    def change_month(self, direction, cal_window):
        self.current_month += direction
        if self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
        elif self.current_month < 1:
            self.current_month = 12
            self.current_year -= 1
        
        self.create_calendar(cal_window)
        
    def create_calendar(self, cal_window):
        for widget in self.cal_frame.winfo_children():
            widget.destroy()
            
        month_name = calendar.month_name[self.current_month]
        self.month_year_label.config(text=f"{month_name} {self.current_year}")
        
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            label = ttk.Label(self.cal_frame, text=day, font=("Arial", 9, "bold"))
            label.grid(row=0, column=i, padx=1, pady=1)
        
        cal_data = calendar.monthcalendar(self.current_year, self.current_month)
        
        for week_num, week in enumerate(cal_data):
            for day_num, day in enumerate(week):
                if day == 0:
                    continue
                    
                btn = ttk.Button(self.cal_frame, text=str(day), width=3,
                               command=lambda d=day: self.select_date(d, cal_window))
                btn.grid(row=week_num + 1, column=day_num, padx=1, pady=1)
                
                today = datetime.now()
                if (day == today.day and 
                    self.current_month == today.month and 
                    self.current_year == today.year):
                    btn.configure(style="Accent.TButton")
                    
    def select_date(self, day, cal_window):
        selected_date = datetime(self.current_year, self.current_month, day)
        formatted_date = selected_date.strftime("%Y-%m-%d")
        
        if self.current_date_type == "start":
            self.start_date_var.set(formatted_date)
            self.start_date_entry.delete(0, tk.END)
            self.start_date_entry.insert(0, formatted_date)
        else:
            self.end_date_var.set(formatted_date)
            self.end_date_entry.delete(0, tk.END)
            self.end_date_entry.insert(0, formatted_date)
            
        cal_window.destroy()
            
    def select_today(self, cal_window):
        today = datetime.now()
        self.select_date(today.day, cal_window)
            
    def submit_dates(self):
        start_date = self.start_date_var.get()
        end_date = self.end_date_var.get()
        
        if not start_date or start_date == "Click to select date" or not end_date or end_date == "Click to select date":
            messagebox.showerror("Error", "Please select both start and end dates.")
            return
            
        try:
            self.ensure_save_directory()
            start_formatted = self.convert_date_format(start_date)
            end_formatted = self.convert_date_format(end_date)
            
            if not start_formatted or not end_formatted:
                messagebox.showerror("Error", "Please enter dates in YYYY-MM-DD format (e.g., 2025-09-11)")
                return

            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
            date_difference = (end_date_obj - start_date_obj).days
            
            if date_difference < 0:
                messagebox.showerror("Invalid Date Range", "End date cannot be before start date.")
                return
            
            if date_difference > 14:
                messagebox.showerror("BIR Validity Error", "POS BIR validity date accepts 15 days validity only.")
                return
            
            notepad_file = os.path.join(self.save_location, "ReferenceValidityDate.txt")
            
            dates_to_save = [start_formatted, end_formatted]
            dates_to_save.sort()
            
            with open(notepad_file, 'w') as f:
                for date in dates_to_save:
                    f.write(date + '\n')
            
            self.log_activity(start_date, end_date)
            start_display = datetime.strptime(start_date, "%Y-%m-%d").strftime("%B %d, %Y")
            end_display = datetime.strptime(end_date, "%Y-%m-%d").strftime("%B %d, %Y")
            
            self.status_label.config(text=f"✅ Saved {len(dates_to_save)} date(s) to {notepad_file}")
            messagebox.showinfo("Success", f"Successfully saved validity dates:\n\nStart Date: {start_display}\nEnd Date: {end_display}\n\nSaved to: {notepad_file}")
            
            self.start_date_var.set("")
            self.end_date_var.set("")
            self.start_date_entry.delete(0, tk.END)
            self.start_date_entry.insert(0, "Click to select date")
            self.end_date_entry.delete(0, tk.END)
            self.end_date_entry.insert(0, "Click to select date")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save dates: {str(e)}")
            
    def convert_date_format(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj.strftime("%Y%m%d")
        except ValueError:
            return None
            

def main():
    root = tk.Tk()
    app = BIRValidityChecker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
