from app import db
from datetime import datetime

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
    total = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)