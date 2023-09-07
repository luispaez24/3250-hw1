from app import app
from flask import render_template, redirect, url_for, request
from app.forms import InvoiceForm

@app.route('/')
@app.route('/invoices')
@app.route('/index.html')
def list_invoices():
    return render_template("index.html", title=app.config['TITLE'], invoices=app.config['INVOICES'])

@app.route('/invoices/create', methods=['GET','POST'])
def create_invoice():
    form = InvoiceForm()
    if form.validate_on_submit():
       
        app.config['INVOICES'].append(
            {
                'number': form.number.data,
                'title': form.title.data,  
                'client_name': form.client_name.data,  
                'phone_number': form.phone_number.data,  
                'due_date': form.due_date.data,
            }
        )
        return redirect(url_for('list_invoices'))
    else:
        return render_template('invoices_create.html', title=app.config['TITLE'], form=form)

