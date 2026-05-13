# Data Science Journey - Week 02: Pipeline Robustness & Numeric Foundations

This folder documents my daily progress during the second week of my Data Science transition. The curriculum evolved from basic file handling and numerical operations to building resilient data pipelines.

## 🎯 Weekly Goals
- **Data I/O & Robustness:** Advancing from simple file reading to error-proof data ingestion.
- **Data Cleaning:** Implementing logic to handle missing or corrupted data in real-world scenarios.
- **Numeric Foundations:** Utilizing **NumPy** for statistical analysis and performance-optimized operations.

## 📂 Daily Exercises

### Day 1: Foundations of Ingestion and NumPy
- **Exercise 01: CSV Reader with DictReader (`exercicio1.py`)**  
  A practical introduction to the `csv` module, focusing on reading sales data using dictionaries and basic data type conversion with basic error skipping.
- **Exercise 02: Basic Temperature Analysis (`exercicio2.py`)**  
  My first steps with **NumPy**, focusing on calculating Mean, Median, and Standard Deviation, plus using **Boolean Masks** to filter data above the average.

### Day 2: Advanced Robustness and Data Cleaning
- **Exercise 03: The "Bulletproof" CSV Reader (`exercicio3.py`)**  
  A major upgrade in error handling. This script manages system-level errors (`FileNotFoundError`) and granular data errors (`ValueError`) using nested try/except blocks to ensure the pipeline never crashes.
- **Exercise 04: Professional Data Cleaning Function (`exercicio4.py`)**  
  A robust function designed to handle "dirty" datasets. It filters out `None` values, empty strings, and non-numeric noise, returning a comprehensive statistical report of the valid data.

### Day 3: Logic and Data Manipulation

  During this week, I focused on building resilient data pipelines and mastering numerical operations using NumPy.

#### Exercise 05: Sensor Data Validator (`exercicio5.py`)
- **Objective:** Clean and process raw sensor data that may contain noise or invalid entries.
- **Key Concepts:** Implementation of `try-except` blocks for error handling, data type conversion, and basic statistical aggregation.
- **Goal:** Ensure the pipeline remains operational even when encountering non-numeric values (e.g., "ERROR", "None").

#### Exercise 06: Data Normalization with NumPy (`exercicio6.py`)
- **Objective:** Apply Min-Max scaling to a randomly generated dataset.
- **Key Concepts:** NumPy vectorization, array manipulation, and defensive programming to prevent division by zero.
- **Goal:** Transform raw values into a normalized range [0, 1], a critical step for preparing data for machine learning models.

## 🛠️ Tech Stack
- **Python 3.13.1**
- **NumPy**
- **VS Code & Git Bash**

## 🚀 Key Takeaways
This week, I learned that real-world data is rarely clean. Building a successful pipeline requires more than just logic; it requires **resilience** and **preparation for the unexpected**.

---
*Developed by Nate Angelim as part of a 5-month Data Science transition plan.*

