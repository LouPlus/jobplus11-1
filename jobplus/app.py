from flask import Flask,render_template
from jobplus.config import configs

def create_app(config):
	
	app = Flask(__name__)
	app.config.from_object(configs.get(config))


	@app.route('/')
	def index():
		return render_template('index.html')


	return app
