# GRADE-PREDICTOR
PREDICTS YOUR GRADE BY TAKING YOUR PREVIOUS GRADES AND DAILY HABITS AS INPUT


# GRADE PREDICTOR
A high-performance machine learning application designed to forecast student academic outcomes. By leveraging historical data and lifestyle metrics, this tool provides students and educators with data-driven insights into potential final grades (G3).
The system achieves a 93% accuracy (R^2 score) by utilizing a supervised learning approach (Linear Regression) to map the relationship between mid-term performance and final results.

# Core Features
Dual-Interface System: * GUI Dashboard: A sleek, dark-themed interface built with CustomTkinter featuring live slider feedback and dynamic value tracking.

CLI Utility: A lightweight terminal-based script for rapid data entry and prediction.
Flexible Input Parsing: Accepts custom grade formats (e.g., 8/10, 15/20) and automatically normalizes them to the model's 20-point scale.

Custom Output Scaling: Predicts results based on any user-defined final exam total (e.g., 60, 100, or 75 marks).

Multi-Factor Analysis: Analyzes 12 distinct features including academic history, study habits, and social-environmental factors.

# Technical Architecture
Model: Linear Regression (Scikit-Learn)

Data Processing: Pandas & NumPy

GUI Framework: CustomTkinter (Modernized Tkinter wrapper)

Persistence: Pickle (for model serialization)

# Repository Structure
Predictor.py: The training engine. It iterates 30 times to find and save the most accurate model weights.

GUIBASED.py: The main graphical application.

TEXTBASED.py: The command-line version of the tool.

student-mat.csv: The source dataset (UCI Student Performance).

studentmodel.pickle: The pre-trained weights for the Linear Regression model.

# Setup & Usage
1. Requirements
Ensure you have Python 3.8+ installed. Install the necessary dependencies via pip:
pip install pandas numpy scikit-learn customtkinter

2. Training
To retrain the model on the provided dataset:
python Predictor.py

3. Execution
To launch the graphical dashboard:
python GUIBASED.py

To use the terminal version:
python TEXTBASED.py

# Feature Set
The predictor evaluates the following 12 attributes:

G1 & G2: Previous midterm scores.

Study Time: Weekly hours spent studying.

Failures: Number of previous class failures.

Absences: Total number of school absences.

Age: Student's current age.

Travel Time: Duration of daily commute.

Social/Lifestyle: Free time, frequency of going out, and alcohol consumption (Workday/Weekend).

Health: Self-reported current health status.

# Author
YASH DEV
CSE-AI Student | IIIT Bhopal | BATCH-2029