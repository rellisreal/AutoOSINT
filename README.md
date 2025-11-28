# AutoOSINT

## Overview
The **OSINT Automation Tool** is planned to be a modular, web-based platform designed to automate Open-Source Intelligence (OSINT) gathering for a given target (e.g., email, username, domain, or file). Users can select which OSINT modules to run and receive consolidated reports in real-time. This project showcases full-stack development, API design, cybersecurity skills, and secure authentication practices.

The tool will be built with:
- **Backend:** Django REST Framework (DRF) with custom JWT authentication
- **Frontend:** Vite + React
- **Background Tasks:** Celery with Redis for asynchronous scan execution

---

## Scope of Work

### **Primary Objectives**
1. **User Authentication**
   - Implement secure, custom JWT-based authentication
   - Login, token refresh, and protected endpoints

2. **Modular OSINT Scans**
   - Allow users to select from multiple OSINT modules via checkboxes
   - Example modules (expandable in the future):
     - Breach lookup
     - Username footprinting
     - Metadata extraction from files/images
     - IP / Domain reconnaissance
     - Social media footprint analysis
   - Each module runs independently and asynchronously

3. **Scan Execution**
   - Execute scans in the background using **Celery**
   - Ensure the backend does not block while running long scans
   - Allow multiple modules to run simultaneously

4. **Report Generation**
   - Consolidate scan results into structured JSON
   - Display results on the frontend dashboard
   - Optionally export reports as PDF/HTML (future expansion)

5. **Frontend**
   - User-friendly dashboard built with React + Vite
   - Module selection interface
   - Scan status indicator (polling via API)
   - Display of consolidated scan reports

6. **Security Best Practices**
   - Proper JWT authentication and authorization
   - CSRF protection and safe request handling
   - Input validation to prevent injection attacks
   - Secure storage of scan data

---

## Project Targets
- **Target Data Sources:** Publicly available data such as:
  - Breach data (via public APIs)
  - Username presence across platforms
  - File/image metadata
  - Domain and IP WHOIS info
  - Public social media footprints
- **Success Criteria:**
  - Users can select modules and execute scans
  - Backend handles long-running scans without timeouts
  - Reports are generated and displayed in a readable format
  - JWT authentication is secure and functional
  - Frontend is responsive and user-friendly

---

## Achievements / Deliverables
- Fully functional **Django REST API** backend
- **Celery**-powered asynchronous task execution
- **React + Vite** frontend with:
  - Login/authentication
  - Module selection interface
  - Scan progress tracking
  - Report display page
- Example OSINT modules integrated and functional
- Documentation for adding new OSINT modules
- Optionally: Exportable reports (PDF/HTML)
- Demonstrates real-world full-stack security project suitable for a resume

---

## Future Enhancements
- Add more OSINT modules (e.g., social media scrapers, advanced domain/IP analysis)
- Add scheduling of recurring scans
- Add user-specific scan history
- Integrate email or webhook notifications
- Improve frontend design with charts and visual analytics
- Add rate limiting and advanced security hardening

---

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Django REST Framework, Celery, Redis |
| Frontend | React, Vite, Axios |
| Database | PostgreSQL  |
| Authentication | Custom JWT |
| Task Queue | Celery with Redis broker |
| Optional | WeasyPrint / ReportLab for PDF reports |

---

## End Goal

End-users should be able to run this locally, in a Docker Container.
