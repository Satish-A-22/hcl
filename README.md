Simple Step-by-Step Flow
1. User signup / login

*   User opens the app.

*   Enter username & password.

*   If the same username+password already exists → log in (no new registration).

*   If not, register the new user and save credentials (hash passwords).

2. Apply for a loan

*    User (logged in) goes to Apply for Loan.

*   Choose Loan Type: Home / Personal / Auto.

*   Enter Loan Amount (P), Tenure (N) (months or years), and Interest Rate (annual R%).

*   Submit the form → application saved with status Pending.

3. EMI calculation (automatic)

*    Convert annual rate to monthly: r = R / (12 * 100)

*    Convert tenure to months if needed: n = N_months

*   EMI formula:

        EMI = (P * r * (1 + r)**n) / ((1 + r)**n - 1)



4. Admin review

*    Admin logs into Admin Dashboard.

*   See list of applications with status Pending.

*   For each application, admin can click:

*   Approve → status = Approved

*   Reject → status = Rejected

5. User sees status

*   User opens their dashboard.

*   They see each application with:

*   Application ID


Status: Pending / Approved / Rejected

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
      ┌─────────┼─────────┐
      ▼                     ▼
┌─────────────┐      ┌─────────────┐
│  Approve    │      │  Reject     │
└───────┬─────┘      └───────┬─────┘
        │                     │
        ▼                     ▼
┌──────────────────────────────┐
│   Loan Status Updated        │
│ (Visible to the Customer)    │
└──────────────────────────────┘

User Side:

    User logs in with username and password.

    Enters loan details (price, rate, month).

    Application is saved with status = pending.

    User can check status anytime on the website.

Admin Side:

    Admin dashboard shows all pending applications.

    Admin can approve or reject applications.

    Database is updated based on admin action.

API Endpoints

/login → User login
username and password

/register->fill the application for loan
type , amount, tenure

/calculator → Calculate EMI
amount rate month = value 
/status → Check loan status

/admin ->to show dashboard