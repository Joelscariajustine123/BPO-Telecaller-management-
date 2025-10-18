from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        print("Authenticating user:", username)
        print("With password:", password)
        user = authenticate(request, username=username, password=password)
        print("With password:", password)
        if user is not None:
            login(request, user)
            print('user role:', getattr(user, 'role', 'No role attribute'))
            # Redirect based on user role
            if hasattr(user, 'role'):
                if user.role == 'admin':
                    return redirect('admin_panel:dashboard')
                elif user.role == 'manager':
                    return redirect('manager_dashboard')
                elif user.role == 'telecaller':
                    return redirect('telecaller_dashboard')
                elif user.role == 'lead':
                    return redirect('lead_dashboard')
                elif user.role == 'superuser':
                    return redirect('superuser_dashboard')
                else:
                    messages.error(request, "Unknown role. Contact admin.")
                    return redirect('login')
            else:
                messages.error(request, "User has no role assigned. Contact admin.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        role = request.POST.get('role')
        managed_by_id = request.POST.get('managed_by')

        managed_by = User.objects.get(id=managed_by_id) if managed_by_id else None

        # Create the user
        user = User.objects.create_user(
            username=username,
            password=password,
            phone_number=phone_number,
            role=role,
            managed_by=managed_by
        )
        messages.success(request, "User registered successfully.")
        return redirect('login')

    managers = User.objects.filter(role='manager')
    return render(request, 'accounts/register.html', {'managers': managers})


def logout_view(request):
    logout(request)
    return redirect('login')