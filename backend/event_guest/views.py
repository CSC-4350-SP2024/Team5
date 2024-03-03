from flask import Blueprint, render_template, redirect, request, url_for, session
from .services import EventGuestServices

event_guest = Blueprint("event_guest", __name__)
event_guest_services = EventGuestServices()

@event_guest.route('/notifications')
def check_notifications():
    
    unread_messages = event_guest_services.get_unread_notifications(session["user_id"])
    return render_template("user_notifications.html", unread_messages=unread_messages)

@event_guest.route('/update_message_status', methods=["POST"])
def update_message_status():
    if request.method == "POST":
        message_id = request.form.get('message_id')
        event_guest_services.update_message_status(message_id)
        
    return redirect(url_for("event_guest.check_notifications"))