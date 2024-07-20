Google Form Automation
This project demonstrates how to use Selenium to automate the process of filling out a Google Form.

Prerequisites
Python 3.x installed on your system.
Google Chrome browser installed.
ChromeDriver compatible with your Chrome browser version.
Setup
Clone this repository:

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Install the required Python packages:

bash
Copy code
pip install selenium
Download the ChromeDriver from here and place it in a suitable directory.

Update the webdriver_path in the script to the path where you placed the ChromeDriver.

Running the Script
Ensure you have the necessary permissions to execute the script.
Run the script using Python:
bash
Copy code
python google_form_automation.py
Script Explanation
Initialization: The script starts by setting up the Selenium WebDriver with ChromeDriver.
Navigating to Google Form: The script navigates to the specified Google Form URL.
Filling Out Form Fields: The script locates each form field using XPath and fills it with predefined data.
Waiting and Closing: After filling out the form, the script waits for a specified duration before closing the browser.


Email Submission with Flask
This project demonstrates how to use Flask and Flask-Mail to send an email with assignment details.

Prerequisites
Python 3.x installed on your system.
A Gmail account with an app-specific password if 2-step verification is enabled.
Setup
Clone this repository:

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Install the required Python packages:

bash
Copy code
pip install Flask Flask-Mail
Update the app.config section in the script with your email credentials and SMTP settings.

Running the Flask Application
Ensure you have the necessary permissions to execute the script.
Run the Flask application using:
bash
Copy code
flask run
Sending an Email
Use a tool like Postman or curl to send a POST request to the /send_email endpoint.
The request body should contain the subject, recipient email, and other required details.
Flask Application Explanation
Initialization: The script sets up the Flask application and configures the Flask-Mail extension.
Email Endpoint: A POST endpoint /send_email is defined to handle email requests.
Sending Email: The endpoint extracts email details from the request, constructs the email content, and sends the email using Flask-Mail.
