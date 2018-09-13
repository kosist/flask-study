import os

class Config(object):
	"""docstring for Config"""
	#TODO: move SECRET_KEY and database related keys to system environment
	SECRET_KEY = 'cd2af2fde129b2e4767758673c7c33d9'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'in-v3.mailjet.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	# import data from system environment variables
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASS')
		