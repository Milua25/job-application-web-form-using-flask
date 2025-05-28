from flask import Flask, render_template, url_for, request, flash
from flask_mail import Mail, message
from flask_sqlalchemy import SQLAlchemy
from config  import Config
from datetime import datetime

#
# def send_mail(subject, sender, recipients, first_name, last_name, email, date):
#     msg = Message(subject, sender=sender, recipients=recipients)
#     message_body = f"""
#     Thank you for submitting your job!, {first_name}.
#     Here are the details you submitted:
#         {first_name}\n{last_name}\n{email}\n{date}
#     """


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app=app)
mail = Mail(app)
from models import Form

@app.route('/job', methods=['GET', 'POST'])
def job_application():# put application's code here
    print(request.method)
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date = request.form['date']
        date = datetime.strptime(date, '%Y-%m-%d')
        occupation = request.form['occupation']
        form = Form(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date=date,
            occupation=occupation
        )
        db.session.add(form)
        db.session.commit()
        db.session.close()

        # message = Message(subject="New Job Application Submitted",
        #                   sender=app.config['MAIL_USERNAME'],
        #                   recipients=[email],
        #                   body =message_body)
        #mail.send(message)
        flash("Your form was successfully submitted")
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/')
def index():
    return f"<a href={url_for('job_application')}>Job Application</a>"

with app.app_context():
    db.create_all()

if __name__ == 'app':
        app.run(debug=True)
