import json
import boto3

def lambda_handler(event, context):

    # 1️⃣ Student expenses (sample data)
    expenses = {
        "Tea": 200,
        "Bus": 500,
        "Snacks": 300,
        "Recharge": 200
    }

    # 2️⃣ Calculate total expense
    total = sum(expenses.values())

    # 3️⃣ Create HTML page dynamically
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Student Expense Tracker</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f2f2f2;
            }}
            .card {{
                background: white;
                padding: 20px;
                width: 300px;
                margin: 100px auto;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>My Monthly Expenses</h2>
            <p><b>Total:</b> ₹{total}</p>
            <ul>
                {''.join([f"<li>{k} - ₹{v}</li>" for k, v in expenses.items()])}
            </ul>
        </div>
    </body>
    </html>
    """

    # 4️⃣ Upload HTML to S3
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket="student-expense-sanjana",   # ⚠️ your bucket name
        Key="index.html",
        Body=html,
        ContentType="text/html"
    )

    # 5️⃣ Lambda response
    return {
        "statusCode": 200,
        "body": "Expense report updated successfully"
    }

