import os
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('key_generator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AppleMusicKeyGenerator:
    def __init__(self, headless=True):
        """
        Initialize the key generator with optional headless mode.
        
        :param headless: Whether to run Chrome in headless mode
        """
        try:
            # Setup Chrome options
            chrome_options = Options()
            if headless:
                chrome_options.add_argument("--headless")  # Run in background
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")

            # Setup WebDriver
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), 
                options=chrome_options
            )
            
            # Set implicit wait to handle potential delays
            self.driver.implicitly_wait(10)
            
            logger.info("WebDriver initialized successfully")
        
        except Exception as e:
            logger.error(f"Failed to initialize WebDriver: {e}")
            raise

    def generate_key(self):
        """
        Generate an Apple Music redemption key.
        
        :return: Generated redemption key or None
        """
        try:
            # Navigate to the first URL
            logger.info("Navigating to redemption services page")
            self.driver.get("https://redeem.services.apple.com/card-apple-entertainment-offer-1-2025")
            
            # Wait and click the specific button using XPath
            logger.info("Waiting for button to be clickable")
            button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[1]/div/div/div/div[1]/div[2]/div/div[2]/button"))
            )
            button.click()
            logger.info("Button clicked successfully")

            # Navigate to the authentication URL
            logger.info("Navigating to authentication page")
            self.driver.get("https://music.apple.com/includes/commerce/authenticate?returnPath=/redeem?ctx=Music%26code=RYTR6JLXEXL3%26ign-itscg=10300%26ign-itsct=AC_MS_Music")
            
            # Extract the code (in this case, hardcoded as per your template)
            redemption_code = "RYTR6JLXEXL3"
            
            logger.info(f"Generated redemption key: {redemption_code}")
            return redemption_code

        except Exception as e:
            logger.error(f"An error occurred during key generation: {e}")
            return None

        finally:
            # Always quit the driver to free up resources
            if hasattr(self, 'driver'):
                self.driver.quit()
                logger.info("WebDriver closed")

    def save_key(self, key):
        """
        Save the generated key to a file with timestamp.
        
        :param key: Redemption key to save
        """
        try:
            # Ensure keys directory exists
            os.makedirs('keys', exist_ok=True)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'keys/redemption_key_{timestamp}.txt'
            
            with open(filename, 'w') as f:
                f.write(key)
            
            logger.info(f"Key saved to {filename}")
        
        except Exception as e:
            logger.error(f"Failed to save key: {e}")

def main():
    try:
        generator = AppleMusicKeyGenerator()
        key = generator.generate_key()
        
        if key:
            print(f"Generated Key: {key}")
            generator.save_key(key)
        else:
            print("Failed to generate key")
    
    except Exception as e:
        logger.error(f"Unexpected error in main: {e}")

if __name__ == "__main__":
    main()
