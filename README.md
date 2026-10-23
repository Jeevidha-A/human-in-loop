# Human-in-the-Loop Agents Using Python

## Project Overview

This project demonstrates five simple, rule-based agents built using Python. Each agent shows a different way to automate tasks, involve human feedback, or correct errors.

The project uses a leave-request email generator as an example. It runs in the terminal and is beginner-friendly.

**No AI model, API key, or external Python packages are required.**

## Agents Included

### 1. Human-in-the-Loop Agent (`app.py`)

Generates a leave-request email and allows the user to revise, approve, or reject it.

**Features:**
- Generates an email using user-provided details.
- Supports predefined revision instructions such as shorter, polite, and formal.
- Lets the human approve or reject the email.

### 2. Human-out-of-the-Loop Agent (`out.py`)

Generates a leave-request email and automatically saves it without asking for approval.

**Features:**
- Collects the leave reason and date.
- Generates the email using a predefined template.
- Automatically saves the result to `leave_email.txt`.

### 3. Approval-Based Agent (`approval.py`)

Generates an email and asks the user for approval before saving it.

**Features:**
- Displays an email preview.
- Saves the email only when the user approves.
- Rejects the email without saving it when the user chooses no.

### 4. Feedback-in-the-Loop Agent (`feedback.py`)

Improves an email based on feedback provided by the user.

**Features:**
- Generates an initial email.
- Accepts feedback such as shorter, polite, or formal.
- Repeats the review process until the user accepts the email.
- Saves the accepted result to `final_email.txt`.

### 5. Self-Correction Agent (`reflection.py`)

Checks a generated email against predefined rules and corrects detected issues automatically.

**Features:**
- Checks for required polite wording and final punctuation.
- Corrects missing wording or punctuation.
- Checks the email again after correction.
- Saves the final result to `final_email.txt`.

## Technologies Used

- Python
- Python built-in functions
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`)
- Functions
- User input and output
- File handling

## Project Structure

```text
human-in-loop/
│
├── app.py
├── out.py
├── approval.py
├── feedback.py
├── reflection.py
├── requirements.txt
└── README.md
```

Generated text files may also appear after running the programs.

## Requirements

- Python 3
- Visual Studio Code (VS Code), or another Python editor
- No additional packages required for these scripts

## How to Run

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/human-in-loop.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Open the project folder

```bash
cd human-in-loop
```

### Step 3: Run an agent

Choose any agent to run:

```bash
python app.py
```

```bash
python out.py
```

```bash
python approval.py
```

```bash
python feedback.py
```

```bash
python reflection.py
```

On Windows, you can also use `py` instead of `python` if necessary.

## Learning Objectives

- Understand different agent workflows.
- Learn how human approval can control an action.
- Understand feedback-based improvement.
- Learn basic self-correction using predefined rules.
- Practice Python functions, loops, conditions, and file handling.

## Limitations

These are beginner-level, rule-based demonstrations. They use predefined templates and rules rather than artificial intelligence or machine learning. They do not send actual emails.

## Future Improvements

- Add more email templates.
- Support additional revision instructions.
- Add stronger validation and error handling.
- Build a graphical user interface.
- Add automated tests.

## Author

Jeevidha A

## License

This project is available for educational and learning purposes.
