# Apple Music Key Generator Web Application

## Overview
A modern web application for generating Apple Music redemption keys using Selenium WebDriver and Flask.

## 🚀 Features
- Automated key generation
- Modern, responsive web interface
- Robust error handling
- Logging and key tracking
- Easy deployment

## 🛠 Technologies
- Python 3.8+
- Selenium WebDriver
- Flask
- Chrome WebDriver
- HTML5
- CSS3
- JavaScript (ES6+)

## 🔧 Prerequisites
- Python 3.8 or higher
- Chrome Browser
- ChromeDriver
- pip (Python package manager)
- AWS Account (for cloud deployment)

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/apple-music-key-generator.git
cd apple-music-key-generator
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### Development Mode
```bash
python src/app.py
```

### Production Deployment Options

#### 1. AWS Elastic Beanstalk
```bash
# Install EB CLI
pip install awsebcli

# Initialize and create environment
eb init -p python-3.8 apple-music-key-generator -r us-east-1
eb create apple-music-key-generator-env
eb deploy
```

#### 2. AWS EC2
1. Launch EC2 Instance
2. Configure security groups
3. Follow deployment steps in `AWS_DEPLOYMENT.md`

#### 3. AWS Lambda (Serverless)
```bash
# Install Zappa
pip install zappa

# Initialize and deploy
zappa init
zappa deploy production
```

## 🔒 Security Considerations
- Use in a controlled environment
- Respect Apple's Terms of Service
- Implement additional authentication if needed
- Use AWS IAM roles and security groups
- Enable HTTPS and SSL

## 📝 Logging
Logs are generated in:
- `key_generator.log`: Selenium WebDriver logs
- `app.log`: Flask application logs
- AWS CloudWatch (for cloud deployments)

## 🐛 Troubleshooting
- Ensure Chrome and ChromeDriver versions match
- Check logs for detailed error information
- Verify network connectivity
- Review AWS deployment logs

## 🚧 Limitations
- Depends on specific web page structure
- Requires manual updates if Apple changes website
- Potential compliance issues with automated key generation

## 📄 License
[Specify your license here]

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📧 Contact
[Your contact information]

---

**Disclaimer**: This tool is for educational purposes only. Always respect the terms of service of the platforms you interact with.
