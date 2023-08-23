# main.py
from flask import Flask, redirect, render_template, request, url_for, flash

app = Flask(__name__)
app.secret_key = "nicschoolwebsite"

admission_data = []
admission_id_count = 1

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/admission', methods=['GET', 'POST'])
def admission():
    global admission_id_count

    if request.method == 'POST':
        admission_data.append({
            'id': admission_id_count,
            'name': request.form['name'],
            'email': request.form['email'],
            'course': request.form['course']
        })
        admission_id_count += 1
        flash('Admission form submitted successfully!', 'success')
        return redirect(url_for('admission'))

    return render_template('admission.html', admission_data=admission_data)

@app.route('/edit_admission/<int:id>', methods=['GET', 'POST'])
def edit_admission(id):
    if request.method == 'POST':
        edited_data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'course': request.form['course']
        }

        for admission_entry in admission_data:
            if admission_entry['id'] == id:
                admission_entry.update(edited_data)
                flash('Admission form updated successfully!', 'success')
                return redirect(url_for('admission'))

    for admission_entry in admission_data:
        if admission_entry['id'] == id:
            return render_template('edit_admission.html', admission_entry=admission_entry)

    flash('Admission entry not found!', 'error')
    return redirect(url_for('admission'))

@app.route('/delete_admission/<int:id>', methods=['GET', 'POST'])
def delete_admission(id):
    for admission_entry in admission_data:
        if admission_entry['id'] == id:
            admission_data.remove(admission_entry)
            flash('Admission form deleted successfully!', 'success')
            return redirect(url_for('admission'))

    flash('Admission entry is not found!', 'error')
    return redirect(url_for('admission'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Do something with the form data, e.g., save to a database or send an email
        # Replace the print statements with your desired actions.
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")

        return "Form submitted successfully!"
    else:
        return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
