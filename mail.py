from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'iamraheman555@gmail.com'
app.config['MAIL_PASSWORD'] = 'egtd bpud bbhc mrdj'  # Use the app password here
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route("/")
def index():
        # Create email message
        msg = Message(subject=["Python (Selenium) Assignment - Abdul Raheman,"],
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['tech@themedius.ai'],
                      cc=['hr@themedius.ai'])
        msg.body = """
Dear Tech Team
Please find below the required items for the assignment:
1. Screenshot of the form filled via code
2. Source code (GitHub repository): https://github.com/iamraheman/Selenium-Automation-Developer-intern.git
3. Brief documentation of approach: https://docs.google.com/document/d/1me_3k-moLOAhCraxapDh5dy6fYH7Gp2A-uNKO5oqcjE/edit?usp=sharing
4. Resume: Attached 
5. Links to past projects samples:
   - Zoom Automation Project: https://drive.google.com/drive/folders/1sBEfcPQ4qOOeRR5petRDECzQqWYfwd1L?usp=sharing
6. I Confirm my availability to work full time (10 am to 7 pm) for the next 3-6 months


Best Regards,
Abdul Raheman Shaikh
"""

        with app.open_resource("E:\Abdul_Resume.pdf") as pdf:
            msg.attach("Abdul_Resume.pdf", "application/pdf", pdf.read())

        with app.open_resource("E:\Screenshot 2024-07-20 192036.png") as img:
            msg.attach("Screenshot_2024-07-20_192036.png", "image/png", img.read())
        
        mail.send(msg)
        return "Mail sent! Thank you, Eager to hear back from you."

if __name__ == '__main__':
    app.run(debug=True)
