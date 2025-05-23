# Online-Education-Analysis
# 🎓 Online Education Platform - Student Performance Analysis

This project analyzes student performance data from an online education platform using **Python (Pandas, NumPy, Matplotlib)** and **Power BI**. It provides insights into course completion rates, session activity, and top performers.

---

## 📁 Dataset Overview

The project uses the following CSV files:

| File Name        | Description                                      |
|------------------|--------------------------------------------------|
| `students.csv`   | Contains student ID, name, gender, age, country |
| `courses.csv`    | Details about available courses                 |
| `enrollments.csv`| Links students to courses, scores, and status  |
| `sessions.csv`   | Session-level data including duration and dates |

---

## ⚙️ Tools Used

- **Python** (Pandas, NumPy, Matplotlib) for data cleaning and processing
- **Power BI** for interactive data visualization
- **Git** & **GitHub** for version control and collaboration

---

## 🧪 Key Features & Analysis

- Cleaned and merged datasets using Python
- Handled missing values and created score bands (`High`, `Medium`, `Low`)
- Aggregated session data: total sessions, duration, average time
- Calculated:
  - 🎯 Course completion rates
  - 🌍 Country-wise success rate
  - ⏱ Top 10 active students by learning duration
- Exported CSVs to Power BI for visualization

---

## 📷 Power BI Dashboards (Screenshots)

### ⏱ Top 10 Active Students by Learning Duration
![Top Active Students](images/Screenshot_Chart2.png.png)

### 🎯 Course Completion Rates
![Course Completion](images/Screenshot_Chart1.png.png)

> Make sure your screenshots are placed in a folder named `screenshots/` inside your repo.

---

## 🧰 Installation & Usage

### 🐍 Python Side

1. Clone the repository:
   ```bash
   git clone https://github.com/mehtaricha-23/Online-Education-Analysis.git
   cd Online-Education-Analysis
