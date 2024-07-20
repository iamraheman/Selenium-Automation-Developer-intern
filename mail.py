# from flask import Flask, request, jsonify
# from flask_mail import Mail, Message

# app = Flask(__name__)

# # Configure mail
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = 'iamraheman555@gmail.com'
# app.config['MAIL_PASSWORD'] = 'egtd bpud bbhc mrdj'  # Use the app password here
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

# mail = Mail(app)

# @app.route('/send_email', methods=['POST'])
# def send_email():
#     try:
#         # Extracting request data
#         data = request.json
#         subject = data.get('subject', 'Python (Selenium) Assignment - Mahesh Waghmare')
#         to_email = data.get('to_email', 'accordbenze@gmail.com')
#         cc_email = data.get('cc_email', 'accorbenze@gmail.com')
        
#         # Create email message
#         msg = Message(subject=subject,
#                       sender=app.config['MAIL_USERNAME'],
#                       recipients=[to_email],
#                       cc=[cc_email])
#         msg.body = """
#         Dear Tech Team,

#         Please find below the required items for the assignment:

#         1. Source code (GitHub repository): [Insert GitHub Link Here]
#         2. Brief documentation of your approach: [Insert Documentation Link Here]
#         3. Your resume: [Insert Resume Link Here]
#         4. Links to past projects/work samples:
#            - Zoom Automation Project: [Insert Project Link Here]
#         5. Confirm your availability to work full time (10 am to 7 pm) for the next 3-6 months.

#         Best Regards,
#         Mahesh Waghmare
#         """

#         # Send the email
#         mail.send(msg)
#         return jsonify({"message": "Email sent successfully!"}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
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
    msg = Message(subject='Hello from the other side!', sender='MAIL_USERNAME', recipients=['accordbenze@gmail.com'])
    msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works."
    mail.send(msg)
    return "Message sent!"


if __name__ == '__main__':
    app.run(debug=True)