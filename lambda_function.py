import json
import boto3

def lambda_handler(event, context):
    expenses = {
        "Tea": 200,
        "Bus": 500,
        "Snacks": 300,
        "Recharge": 200
    }

    total = sum(expenses.values())

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Student Expense Tracker</title>
        <style>
            body {{
                font-family: Arial;
                background: #f4f6f8;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .card {{
                background: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>My Monthly Expenses</h1>
            <p><b>Total:</b> ₹{total}</p>
            <ul>
                {''.join([f"<li>{k} – ₹{v}</li>" for k, v in expenses.items()])}
            </ul>
        </div>
    </body>
    </html>
    """

    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='student-expense-sanjana',
        Key='index.html',
        Body=html,
        ContentType='text/html'
    )

    return {
        "statusCode": 200,
        "body": "Expense report updated successfully"
    }
