import os
import logging
from flask import Flask, render_template, jsonify
from datetime import datetime
import random
import string

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Ensure keys directory exists
os.makedirs('keys', exist_ok=True)

app = Flask(__name__)

def generate_apple_music_key(length=12):
    """
    Generate a random key similar to Apple Music redemption codes
    
    Args:
        length (int): Length of the key to generate
    
    Returns:
        str: Generated key
    """
    # Combination of uppercase letters and digits
    characters = string.ascii_uppercase + string.digits
    
    # Generate key
    key = ''.join(random.choice(characters) for _ in range(length))
    
    return key

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/generate_key')
def generate_key():
    """Generate and save a new key"""
    try:
        # Generate key
        key = generate_apple_music_key()
        
        # Save key to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'keys/redemption_key_{timestamp}.txt'
        
        with open(filename, 'w') as f:
            f.write(key)
        
        logger.info(f"Generated key: {key}")
        
        return jsonify({
            "status": "success", 
            "key": key
        })
    
    except Exception as e:
        logger.error(f"Key generation error: {e}")
        return jsonify({
            "status": "error", 
            "message": "Failed to generate key"
        }), 500

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error handler"""
    return render_template('error.html', error_code=404), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Custom 500 error handler"""
    return render_template('error.html', error_code=500), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000) 