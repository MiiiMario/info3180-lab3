"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, mail
from flask import render_template, request, redirect, url_for, flash
from forms import MyForm
from flask_mail import Message

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/contact', methods=["POST","GET"])
def contact():
    myform=MyForm()
    """Render the website's contact page."""
    if request.method == 'POST' and myform.validate_on_submit():
        send_mail(myform.name.data,myform.email.data,myform.subject.data,myform.message.data)
        flash('Message Successfully Sent')
        return redirect(url_for('home'))
    else:
        return render_template('contact.html',form=myform,addtext='Error sending')
 
def send_mail(name,email,subject,message):
	msg = Message(subject, sender=(name,email), recipients=["to@example.com"])
	msg.body = message
	mail.send(msg)  
	
@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
