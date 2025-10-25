# register/tests/test_views.py
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from register.models import LoanApplication

@pytest.mark.django_db
def test_status_view_success_and_fail(client):
    # Create a loan application (no auth — plain username/password fields on model)
    LoanApplication.objects.create(
        username="alice",
        password="alicepass",
        loan_type="personal",
        amount=10000.0,
        tenure_months=12,
        interest_rate=5.0,
        status="Progress"
    )

    url = reverse('status')

    # Successful check: correct username/password -> shows status
    resp = client.post(url, {'username': 'alice', 'password': 'alicepass'})
    assert resp.status_code == 200
    content = resp.content.decode()
    assert "progress" in content.lower()  # status displayed

    # Failed check: wrong credentials -> shows error message
    resp2 = client.post(url, {'username': 'alice', 'password': 'wrongpass'})
    assert resp2.status_code == 200
    content2 = resp2.content.decode()
    assert "invalid" in content2.lower() or "not found" in content2.lower()

@pytest.mark.django_db
def test_admin_login_and_approve_reject_flow(client):
    # Create a superuser to use for admin login
    admin_user = User.objects.create_superuser(username='ind', email='', password='ind123')

    # Create two loan applications in progress
    a1 = LoanApplication.objects.create(
        username="bob", password="bobpass", loan_type="home",
        amount=50000, tenure_months=24, interest_rate=7.0, status="Progress"
    )
    a2 = LoanApplication.objects.create(
        username="carol", password="carolpass", loan_type="persional",
        amount=20000, tenure_months=12, interest_rate=8.0, status="Progress"
    )

    login_url = reverse('admin_login')
    dashboard_url = reverse('admin_dashboard')

    # Login via admin_login view (posts username/password)
    resp = client.post(login_url, {'username': 'ind', 'password': 'ind123'}, follow=True)
    assert resp.status_code == 200

    # After login, admin_dashboard should be reachable
    resp2 = client.get(dashboard_url)
    assert resp2.status_code == 200

    # Approve a1 using POST (simulate pressing Approve button)
    resp3 = client.post(dashboard_url, {'app_id': str(a1.id), 'action': 'approve'}, follow=True)
    assert resp3.status_code == 200
    a1.refresh_from_db()
    assert a1.status == "approved"

    # Reject a2
    resp4 = client.post(dashboard_url, {'app_id': str(a2.id), 'action': 'reject'}, follow=True)
    assert resp4.status_code == 200
    a2.refresh_from_db()
    assert a2.status == "rejected"

@pytest.mark.django_db
def test_calculator_negative_input_shows_error(client):
    url = reverse('calculator')

    # Post negative principal -> should produce error in response
    resp = client.post(url, {'principal': '-1000', 'rate': '10', 'time': '12'})
    assert resp.status_code == 200
    text = resp.content.decode().lower()
    assert "positive" in text or "must be positive" in text or "invalid" in text

    # Post zero tenure_months -> should show appropriate error
    resp2 = client.post(url, {'principal': '10000', 'rate': '10', 'time': '0'})
    assert resp2.status_code == 200
    text2 = resp2.content.decode().lower()
    assert "greater than zero" in text2 or "tenure_months_months_months_months_months_months_months_months_months" in text2 or "cannot be zero" in text2
