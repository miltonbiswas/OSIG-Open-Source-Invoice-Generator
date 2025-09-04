from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Invoice

@app.route('/')
def home():
    return redirect(url_for('new_invoice'))

@app.route('/invoice/new')
def new_invoice():
    return render_template('new_invoice.html')

@app.route('/invoice/preview', methods=['POST'])
def preview_invoice():
    data = request.form
    try:
        amount = float(data['amount'])
        tax = float(data['tax'])
    except ValueError:
        amount = 0
        tax = 0
    total = amount + tax
    return render_template('preview_invoice.html', data=data, total=total)

@app.route('/save_invoice', methods=['POST'])
def save_invoice():
    data = request.form
    try:
        bill_date = datetime.strptime(data['bill_date'], '%Y-%m-%d')
        amount = float(data['amount'])
        tax = float(data['tax'])
        total = amount + tax
    except (ValueError, KeyError):
        return "Invalid input", 400

    invoice = Invoice(
        business_name=data['business_name'],
        owner_name=data['owner_name'],
        bill_by=data['bill_by'],
        billed_to=data['billed_to'],
        bill_date=bill_date,
        description=data['description'],
        amount=amount,
        tax=tax,
        total=total
    )
    db.session.add(invoice)
    db.session.commit()

    return render_template('preview_invoice.html', data=data, total=total)

@app.route('/invoices')
def list_invoices():
    invoices = Invoice.query.order_by(Invoice.created_at.desc()).all()
    return render_template('invoice_list.html', invoices=invoices)

@app.route('/invoice/<int:id>')
def view_invoice(id):
    invoice = Invoice.query.get_or_404(id)

    # Convert SQLAlchemy object to dictionary for template
    data = {
        'business_name': invoice.business_name,
        'owner_name': invoice.owner_name,
        'bill_by': invoice.bill_by,
        'billed_to': invoice.billed_to,
        'bill_date': invoice.bill_date.strftime('%Y-%m-%d'),
        'description': invoice.description,
        'amount': invoice.amount,
        'tax': invoice.tax,
        'advance': invoice.advance,
        'payment_method': invoice.payment_method,
        'payer_name': invoice.payer_name
    }

    total = invoice.total
    outstanding = total - invoice.advance

    return render_template('preview_invoice.html', data=data, total=total, outstanding=outstanding)


@app.route('/invoice/<int:id>/delete', methods=['POST'])
def delete_invoice(id):
    invoice = Invoice.query.get_or_404(id)
    db.session.delete(invoice)
    db.session.commit()
    return redirect(url_for('list_invoices'))


if __name__ == '__main__':
    app.run(debug=True)
