# Exercise 1.1 - Python Achievement 1

## Overview

This project is part of the "Web Development with Python" course. It includes setting up a Python environment, writing a simple script, and managing the project using Git and GitHub.

## Tasks Completed

### 1. **Python Installation**
- **Version Installed**: Python 3.8.7
- **Verification**: Confirmed installation using `python3 --version`.

### 2. **Virtual Environment Setup**
- **Environment Name**: `cf-python-base`
- **Setup Commands**:
  ```bash
  python3 -m venv cf-python-base
  source cf-python-base/bin/activate
  ```

### 3. **Script Creation**
- **Script Name**: `add.py`
- **Functionality**: Adds two numbers provided by the user.
- **Code**:
  ```python
  # add.py
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))
  c = a + b
  print("The sum is:", c)
  ```

### 4. **IPython Shell Setup**
- **Package Installed**: `ipython`
- **Installation Command**:
  ```bash
  pip install ipython
  ```
- **Verification**: Launched IPython shell with the command `ipython`.

### 5. **Exporting Requirements**
- **File Created**: `requirements.txt`
- **Command Used**:
  ```bash
  pip freeze > requirements.txt
  ```

### 6. **Creating a New Environment from Requirements**
- **New Environment Name**: `cf-python-copy`
- **Setup Commands**:
  ```bash
  python3 -m venv cf-python-copy
  source cf-python-copy/bin/activate
  pip install -r requirements.txt
  ```

### 7. **GitHub Repository Setup**
- **Repository Name**: `python-achievement-1`
- **Repository URL**: [https://github.com/ffferchavez/python-achievement-1](https://github.com/ffferchavez/python-achievement-1)
- **Repository Structure**:
  ```
  python-achievement-1/
  ├── Exercise 1.1/
  │   ├── add.py
  │   ├── requirements.txt
  │   ├── README.md
  │   ├── learning_journal.md
  └── ...
  ```

### 8. **Learning Journal**
- **Document Name**: `learning_journal.md`
- **Contents**: Reflections on the exercise, what was learned, and future learning goals.

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ffferchavez/python-achievement-1.git
   cd python-achievement-1/Exercise 1.1
   ```

2. **Set Up the Virtual Environment**:
   ```bash
   python3 -m venv cf-python-base
   source cf-python-base/bin/activate
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**:
   ```bash
   python add.py
   ```

## Notes

- The main branch has been set as the default branch for this repository.
- Screenshots of each step are available in the repository under the `screenshots/` directory.

## Author

- Manuel Fernando - [ffferchavez](https://github.com/ffferchavez)
