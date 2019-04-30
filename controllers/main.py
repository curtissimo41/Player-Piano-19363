from flask import Blueprint, render_template

# controller for default / url prefix
homepage = Blueprint('homepage', __name__, template_folder = 'templates')

# Main view that shows homepage.html
@homepage.route('/',methods=['GET'])
def main_view():
	return render_template('homepage.html')
