# Calculate-BMI
BMI Calculator with History (Tkinter + Matplotlib)
📌 Project Overview

This project is a BMI (Body Mass Index) Calculator built with Python Tkinter for GUI and Matplotlib for data visualization.
It allows users to:

Enter their username, weight, and height.

Calculate their BMI and see the category (Underweight, Normal, Overweight, Obese).

Save BMI records in a CSV file (bmi_data.csv).

View their BMI trend graph over multiple entries.

🚀 Features

User-friendly Graphical User Interface (GUI).

BMI classification based on WHO standards:

Underweight (<18.5)

Normal (18.5–24.9)

Overweight (25–29.9)

Obese (30 and above)

Data persistence using CSV files.

Graph visualization with Matplotlib (trend of BMI values per user).

Error handling for invalid or empty inputs.

🛠️ Technologies Used

Python 3.x

Tkinter – for GUI

Matplotlib – for plotting BMI history

CSV module – for storing user data

📂 Project Structure
BMI-Calculator/
│
├── bmi_calculator.py     # Main application code
├── bmi_data.csv          # User BMI records (auto-generated after first entry)
├── README.md             # Project documentation (this file)

📊 How It Works

User enters:

Username

Weight (kg)

Height (m)

Clicks Calculate BMI → BMI value & category are displayed.

The BMI result is stored in bmi_data.csv.

Clicking Show Graph plots the user’s BMI trend across all saved entries.

📷 Screenshots

(You can add screenshots of your GUI here once you run the program and save them.)

▶️ How to Run

Clone the repository:

git clone https://github.com/your-username/BMI-Calculator.git
cd BMI-Calculator


Install dependencies (Matplotlib required):

pip install matplotlib


Run the application:

python bmi_calculator.py

📈 Example Output

BMI Result Example:

BMI: 22.15 (Normal weight)


Graph Example:
Line chart showing user’s BMI trend across multiple entries.

✅ Future Improvements

Add date/time stamps for BMI entries.

Support multiple users with selection menu.

Add export to PDF/Excel option.

Create an installer/executable for easier use.

👨‍💻 Author

Your name

GitHub: jarupulaprudhvi
