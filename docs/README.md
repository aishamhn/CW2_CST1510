# Multi-Domain Intelligence Platform

**Student Name:** Aisha Mahmood nyako
**Student ID:** M01027193
**Course:** CST1510 - CW2 - Multi-Domain Intelligence Platform

### Week 7: Secure Authentication System

**Theoretical Focus:** Secure Authentication Principles: Password hashing vs. encryption. The role of salts. Introduction to bcrypt and basic file I/O in Python.
**Practical Focus:** Implement Secure Login (Text-Based)

## Project Description
A command-line authentication system implementing secure password hashing
This system allows users to register accounts and log in with proper password

## Features
- Secure password hashing using bcrypt with automatic salt generation
- User registration with duplicate username prevention
- User login with password verification
- Input validation for usernames and passwords
- File-based user data persistence

## Technical Implementation
- Hashing Algorithm: bcrypt with automatic salting
- Data Storage: Plain text file (`users.txt`) with comma-separated values
- Password Security: One-way hashing, no plaintext storage
- Validation: Username (3-20 alphanumeric characters), Password (6-50 characters)

---

### Week 8: Data Pipeline & CRUD (SQL)

**Theoretical Focus:** Relational Databases & SQL: Introduction to SQLite. Database schema design (Normalization). Full CRUD operations and parameterized queries (SQL Injection prevention).
**Practical Focus:** Database Migration & CRUD for All Domains

**Implementation Tasks:**
1. **Database Manager:** Create a DatabaseManager class to handle SQLite connection and cursor operations.
2. **Schema Design:** Create the users table and the tables for **ALL THREE** domains.
3. **Data Migration:** Write a script to read data from `users.txt` and insert it into the new SQLite `users` table.
4. **CRUD Implementation:** Implement all four CRUD operations (Create, Read, Update, Delete) for **ALL THREE** domain tables.
5. **Data Loading:** Use pandas to read the provided sample data (e.g., `cyber_incidents.csv`) and load it into the respective SQLite tables.

**GitHub Deliverable:** A command-line script that uses the SQLite database for all user and domain data. Full CRUD functionality demonstrated via the command line for all three domains.

---

### Week 9: Web Interface, MVC & Visualization

**Theoretical Focus:** Web Application Architecture: Streamlit fundamentals, session state management, multi-page apps. Data Visualization with Plotly/Matplotlib and embedding charts in Streamlit.
**Practical Focus:** Streamlit Conversion & Master One Domain

**Implementation Tasks:**
1. **Streamlit Setup:** Convert the application to a Streamlit multi-page structure (`app.py`, `pages/Login.py`, `pages/Dashboard.py`).
2. **Login Page:** Implement the login page (`Login.py`) using Streamlit widgets and integrate the Week 8 database functions. Use `st.session_state` to manage the logged-in user and role.
3. **Dashboard Conversion:** Create the dashboard page for the student's **Primary Domain**. Convert the Week 8 CRUD operations into interactive Streamlit forms and tables.
4. **Visualization:** Implement the required analytical functions and **All Visualizations** for the chosen domain (e.g., Bar Chart) and embed them using Streamlit.

**GitHub Deliverable:** A fully functional Streamlit web application with: Secure Login, Session Management, and **ONE** complete, interactive domain dashboard featuring all required visualizations.

---

### Week 10: Final Dashboards & AI Integration

**Theoretical Focus:** API Integration: REST APIs, API keys, Environment Variables. Introduction to the Gemini API and context-aware prompting.
**Practical Focus:** Complete Remaining Dashboards & Integrate AI

**Implementation Tasks:**
1. **Remaining Dashboards:** Implement the remaining analytical functions and visualizations for the **Secondary/Tertiary Domains**.
2. **AI Integration:** Set up the API key using **Streamlit Secrets**. Create a helper function (`ai_service.py`) to call the Gemini API.
3. **AI Assistant:** Integrate the AI Assistant feature into its own dedicated chat page (`ai_chat.py`) to provide security advice or statistical explanations.

**GitHub Deliverable:** A complete, fully functional Multi-Domain Intelligence Platform that meets all mandatory requirements (Authentication, DB, CRUD for all domains, All Visualizations, AI).

---

### Week 11: Software Architecture & Polish

**Theoretical Focus:** Software Refactoring: Benefits of OOP. Review of class design, constructors, methods, and attributes. Final project documentation and submission requirements.
**Practical Focus:** OOP Refactoring & Final Documentation

**Implementation Tasks:**
1. **Refactoring:** Refactor the procedural code from Weeks 7-10 to use a clean, maintainable structure (e.g., Service and Data Access Layers).
2. **Documentation:** Write the final `README.md` and ensure all code has clear comments and docstrings.
3. **Report Preparation:** Finalize the required diagrams and draft the technical report.

**GitHub Deliverable:** The final project code, fully refactored and documented, ready for submission.