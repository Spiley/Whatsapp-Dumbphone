import os
import subprocess
import secrets
import getpass
import sys
import shutil

npm_path = shutil.which("npm")
node_path = shutil.which("node")

def check_requirements():
    if not node_path or not npm_path:
        print("Error: Node.js is not installed or not in PATH.")
        print("Please install Node.js from https://nodejs.org/")
        sys.exit(1)

def setup_env():
    if not os.path.exists(".env"):
        print("--- First Time Setup ---")
        password = getpass.getpass("Set a password for the web interface: ")
        session_secret = secrets.token_hex(32)
        
        with open(".env", "w") as f:
            f.write(f"PASSWORD={password}\nSESSION_SECRET={session_secret}\n")
        print(".env configuration saved.")

def install_dependencies():
    print("Installing dependencies... (This downloads Chromium and may take a moment)")
    try:
        subprocess.run([npm_path, "install"], check=True)
    except subprocess.CalledProcessError:
        print("Error installing Node.js dependencies. Check your internet connection.")
        sys.exit(1)

def start_server():
    print("\nStarting WhatsApp Gateway...")
    try:
        subprocess.run([node_path, "index.js"])
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    check_requirements()
    setup_env()
    install_dependencies()
    start_server()