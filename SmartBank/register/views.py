from django.shortcuts import render, redirect
from .models import LoanApplication
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        loan_type = request.POST.get('loan_type')
        amount = request.POST.get('amount')
        tenure = request.POST.get('tenure')
        interest_rate = request.POST.get('interest_rate')

        # Convert to correct types
        amount = float(amount) if amount else 0
        tenure = int(tenure) if tenure else 0
        interest_rate = float(interest_rate) if interest_rate else 0.0

        # Create LoanApplication object
        LoanApplication.objects.create(
            username=username,
            password=password,
            loan_type=loan_type,
            amount=amount,
            tenure_months=tenure,
            interest_rate=interest_rate,
            status='Progress'  # default status
        )

        return redirect('/')

    return render(request, 'register.html')

def calculator(request):
    emi = None
    error = None

    if request.method == "POST":
        try:
            # Get values from form
            P = request.POST.get('principal')
            annual_rate = request.POST.get('rate')
            n = request.POST.get('time')

            # Check if fields are empty
            if not P or not annual_rate or not n:
                raise ValueError("All fields are required!")

            # Convert to numeric
            P = float(P)
            annual_rate = float(annual_rate)
            n = int(n)

            # Check for negative or zero values
            if P <= 0 or annual_rate <= 0 or n <= 0:
                raise ValueError("All values must be positive and greater than zero!")

            # EMI calculation
            r = annual_rate / (12 * 100)
            emi = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
            emi = round(emi, 2)

        except OverflowError:
            error = "Value too large! Try smaller numbers."
        except ZeroDivisionError:
            error = "Tenure cannot be zero."
        except ValueError as ve:
            error = str(ve)
        except Exception as e:
            error = f"Unexpected error: {e}"

    return render(request, 'calculator.html', {'emi': emi, 'error': error})


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        
        user = authenticate(request, username=username, password=password)
        
       
        if user is not None and user.is_superuser:
            login(request, user)
            request.session['admin_logged_in'] = True
            return redirect('admin_dashboard')  
        else:
            error = "Invalid admin credentials"
            return render(request, 'admin_login.html', {'error': error})
    
    return render(request, 'admin_login.html')


def admin_dashboard(request):
    # Check if admin is logged in
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')

    # Fetch only applications with status 'progress'
    applications = LoanApplication.objects.filter(status='Progress')

    if request.method == "POST":
        app_id = request.POST.get("app_id")
        action = request.POST.get("action")
        app = LoanApplication.objects.get(id=app_id)
        if action == "approve":
            app.status = "approved"
        elif action == "reject":
            app.status = "rejected"
        app.save()

    applications = LoanApplication.objects.filter(status='Progress')  
    print("applications",applications)
    return render(request, 'admin_dashboard.html', {'applications': applications})


def status_view(request):
    status = None
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if user exists with same username and password
        try:
            application = LoanApplication.objects.get(username=username, password=password)
            status = application.status
        except LoanApplication.DoesNotExist:
            error = "Invalid username or password"

    return render(request, "status.html", {"status": status, "error": error})