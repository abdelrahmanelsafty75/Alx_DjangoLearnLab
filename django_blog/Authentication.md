# User Authentication System

## Overview
This project includes a comprehensive user authentication system leveraging Django's robust built-in `django.contrib.auth` framework, tailored for our blogging platform.

## Features & Implementation
* **Registration (`/register/`):** Utilizes a custom `CustomUserCreationForm` to securely create new users while enforcing the collection of email addresses. Passwords are automatically hashed.
* **Login/Logout (`/login/`, `/logout/`):** Handled via Django's built-in class-based views (`LoginView` and `LogoutView`), routing users to custom UI templates.
* **Profile Management (`/profile/`):** A custom view protected by the `@login_required` decorator. Authenticated users can securely update their `username` and `email` using a `UserUpdateForm`.
* **Security Measures:** All forms POSTing data strictly implement the `{% csrf_token %}` tag to protect against Cross-Site Request Forgery attacks.

## How to Test
1. Start the server using `python manage.py runserver`.
2. Visit `/register/` to create a new user.
3. Visit `/login/` to authenticate the user.
4. Visit `/profile/` to test updating the user's email or username. Ensure a success message appears.
5. Visit `/logout/` to end the session, then attempt to access `/profile/` to verify you are redirected back to the login page.