"""
Project Chesapeake Hint Plugin for CTFd
AI-powered hint system for cybersecurity challenges
"""

from CTFd.plugins import register_plugin_assets_directory
from CTFd.plugins import register_plugin_script
from CTFd.plugins import register_plugin_stylesheet
from CTFd.plugins import register_admin_plugin_menu_bar
from CTFd.plugins import register_user_page_menu_bar
from CTFd.plugins import override_template
from CTFd.plugins import register_blueprint

from .hint_system import ai_hint_bp

def load(app):
    """Load the plugin into CTFd"""
    
    # Register the blueprint with the main app
    register_blueprint(ai_hint_bp)
    
    # Register plugin assets (if you have any CSS/JS files)
    # register_plugin_assets_directory(app, base_path="/plugins/chesapeake_hint_plugin/assets/")
    
    # Register admin menu items (optional)
    # register_admin_plugin_menu_bar(title="Chesapeake Hints", route="/admin/chesapeake")
    
    print("🔬 Project Chesapeake Hint Plugin loaded successfully!")
    print("📡 AI-powered hints available at: /api/v1/project_chesapeake/hint/<challenge_id>")
