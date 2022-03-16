"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from app.forms import PropertyForm
from app.model import Properties
from werkzeug.utils import secure_filename
import os



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
    return render_template('about.html', topic="Not only allowing you to to find your dream house. We also provide you with the best deals on the market.")

@app.route('/properties/create', methods=['GET', 'POST'])
def properties():
    form = PropertyForm()
    if request.method == 'POST' and form.validate():
        Title = request.form['property_title']
        Description = request.form['property_description']
        Rooms = request.form['noOfRooms']
        Bathrooms = request.form['noOfBathrooms']
        Price = request.form['property_price']
        Location = request.form['property_location']
        Type = request.form['property_type']
        image = form.property_image.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_property = Properties(Title, Description, Rooms, Bathrooms, Price, Location, Type, filename)
        db.session.add(new_property)
        db.session.commit()
        flash('New Property added!', 'success')
        return redirect(url_for('property_list'))
    else:
        flash_errors(form)
    return render_template('add_properties.html', form=form)

@app.route('/properties')
def property_list():
    properties = db.session.query(Properties).all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<int:id>')
def property_detail(id):
    property = db.session.query(Properties).get(id)
    return render_template('property_detail.html', property=property)

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

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
    app.run(debug=True,host="0.0.0.0",port="8080")
