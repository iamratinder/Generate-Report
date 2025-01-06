


# 📋 CSV Profiling Report Generator

## Introduction 
This is a web application that generates a profiling report for a CSV file using the **Pandas Profiling** library. The application allows users to upload a CSV file and receive a detailed profiling report that summarizes the data, including statistics and visualizations.

## Features ✅
- **CSV Upload**: Users can upload their CSV files.
- **Data Profiling**: Generates a comprehensive profiling report using Pandas Profiling.
- **HTML Report**: The profiling report is rendered as an HTML page for easy viewing.
- **User-Friendly Interface**: Simple and intuitive web interface built with HTML and CSS.

## Tech Stack used 🛠️

- Python 
- Flask
- Pandas
- ydata-profiling (formerly Pandas Profiling)
- HTML/CSS

## Directory Structure 📁
```
Directory structure:
└── iamratinder-Generate-Report/
    ├── app.py
    ├── main.py
    ├── requirements.txt
    ├── static/
    │   ├── style.css
    │   └── style2.css
    └── templates/
        ├── index.html
        └── report.html
```

## Demo Video

https://github.com/user-attachments/assets/2c08b4f9-02f9-415b-b546-990166b068c6

## Installation (to run on your machine)

1. Clone the repository:
```
git clone https://github.com/iamratinder/Generate-Report.git
cd Generate-Report
```

2. Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:
```
pip install -r requrements.txt
```
4. Run the Application (make sure you are in virtual environment)
```
python app.py
```
5. Open your web browser and navigate to `http://127.0.0.1:5000/`.
6. Upload the file and enjoy 😉✌🏻
