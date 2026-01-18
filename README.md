# Student Expense Tracker using AWS (Serverless)

## 📌 Project Overview
This project is a beginner-friendly serverless AWS application that generates a
monthly expense report for a student and hosts it as a public static website.

The goal of this project is to understand how core AWS services work together
in a real-world scenario without using servers, databases, or complex frameworks.

This project follows a fully serverless architecture using AWS Lambda and Amazon S3.

---

## 🛠️ Technologies Used
- AWS Lambda (Python)
- Amazon S3 (Static Website Hosting)
- AWS IAM (Roles & Permissions)
- Python (boto3)
- HTML & CSS (generated dynamically)

---

## 🧠 Architecture Explanation
This project follows a simple serverless workflow:

1. Expense data is defined inside the AWS Lambda function.
2. AWS Lambda calculates the total monthly expense.
3. Lambda dynamically generates an HTML page using Python.
4. The generated HTML file (`index.html`) is uploaded to an S3 bucket.
5. Amazon S3 hosts the file as a public static website.
6. The website can be accessed using the S3 website endpoint.

There are no servers, no databases, and no backend APIs involved.

---

## ⚙️ AWS Services Used (In Detail)

### 🔹 AWS Lambda
- Written in Python
- Calculates expenses and total amount
- Generates HTML content dynamically
- Uploads the HTML file to Amazon S3 using boto3
- Runs only when triggered (event-based)

### 🔹 Amazon S3
- Used for static website hosting
- Stores the generated `index.html` file
- Public access enabled for website hosting
- Very low cost and scalable

### 🔹 AWS IAM
- IAM role attached to Lambda function
- Permissions:
  - Allows Lambda to upload objects to S3
  - Allows logging to CloudWatch
- Ensures secure access control

---

## 🔄 How the Project Works (Step-by-Step)

1. AWS Lambda function is triggered manually (or can be scheduled).
2. Expense data (Tea, Bus, Snacks, Recharge) is processed.
3. Total expense is calculated inside Lambda.
4. Lambda creates a styled HTML page with the expense report.
5. The HTML file is uploaded to an S3 bucket as `index.html`.
6. Amazon S3 serves the page publicly as a static website.

Whenever Lambda is triggered again, the website content is updated.

---

## 🌐 Live Demo
🔗 https://student-expense-sanjana.s3-website.ap-south-1.amazonaws.com/

---
## Website Preview

![Student Expense Tracker Output](website-output.png)


## 📂 Repository Structure

## 🧩 Lambda Function Code Explanation

The core logic of this project is implemented inside the AWS Lambda function
written in Python (`lambda_function.py`). This function is responsible for
calculating expenses, generating an HTML page, and uploading it to Amazon S3.

---

### 1️⃣ Importing Required Libraries
```python
import json
import boto3

