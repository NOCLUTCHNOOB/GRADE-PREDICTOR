import customtkinter as ctk
import pickle
import numpy as np
from tkinter import messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class StudentPredictorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        try:
            with open("studentmodel.pickle", "rb") as f:
                self.model = pickle.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "studentmodel.pickle not found!")
            self.destroy()

        self.title("GRADE PREDICTOR")
        self.geometry("1000x800")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(self.sidebar, text="GRADE PREDICTOR", font=("Roboto", 20, "bold")).pack(pady=30)

        self.main_frame = ctk.CTkScrollableFrame(self, corner_radius=15)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.inputs = {}
        self.value_labels = {}
        self.setup_ui()

    def setup_ui(self):
        self.add_section("1. ACADEMIC PERFORMANCE")
        self.inputs['g1'] = self.add_entry("Mini Test Score (G1):", "e.g. 8/10", "Enter your score and total (Format: Marks/Total).")
        self.inputs['g2'] = self.add_entry("Mid Test Score (G2):", "e.g. 16.5/20", "Enter your score and total (Format: Marks/Total).")
        self.inputs['final_total'] = self.add_entry("Final Exam Total Marks:", "60", "What is the total marks of the exam you are predicting for?")

        self.add_section("2. DAILY HABITS")
        self.inputs['study'] = self.add_slider("Weekly Study Time", 1, 4, 2, 
            "1: <2h, 2: 2-5h, 3: 5-10h, 4: >10h")
        self.inputs['age'] = self.add_entry("Age:", "19", "Enter your current age.")
        self.inputs['travel'] = self.add_slider("Daily Commute", 1, 4, 1, 
            "1: <15m, 2: 15-30m, 3: 30-60m, 4: >1h")
        self.inputs['failures'] = self.add_entry("Past Failures:", "0", 
            "0: None, 1: One, 2: Two, 3: Three or more subjects repeated.")

        self.add_section("3. SOCIAL & HEALTH")
        self.inputs['freetime'] = self.add_slider("Free Time After School", 1, 5, 3, 
            "1: Very Low to 5: Very High amount of leisure time.")
        self.inputs['goout'] = self.add_slider("Time with Friends", 1, 5, 2, 
            "1: Isolated to 5: Out with friends almost every day.")
        self.inputs['dalc'] = self.add_slider("Workday Alcohol", 1, 5, 1, 
            "1: Never/Rare to 5: Very High (Monday-Friday).")
        self.inputs['walc'] = self.add_slider("Weekend Alcohol", 1, 5, 1, 
            "1: Never/Rare to 5: Very High (Sat-Sun).")
        self.inputs['health'] = self.add_slider("Health Status", 1, 5, 5, 
            "1: Very Poor to 5: Very Good current physical health.")
        self.inputs['absences'] = self.add_entry("Total Absences:", "0", "Total number of school days missed this semester.")

        self.btn = ctk.CTkButton(self.main_frame, text="CALCULATE PREDICTION", height=60, 
                                 command=self.predict_logic, font=("Roboto", 18, "bold"))
        self.btn.pack(pady=40, padx=100, fill="x")

        self.res_lbl = ctk.CTkLabel(self.main_frame, text="Prediction: --", font=("Roboto", 24, "bold"))
        self.res_lbl.pack(pady=20)

    def add_section(self, text):
        ctk.CTkLabel(self.main_frame, text=text, text_color="LIGHT BLUE", font=("Roboto", 14, "bold")).pack(anchor="w", padx=40, pady=(30,5))

    def add_entry(self, label, placeholder, explanation):
        ctk.CTkLabel(self.main_frame, text=label, font=("Roboto", 13, "bold")).pack(anchor="w", padx=45)
        ctk.CTkLabel(self.main_frame, text=explanation, font=("Roboto", 11), text_color="gray").pack(anchor="w", padx=45)
        e = ctk.CTkEntry(self.main_frame, placeholder_text=placeholder, width=400)
        e.pack(pady=(5, 15))
        return e

    def add_slider(self, label, start, end, default, explanation):
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=45)
        
        ctk.CTkLabel(header_frame, text=label, font=("Roboto", 13, "bold")).pack(side="left")
        
        val_lbl = ctk.CTkLabel(header_frame, text=f"Selected: {default}", text_color="LIGHT BLUE", font=("Roboto", 13, "bold"))
        val_lbl.pack(side="right")
        
        ctk.CTkLabel(self.main_frame, text=explanation, font=("Roboto", 11), text_color="gray").pack(anchor="w", padx=45)
        
        s = ctk.CTkSlider(self.main_frame, from_=start, to=end, number_of_steps=end-start, width=400,
                          command=lambda v, l=val_lbl: l.configure(text=f"Selected: {int(v)}"))
        s.set(default)
        s.pack(pady=(5, 15))
        return s

    def parse_marks(self, val):
        if "/" in val:
            parts = val.split("/")
            return (float(parts[0]) / float(parts[1])) * 20
        return float(val)

    def predict_logic(self):
        try:
            final_total = float(self.inputs['final_total'].get())
            data_row = [
                self.parse_marks(self.inputs['g1'].get()),
                self.parse_marks(self.inputs['g2'].get()),
                int(self.inputs['study'].get()),
                float(self.inputs['age'].get()),
                int(self.inputs['travel'].get()),
                float(self.inputs['failures'].get()),
                int(self.inputs['freetime'].get()),
                int(self.inputs['goout'].get()),
                int(self.inputs['dalc'].get()),
                int(self.inputs['walc'].get()),
                int(self.inputs['health'].get()),
                float(self.inputs['absences'].get())
            ]
            pred_20 = self.model.predict(np.array([data_row]))[0]
            pred_20 = min(20, max(0, pred_20))
            final_result = (pred_20 / 20) * final_total
            self.res_lbl.configure(text=f"Prediction: {final_result:.2f} / {final_total}", text_color="GREEN")
        except Exception:
            messagebox.showerror("Input Error", "Please ensure all fields are filled correctly (e.g., 8/10 for marks).")

if __name__ == "__main__":
    app = StudentPredictorApp()
    app.mainloop()