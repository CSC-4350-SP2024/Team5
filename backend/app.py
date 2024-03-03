
from flask import Flask
from init_db import init_db
from auth.user.views import auth
from auth.event_manager.views import event_manager_auth
from event_manager.views import event_manager
from event_guest.views import event_guest


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.register_blueprint(auth)
app.register_blueprint(event_manager_auth)
app.register_blueprint(event_manager)
app.register_blueprint(event_guest)

init_db()


if __name__ == '__main__':
    app.run(debug=True)
