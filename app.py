#!/usr/bin/env python3
"""
CTFd Application with Project Chesapeake Hint Plugin
"""

import os
from CTFd import create_app
from CTFd.plugins import init_plugins

def create_chesapeake_ctfd():
    """Create CTFd application with Chesapeake hint plugin"""
    
    # Set up environment
    os.environ.setdefault('CTFD_CONFIG', 'config.py')
    
    # Create the CTFd app
    app = create_app()
    
    # Initialize plugins (this will load our Chesapeake hint plugin)
    init_plugins(app)
    
    return app

if __name__ == '__main__':
    app = create_chesapeake_ctfd()
    
    print("🔬 Project Chesapeake CTFd Server Starting...")
    print("📡 AI Hint System: ACTIVE")
    print("🌐 Server will be available at: http://localhost:4000")
    print("🔑 Make sure your API key is set: $env:__API_KEY='your_key_here'")
    print("-" * 60)
    
    # Run the development server
    app.run(host='0.0.0.0', port=4000, debug=True)
