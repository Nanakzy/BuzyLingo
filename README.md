# BuzyLingo

BuzyLingo is an all-in-one language tutoring platform that enables students to connect with expert language tutors around the world. It offers real-time chat, booking and scheduling, payments, admin management, notifications, email confirmations, and calendar integration — all in one powerful app.

🚀 Features
✅ User Authentication (Sign up, Log in, Log out)

📅 Session Booking & Scheduling

💬 Real-Time Chat Messaging between students and tutors

📧 Email Notifications & Booking Confirmations

🔔 Real-Time Notifications

🗓️ Google Calendar Integration

💳 Payment Integration via Stripe (ZAR/USD support)

🛠️ Admin Dashboard for managing bookings and sessions

🌐 Global Support for multilingual students and tutors


🖼️ App Preview
🧑‍💻 Frontend built with HTML/CSS/JS
⚙️ Backend built with Flask, Flask-SocketIO, Stripe, and Flask-Mail

📍 Dashboard

📍 Live Chat

📍 Booking Page

📍 Admin Panel

📍 Payment Checkout


🧰 Tech Stack

Frontend	Backend	Integration
HTML/CSS/JS	Python (Flask)	Stripe (Payments)
Flask-SocketIO	Flask-Mail (Email)
Flask-Mail	Google Calendar API
Flask-Login	

📦 Installation
1. Clone the Repo
git clone https://github.com/yourusername/buzylingo.git
cd buzylingo

2. Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Setup Environment Variables
Create a .env file in the root with the following:

SECRET_KEY=your_secret_key
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_email_password
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key

5. Run the Server
flask run
# OR for real-time socket:
python app.py

✅ Usage
Open browser at http://localhost:5000

Sign up or log in as a student or admin

Book a session, chat with your tutor, or manage schedules

Admin can view and complete bookings

Stripe checkout is available for payments


🔐 Security & Privacy
Passwords are hashed with Bcrypt

Emails are verified with OTP if enabled

Secure payment processing through Stripe

JWT/session-based authentication


✨ Future Enhancements
✅ AI-based tutor matching

✅ Lesson history and replay

✅ Multi-language support

✅ Native mobile app (React Native)

👨‍💻 Contributing
Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first.

📄 License
This project is licensed under the MIT License.

🤝 Connect With Us
github: Nanakzy
linkedin: nana-khuzwayo123