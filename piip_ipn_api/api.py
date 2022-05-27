from piip.setup import create_application
from flask_mail import Mail

app = create_application(__name__)
mail = Mail(app)