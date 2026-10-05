'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student: 
Description: Project 1 - GPA Calculator
'''

from app import app, db
from app.models import User, Course, Enrollment
from app.forms import SignUpForm, LoginForm, EnrollmentForm, DeleteEnrollmentForm
from gpa_calculator import calculate_gpa
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
import bcrypt

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/users/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit() and form.passwd.data == form.passwd_confirm.data and not db.session.get(User, form.id.data):
        hashed = bcrypt.hashpw(form.passwd.data.encode('utf-8'), bcrypt.gensalt())
        user = User(id=form.id.data, name=form.name.data, about=form.about.data, passwd=hashed)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('list_enrollments'))
    return render_template('signup.html', form=form)

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.get(User, form.id.data)
        if user and bcrypt.checkpw(form.passwd.data.encode('utf-8'), user.passwd):
            login_user(user)
            return redirect(url_for('list_enrollments'))
    return render_template('login.html', form=form)

@app.route('/users/signout', methods=['GET', 'POST'])
@login_required
def signout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/enrollments')
@login_required
def list_enrollments():
    delete_form = DeleteEnrollmentForm()
    gpa = calculate_gpa(current_user.enrollments)
    return render_template('enrollments.html', enrollments=current_user.enrollments, gpa=gpa, delete_form=delete_form)

@app.route('/enrollments/delete/<course_prefix>/<course_number>', methods=['POST'])
@login_required
def delete_enrollment(course_prefix, course_number):
    enrollment = db.session.get(Enrollment, (current_user.id, course_prefix, course_number))
    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
    return redirect(url_for('list_enrollments'))

@app.route('/enrollments/create', methods=['GET', 'POST'])
@login_required
def create_enrollment():
    form = EnrollmentForm()
    enrolled = {(e.course_prefix, e.course_number) for e in current_user.enrollments}
    available_courses = [c for c in Course.query.all() if (c.prefix, c.number) not in enrolled]
    form.course.choices = [(f'{c.prefix}|{c.number}', f'{c.prefix} {c.number} - {c.name}') for c in available_courses]
    if form.validate_on_submit():
        prefix, number = form.course.data.split('|')
        db.session.add(Enrollment(user_id=current_user.id, course_prefix=prefix, course_number=number, grade=form.grade.data))
        db.session.commit()
        return redirect(url_for('list_enrollments'))
    return render_template('create_enrollment.html', form=form)
