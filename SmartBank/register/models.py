from django.db import models

class LoanApplication(models.Model):
    
    id = models.AutoField(primary_key=True)

    # User information
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150) 

    # Loan details
    loan_type = models.CharField(max_length=50)  
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    tenure_months = models.PositiveIntegerField()  
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

    # Status with default
    status = models.CharField(max_length=20, default='progress')

    # Optional timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.loan_type} - {self.status}"
