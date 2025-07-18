import os
import logging
from flask import Flask, render_template, jsonify
from key_generator import AppleMusicKeyGenerator

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

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Ensure keys directory exists
os.makedirs('keys', exist_ok=True)

@app.route('/')
def index():
    """Render the main page"""
    try:
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error rendering index page: {e}")
        return "An error occurred", 500

@app.route('/generate_key')
def generate_key():
    """Generate a new Apple Music redemption key"""
    try:
        # Create generator instance
        generator = AppleMusicKeyGenerator(headless=True)
        
        # Attempt to generate key
        key = generator.generate_key()
        
        if key:
            # Save the key
            generator.save_key(key)
            
            logger.info(f"Successfully generated key: {key}")
            return jsonify({"status": "success", "key": key})
        else:
            logger.warning("Key generation failed")
            return jsonify({"status": "error", "message": "Failed to generate key"}), 500
    
    except Exception as e:
        logger.error(f"Unexpected error in key generation: {e}")
        return jsonify({"status": "error", "message": "An unexpected error occurred"}), 500

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error handler"""
    logger.warning(f"404 error: {e}")
    return render_template('error.html', error_code=404), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Custom 500 error handler"""
    logger.error(f"500 error: {e}")
    return render_template('error.html', error_code=500), 500

if __name__ == '__main__':
    # Ensure debug mode is off in production
    app.run(debug=False, host='0.0.0.0', port=5000)
