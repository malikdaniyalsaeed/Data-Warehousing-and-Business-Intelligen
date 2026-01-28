# GPA & CGPA Calculator

A desktop application built with Python Tkinter for calculating GPA and CGPA.

## Features

- **GPA Calculator**: Calculate GPA for 4 courses (DS, AI, DB, IS)
  - Input marks and credit hours for each course
  - Automatic grade point conversion based on marks
  
- **CGPA Calculator**: Calculate cumulative GPA
  - Input previous GPA and credit hours
  - Input current semester GPA and credit hours
  - Get combined CGPA

## Grade Point Scale

| Marks Range | Grade Points |
|-------------|--------------|
| 85-100      | 4.0          |
| 80-84       | 3.7          |
| 75-79       | 3.3          |
| 70-74       | 3.0          |
| 65-69       | 2.7          |
| 60-64       | 2.3          |
| 55-59       | 2.0          |
| 50-54       | 1.7          |
| Below 50    | 0.0          |

## How to Run

### Method 1: Using the Batch File (Windows)
Simply double-click `run.bat`

### Method 2: Using Python Directly
```bash
python gpa_calculator.py
```

## Requirements

- Python 3.x (Tkinter is included with Python)
- No additional packages required

## Creating an Executable (Optional)

To create a standalone .exe file that can run without Python installed:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Create the executable:
   ```bash
   pyinstaller --onefile --windowed gpa_calculator.py
   ```

3. Find your executable in the `dist` folder

## Usage

1. **For GPA Calculation**:
   - Enter credit hours for each course (DS, AI, DB, IS)
   - Enter marks obtained for each course
   - Click "Calculate GPA"
   - View your GPA result

2. **For CGPA Calculation**:
   - Enter your previous GPA and total credit hours
   - Enter your current semester GPA and credit hours
   - Click "Calculate CGPA"
   - View your CGPA result
