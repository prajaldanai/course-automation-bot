# Course Automation Bot

A Python automation tool that automatically progresses through lessons on an online learning platform.

The bot uses **Selenium** to control a Chrome browser and perform actions such as:

- Clicking **Start Now**
- Clicking **Mark as Complete**
- Clicking **Next Lesson**
- Automatically scrolling the page

This project demonstrates **browser automation using Python and Selenium**.

---

# Repository

https://github.com/prajaldanai/course-automation-bot.git

---

# Features

- Automated lesson progression
- Detects and clicks **Start Now**
- Marks lessons as **Complete**
- Navigates to the **Next lesson**
- Automatic page scrolling
- Handles dynamic web elements

---

# Technologies Used

- Python
- Selenium
- WebDriver Manager
- Chrome WebDriver

---

# Project Structure


course-automation-bot
│
├── bot.py # Main automation script
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

# Requirements

Make sure the following are installed:

- Python 3.8+
- Google Chrome
- Internet connection

---

# Installation Guide

## 1 Clone the Repository


git clone https://github.com/prajaldanai/course-automation-bot.git


## 2 Navigate to the Project Folder


cd course-automation-bot


## 3 Install Dependencies


pip install -r requirements.txt


---

# How to Run the Bot

Run the automation script:


python bot.py


---

# How to Use

1. After running the script, a **Chrome browser will open automatically**.

2. Login to your learning platform manually.

3. Open the **first lesson page**.

4. Return to the terminal and press **ENTER**.

5. The automation bot will now:

   - Scroll down the page
   - Click **Start Now**
   - Click **Mark as Complete**
   - Click **Next Lesson**
   - Repeat the process until there are no more lessons

---

# Example Workflow


Start Now
↓
Scroll page
↓
Mark as Complete
↓
Next Lesson
↓
Repeat until finished


---

# Generate requirements.txt (Optional)

If dependencies change, regenerate the requirements file:


pip freeze > requirements.txt


---

# Learning Purpose

This project was created to practice:

- Python automation
- Browser automation with Selenium
- Web scraping and DOM interaction
- Automated workflows

---

# Author

**Prajal Danai**

GitHub: https://github.com/prajaldanai
   