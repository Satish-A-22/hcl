1. Signup / Login

      *  Users can register or log in using username and password.

      *  If already registered, login directly.

2. Apply for a Loan

        Users can apply for Home, Personal, or Auto loans.

        Required details:

        Loan Amount (P)

        Tenure (N months/years)

        Interest Rate (R%)

        Each new application is saved with status = Pending.

3. EMI Calculation

        Automatically calculated using:

        r = R / (12 * 100)
        EMI = (P * r * (1 + r)**n) / ((1 + r)**n - 1)


        EMI result is displayed immediately after submission.

4. Check Loan Status


        Status → Pending / Approved / Rejected

🧑‍🏫 Admin Side
        1. Admin Login

        Access via /admin-login/

        Only superusers can log in.

2. Admin Dashboard

        URL: /admin-dashboard/

        Shows all Pending loan requests.

Admin can:

        ✅ Approve → updates status to Approved

        ❌ Reject → updates status to Rejected

Direct URL access without login is blocked.

🌐 API Endpoints
Endpoint	Method	Description	Parameters
/	        POST	Apply for a loan	loan_type, amount, tenure, rate
/calculator	POST	Calculate EMI	amount, rate, time
/status	        POST	Check loan status	username, password
/admin-login	POST	Admin login	username, password
/admin-dashboard	GET/POST	Admin dashboard	app_id, action (Approve/Reject)


🧭 Project Flow (Step-by-Step)

3️⃣ Loan Application (select type, amount, etc.) →
4️⃣ EMI Calculation (Python formula) →
5️⃣ Admin Dashboard (Review requests) →
6️⃣ Admin Approves/Rejects loan →
7️⃣ User views updated status

⚙️ Installation & Setup
1. Clone the repository
git clone <repo-url>
cd SmartBank

2. Create a virtual environment
python -m venv env
# Activate it
# On Windows:
env\Scripts\activate
# On Linux/Mac:
source env/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Create a superuser (for Admin login)
python manage.py createsuperuser

6. Run the server
python manage.py runserver


Access the app at: http://127.0.0.1:8000/

🧪 Testing
Unit Tests

Test EMI calculator logic

Validate user input and model rules

Integration Tests

Test API endpoints:
/login, /register, /calculator, /status, /admin-dashboard

Admin Flow Tests

Verify only logged-in admins can approve/reject applications

Run all tests:

pytest -v
