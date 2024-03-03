from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from .forms import EventManagerRegistrationForm, EventManagerLoginForm
from .models import EventHost
from event_manager.views import event_manager
import sqlite3

event_manager_auth = Blueprint("event_manager_auth", __name__)


@event_manager_auth.route('/host/register', methods=["GET", "POST"])
def register():
    form = EventManagerRegistrationForm()

    if request.method == "POST":
        if form.validate_on_submit():

            event_host = EventHost(
                primary_host=form.primary_host.data,
                host_email=form.host_email.data,
                organization_name=form.organization_name.data,
                organization_address=form.organization_address.data,
                organization_email=form.organization_email.data,
                password=form.password.data
            )
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO event_hosts (primary_host, host_email, organization_name, organization_address, organization_email, password) VALUES (?, ?, ?, ?, ?, ?)", (
                event_host.primary_host, event_host.host_email, event_host.organization_name, event_host.organization_address, event_host.organization_email, event_host.password))
            
            conn.commit()
            conn.close()
            return redirect(url_for("event_manager_auth.login"))
            
    return render_template("event_manager_registration.html", form=form)


@event_manager_auth.route('/host/login', methods=["GET", "POST"])
def login():
    form = EventManagerLoginForm()
    
    if request.method == "POST":
        if form.validate_on_submit():
            email = form.organization_email.data
            password = form.password.data
            
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM event_hosts WHERE organization_email=? AND password=?", (email, password))
            event_host = cursor.fetchone()
            
            if event_host:
                session['host_id'] = event_host[0]
                session['host_name'] = event_host[1]
                session['host_email'] = event_host[2]
                session['organization_name'] = event_host[3]
                session['organization_email'] = event_host[4]
                session['logged_in'] = True
                
                return redirect(url_for("event_manager.home"))
                
            else:
                flash("Invalid credentials! please try again!")
        else:
            flash("Invalid form data provided!, please try again!")
    
    return render_template("event_manager_login.html", form=form)
        
        
@event_manager_auth.route('/host/logout')
def logout():
    session.pop('host_id', None)
    session.pop('host_name', None)
    session.pop('host_email', None)
    session.pop('organization_name', None)
    session.pop('organization_email', None)
    session.pop('logged_in', None)

    return redirect(url_for('event_manager_auth.login'))
