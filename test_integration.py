#!/usr/bin/env python3
"""
Test script to verify CTFd integration with Chesapeake hint plugin
"""

import os
import sys
import requests
import json

def test_plugin_loading():
    """Test if the plugin loads correctly"""
    try:
        from app import create_chesapeake_ctfd
        app = create_chesapeake_ctfd()
        print("✅ CTFd app created successfully")
        return app
    except Exception as e:
        print(f"❌ Failed to create CTFd app: {e}")
        return None

def test_hint_endpoint(app):
    """Test the hint endpoint"""
    try:
        with app.test_client() as client:
            # Test with a valid challenge ID
            response = client.post('/api/v1/project_chesapeake/hint/101')
            print(f"📡 Hint endpoint response status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.get_json()
                print("✅ Hint endpoint working!")
                print(f"💡 Sample hint: {data.get('hint', 'No hint generated')[:100]}...")
            else:
                print(f"⚠️  Hint endpoint returned status {response.status_code}")
                print(f"Response: {response.get_data(as_text=True)}")
                
    except Exception as e:
        print(f"❌ Failed to test hint endpoint: {e}")

def main():
    """Main test function"""
    print("🔬 Testing Project Chesapeake CTFd Integration")
    print("=" * 50)
    
    # Check API key
    api_key = os.environ.get("__API_KEY")
    if not api_key:
        print("⚠️  Warning: No API key found in environment")
        print("Set it with: $env:__API_KEY='your_key_here'")
    else:
        print(f"✅ API key found: {api_key[:10]}...")
    
    # Test plugin loading
    app = test_plugin_loading()
    if app:
        # Test hint endpoint
        test_hint_endpoint(app)
    
    print("\n🎯 Integration test complete!")

if __name__ == "__main__":
    main()
