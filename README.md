# 📞 BPO Telecaller Management App (Modular Structure)

This is a **Django-based web application** for managing telecallers, leads, and calls in a BPO environment.  
The project follows a **modular structure**, where each user role has its own dedicated Django app for better organization and scalability.

---

## 🚀 Features

### 🧩 Role-Based Access Control (via separate apps)

- **Admin (`admin_panel` app)**  
  Manages all users, with special privileges to add or remove Managers.

- **Manager (`manager_panel` app)**  
  Views overall performance dashboards and analytics.

- **Lead Manager (`lead_manager_panel` app)**  
  Uploads lead sheets (Excel/PDF), which are automatically distributed among telecallers.  
  Can also monitor the status of leads.

- **Telecaller (`telecaller_panel` app)**  
  Receives leads, makes calls, and updates the status of each call.

---

### 👥 Custom User Model (`users` app)
- Handles different roles (Admin, Manager, Lead Manager, Telecaller).  
- Tracks specific data like total call time and performance.

---

### 📊 Centralized Lead Management (`leads` app)
- Dedicated app to manage:
  - **Lead** model  
  - **Call** model  
  - **UploadedFile** model  
- Provides a **single source of truth** for all lead data.

---

### ☎️ Call Logging & Performance Tracking
- Automatically records **call duration** when a telecaller attends a call.  
- Unattended calls are marked accordingly.  
- **Total call time** and **lead statuses** are visible to Lead Managers and Managers.

---

### 💻 Responsive Web Interface
- Built using **Tailwind CSS** for a modern, responsive, and accessible design.  
- Works seamlessly on desktop, tablet, and mobile devices.

---

## ⚙️ Setup and Installation

### 1️⃣ Apply database migrations
```bash
python manage.py migrate
```


### 2️⃣Create a superuser (Admin):
``` bash
python manage.py createsuperuser
```

During creation, you can set the role for this user. To have full access, you can leave it or set it to 'admin'. The superuser will have all permissions regardless of the custom role.

### 3️⃣Run the development server:
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000.

Create other users: Use the Django admin interface at /admin to create new users and assign them the roles of Manager, Lead Manager, or Telecaller.
