import os
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

# Load environment variables

app = Flask(__name__)
CORS(app)  

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ""
app.config['MAIL_PASSWORD'] = ""
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
sender = ""
recipient = ""

mail = Mail(app)

@app.route('/send-appointment', methods=['POST'])
def send_appointment():
    data = request.json
    
    print(data)
    # 1. Extract Data
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    message_body = data.get('message')

    # 2. Validation
    if not all([name, phone, email, message_body]):
        return jsonify({'success': False, 'message': 'All fields are required.'}), 400

    # 3. Create Formatted HTML Email
    html_content = f"""
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden;">
        <div style="background-color: #0d6efd; padding: 20px; text-align: center; color: white;">
            <h2 style="margin: 0;">New Appointment Request</h2>
            <p style="margin: 5px 0 0;">Website Inquiry</p>
        </div>
        
        <div style="padding: 25px; background-color: #f9f9f9;">
            <p style="color: #555; font-size: 16px;">Hello Dr. Saroj,</p>
            <p style="color: #555; font-size: 16px;">You have received a new message from your portfolio website. Here are the details:</p>
            
            <table style="width: 100%; border-collapse: collapse; margin-top: 20px; background: white; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <tr style="border-bottom: 1px solid #eee;">
                    <td style="padding: 12px; font-weight: bold; color: #333; width: 30%;">Name</td>
                    <td style="padding: 12px; color: #555;">{name}</td>
                </tr>
                <tr style="border-bottom: 1px solid #eee;">
                    <td style="padding: 12px; font-weight: bold; color: #333;">Phone</td>
                    <td style="padding: 12px; color: #555;">
                        <a href="tel:{phone}" style="color: #0d6efd; text-decoration: none;">{phone}</a>
                    </td>
                </tr>
                <tr style="border-bottom: 1px solid #eee;">
                    <td style="padding: 12px; font-weight: bold; color: #333;">Email</td>
                    <td style="padding: 12px; color: #555;">
                        <a href="mailto:{email}" style="color: #0d6efd; text-decoration: none;">{email}</a>
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px; font-weight: bold; color: #333; vertical-align: top;">Message</td>
                    <td style="padding: 12px; color: #555; line-height: 1.5;">{message_body}</td>
                </tr>
            </table>

            <div style="margin-top: 30px; text-align: center;">
                <a href="mailto:{email}" style="background-color: #0d6efd; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold;">Reply via Email</a>
            </div>
        </div>
        
        <div style="background-color: #eee; padding: 15px; text-align: center; font-size: 12px; color: #777;">
            This email was sent automatically from your website contact form.
        </div>
    </div>
    """

    # 4. Send Email
    try:
        msg = Message(
            subject=f"🔔 New Appointment: {name}",
            sender=sender,     # Your 'No Reply' email
            recipients=recipient # Dr. Saroj's email
        )
        msg.reply_to = email # So clicking reply goes to the patient
        msg.html = html_content
        
        mail.send(msg)
        return jsonify({'success': True, 'message': 'Appointment request sent!'}), 200

    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'success': False, 'message': 'Failed to send email.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)