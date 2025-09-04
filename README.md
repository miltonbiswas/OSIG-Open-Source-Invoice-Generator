# OSIG-Open-Source-Invoice-Generator
## 📌 Overview
OSIG: Invoice Generator is a lightweight, browser-based billing tool built with Python (Flask), Bootstrap, and SQLite. It allows users to create, preview, print, and store professional invoices locally — with no external dependencies or cloud storage.

## 🚀 Features
  * Create invoices with business and client details
  * Preview invoices in a styled, print-ready format
  * Save invoices to local SQLite database
  * View and manage saved invoices
  * Responsive UI with Bootstrap 5
  * Offline-first architecture — no internet required

## 🧱 Tech Stack
| Layer | Technology |
|----------------|----------------|
| Backend | Python + Flash |
| Database | SQLite(Local) |
| Frontend | HTML + Bootstrap |
| Templating | Jinja2 |

## 📁 Folder Structure
```
OSIG/
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── base.html
│   ├── new_invoice.html
│   ├── preview_invoice.html
│   ├── invoice_list.html
├── models.py
├── app.py
├── database.db

```

## 🧩 Data Model (models.py)
```
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(100))
    owner_name = db.Column(db.String(100))
    bill_by = db.Column(db.String(100))
    billed_to = db.Column(db.String(100))
    bill_date = db.Column(db.Date)
    description = db.Column(db.Text)
    amount = db.Column(db.Float)
    tax = db.Column(db.Float)
    advance = db.Column(db.Float)
    total = db.Column(db.Float)
    payment_method = db.Column(db.String(100))
    payer_name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

## 🌐 Routes Overview
| Route | Method | Description |
|-----|-----|-----|
| `/` | GET | Redirects to invoice creation |
| `/invoice/new` |	GET	| Displays invoice form |
| `/invoice/preview` |	POST	| Shows styled invoice preview |
| `/save_invoice` | POST | Save invoice to Database |
| `/invoices` | GET | Lists saved invoices |
| `/invoice/<id>` | GET | Views a specific invoice |
| `/invoice/<id>/delete` | POST | Deletes a specific invoice |

## 🖨️ Invoice Workflow
1. Create Invoice → `/invoice/new`
2. Preview Invoice → `/invoice/preview`
3. Print or Save → `/save_invoice`
4. View Saved Invoices → `/invoices`
5. Reprint or Delete → `/invoice/<id>`

## 🛠️ Setup Instructions
### 1. Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate  # Windows
```
### 2. Install Dependencies
```
pip install flask flask_sqlalchemy
```
### 3. Initialize Database
```
from app import app, db
with app.app_context():
    db.create_all()
```
### 4. Run the App
```
python app.py
```

###📌 Notes
* All data is stored locally in database.db
* No external APIs or cloud services used
* Designed for small businesses and personal use
* Easily customizable for branding, invoice numbering, or PDF export

  ## 📬 Contact
I'm always open to collaborating on projects or just having a chat!  

Designed and Developed by **Milton Biswas**  
📍 Abu Road, Rajasthan, India  
📧 Email: miltonbiswasdev@gmail.com  
🌐 GitHub: [github.com/miltonbiswas](https://github.com/miltonbiswas)  
💼 LinkedIn: [linkedin.com/in/xmiltonbiswas](https://linkedin.com/in/xmiltonbiswas)  
🐦 Twitter: [twitter.com/miltonbiswas](https://twitter.com/miltonbiswas)
📸 Instagram: [instagram.com/miltonbiswasx](https://instagram.com/miltonbiswasx)

<p align="left">
  <a href="https://linkedin.com/in/xmiltonbiswas" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-%230A66C2.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://twitter.com/miltonbiswasx" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />
  </a>
  <a href="https://instagram.com/miltonbiswasx" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white" />
  </a>
  <a href="https://github.com/miltonbiswas" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white" />
  </a>
    <a href="https://threads.net/@miltonbiswasx" target="_blank">
    <img src="https://img.shields.io/badge/Threads-%23111111.svg?&style=for-the-badge&logo=threads&logoColor=white" />
  </a>
</p>
