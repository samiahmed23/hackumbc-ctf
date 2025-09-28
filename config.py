# CTFd Configuration for Project Chesapeake
import os

# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///ctfd.db')

# Security
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-change-this-in-production')

# API Configuration OUR API KEY
API_KEY = os.environ.get('__API_KEY', 'AIzaSyB71X3YceZ90rNOyZqs4AlxDpSAtia-oTo')

# CTFd specific settings
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')
TEMPLATES_AUTO_RELOAD = True

# Plugin settings
PLUGINS = ['chesapeake_hint_plugin']