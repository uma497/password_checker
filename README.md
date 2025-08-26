# 🔐 Password Strength & Breach Checker

A Python-based tool that checks if a password is strong and whether it has appeared in known data breaches (using k-Anonymity with the HaveIBeenPwned API).

![GitHub stars](https://img.shields.io/github/stars/uma497/password-checker?style=social) 
![GitHub forks](https://img.shields.io/github/forks/uma497/password-checker?style=social)  
![Python](https://img.shields.io/badge/python-3.x-blue.svg) 
![Build](https://img.shields.io/badge/build-passing-brightgreen)

---

## Features

- ✅ Checks password strength (length, special characters, entropy)  
- ✅ Verifies if password exists in real leaked password databases  
- ✅ Uses **k-Anonymity** (secure, no raw password is sent)  
- ✅ CLI-based tool, lightweight and easy to use  

---

## Project Structure

password-checker/  
├── src/  
│   └── password_checker.py  
├── tests/  
│   └── test_password_checker.py  
├── requirements.txt  
├── README.md  
├── LICENSE  
└── .gitignore  

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/uma497/password-checker.git
cd password-checker
pip install -r requirements.txt

##Usage

Run the tool:

python src/password_checker.py


Sample Output:

🔐 Password Strength & Breach Checker 🔐

Enter a password to check: **********
Strength Check → Strong password ✅
Breach Check → ⚠️ Found in 5 data breaches! Choose another password.

##Testing

Run unit tests with:

pytest tests/

##Demo

(Insert demo GIF or screenshot here once ready)

##Tech Stack

Python 3

Requests library

HaveIBeenPwned API

Pytest (for testing)

##Future Improvements

 Add a GUI version with Tkinter / PyQt

 Create a browser extension version

 Add password manager integration

 Dockerize the project

##Contributing

Contributions are welcome!

Fork the repo

Create your feature branch (git checkout -b feature/YourFeature)

Commit changes (git commit -m 'Add some feature')

Push to branch (git push origin feature/YourFeature)

Open a Pull Request

##License

This project is licensed under the MIT License - see the LICENSE
 file for details.

##Author

Uma Tomar

📧 Email: umatomar497@gmail.com

💼 LinkedIn: linkedin.com/in/uma-tomar-aa2772293

🐙 GitHub: github.com/uma497

⭐ If you like this project, don’t forget to star the repo!
