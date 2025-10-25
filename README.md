SmartBank - Loan Management System

SmartBank is a simple web-based loan management system where users can apply for loans, calculate EMI, and track application status. Admins can review, approve, or reject loan requests.

1. Features
User Side

Signup / Login

Users can register or log in using a username and password.

Existing users with the same credentials can log in directly.

Passwords are securely stored (hashed) in the database.

Apply for a Loan

Logged-in users can apply for Home, Personal, or Auto loans.

Required inputs: Loan Amount (P), Tenure (N months/years), Interest Rate (R%).

Application is saved with status = Pending.

EMI Calculation

EMI is automatically calculated using the formula:

r = R / (12 * 100)  # Monthly interest rate
EMI = (P * r * (1 + r)**n) / ((1 + r)**n - 1)


EMI is displayed to the user immediately after submitting the form.

Check Loan Status

Users can see each loan application with:

Application ID

Loan Type

Amount

Tenure

Interest Rate

Status: Pending / Approved / Rejected

Admin Side

Admin Login

Admins log in via /admin-login/.

Only superusers can access the Admin Dashboard.

Admin Dashboard

URL: /admin-dashboard/

Only accessible if the admin is logged in; otherwise, redirected to login.

Shows all Pending loan applications.

Admin can:

Approve → updates status to Approved

Reject → updates status to Rejected

Access Control

Dashboard is protected by a session check.

Direct access via URL without login is blocked.

2. API Endpoints
Endpoint	Method	Description	Parameters
/login	POST	User login	username, password
/register	POST	Apply for a loan	loan_type, amount, tenure, rate
/calculator	POST	Calculate EMI	amount, rate, time
/status	POST	Check loan status	username, password
/admin-login	POST	Admin login	username, password
/admin-dashboard	GET/POST	Admin dashboard	Approve/Reject application via app_id and action

3. Step-by-Step Flow
┌────────────────────┐
│  Customer Signup   │
└───────┬────────────┘
        │
        ▼
┌────────────────────┐
│   User Login       │
└───────┬────────────┘
        │
        ▼
┌──────────────────────────────┐
│  Loan Application Form       │
│  (Select type, amount, etc.) │
└───────┬──────────────────────┘
        │
        ▼
┌──────────────────────────────┐
│   EMI Calculation (Python)   │
└───────┬──────────────────────┘
        │
        ▼
┌────────────────────┐
│  Admin Dashboard   │
│  (Review Request)  │
└───────┬────────────┘
        │
  ┌─────┴─────┐
  ▼           ▼
┌───────┐   ┌───────┐
│Approve│   │Reject │
└───────┘   └───────┘
        │           │
        ▼           ▼
┌──────────────────────────────┐
│   Loan Status Updated        │
│ (Visible to the Customer)    │
└──────────────────────────────┘

4. Installation / Setup

Clone the repository:

git clone <repo-url>
cd SmartBank


Create a virtual environment:

python -m venv env
source env/bin/activate   # Linux / macOS
env\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Create a superuser (for admin):

python manage.py createsuperuser


Run the server:

python manage.py runserver

5. Additional / Future Features

Loan Filtering / Sorting: Filter by loan type, status, or user.

Email Notifications: Send emails to users when a loan is approved/rejected.

Multiple Admin Roles: Admins with different permissions.

Dashboard Analytics: Total applications, approval rate, pending loans, etc.

PDF Generation: Generate EMI schedules for users.

REST API: Full API support for external mobile apps.

Two-Factor Authentication (2FA): Secure admin login.

Loan History: Users can see previous applications.

Interest Rate Calculator: Compare loans with different rates dynamically.

Dark Mode / UI Improvements: Enhance user experience.

6. Testing

Unit Tests: Test calculator logic, input validation, and model constraints.

Integration Tests: Test API endpoints /login, /register, /calculator, /status, /admin-dashboard.

Admin Flow Tests: Ensure only logged-in admins can approve/reject loans.

Run tests using:

pytest -v


This README explains the project, workflow, API, and future enhancements clearly.