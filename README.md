# 🧮 GUI-Based Calculator with History (Python + MySQL)

This repository contains a graphical calculator application built using **Tkinter** and **CustomTkinter** with **MySQL integration**.  
It performs basic arithmetic operations (addition, subtraction, multiplication, division) and stores all calculations in a database with a viewable history.

---

## 📸 Features

- 🧠 Basic Operations: `+`, `-`, `×`, `÷`
- 🗃️ History: Saves results in separate MySQL tables
- 👁️ View History: Displays past calculations (per operation)
- 🧹 Clear History: Truncates all stored records
- 💾 MySQL integration for persistent logging
- 📦 Simple and modern GUI with `CustomTkinter`

---

## 🧰 Requirements

- Python 3.6+
- MySQL Server
- Required Python packages:
  ```bash
  pip install customtkinter mysql-connector-python
  ```

---

## 🛠️ Setup & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/alifjobaer12/Normal_Calculator.git
   cd Normal_Calculator
   ```

2. **Create MySQL Database & Tables**

   - Create a MySQL database named `calculator`
   - Inside it, create the following tables:

     ```sql
     CREATE TABLE adddb (n1 INT, n2 INT, result INT);
     CREATE TABLE subdb (n1 INT, n2 INT, result INT);
     CREATE TABLE muldb (n1 INT, n2 INT, result INT);
     CREATE TABLE divddb (n1 FLOAT, n2 FLOAT, result FLOAT);
     ```

3. **Update MySQL credentials in `calculator.py`**  
   Modify this line if needed:
   ```python
   cnn = mysql.connector.connect(host='localhost', user='root', passwd='', database='calculator')
   ```

4. **Run the App**
   ```bash
   python calculator.py
   ```

---

## 🧪 Example UI

- Input two numbers
- Choose an operation
- Click `=` to view and save result
- View previous results using `History` button
- Clear all history with `Clear History`

---

## 📌 Notes

- The UI uses **CustomTkinter** for modern aesthetics
- Error dialogs are shown using modal popups
- MySQL errors are handled gracefully

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🤝 Author

Made by [@alifjobaer12](https://github.com/alifjobaer12) for personal learning and GUI/database integration practice.
