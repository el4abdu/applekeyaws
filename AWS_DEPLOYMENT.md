# AWS Deployment Guide for Apple Music Key Generator

## Prerequisites
- AWS Account
- AWS CLI installed and configured
- Python 3.8+
- Git
- Project files ready

## Deployment Options

### 1. AWS Elastic Beanstalk Deployment

#### Step 1: Prepare Deployment Files
Create the following files in your project root:

##### `.ebextensions/python.config`
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: src.app:app
```

##### `requirements.txt`
(Ensure this is up to date with all dependencies)

##### `.gitignore`
```
venv/
*.pyc
*.pyo
__pycache__/
.env
.elasticbeanstalk/
```

#### Step 2: Install EB CLI
```bash
pip install awsebcli
```

#### Step 3: Initialize Elastic Beanstalk Application
```bash
eb init -p python-3.8 apple-music-key-generator -r us-east-1
```

#### Step 4: Create Environment
```bash
eb create apple-music-key-generator-env \
    --instance-type t2.micro \
    --platform python-3.8 \
    --single
```

#### Step 5: Deploy
```bash
eb deploy
```

### 2. AWS EC2 Deployment

#### Preparation
1. Launch an EC2 Instance
   - Choose Amazon Linux 2 or Ubuntu
   - Select t2.micro (free tier)
   - Create a security group allowing:
     - SSH (Port 22)
     - HTTP (Port 80)
     - HTTPS (Port 443)

#### Installation Steps
```bash
# Update system
sudo yum update -y  # For Amazon Linux
# OR
sudo apt-get update && sudo apt-get upgrade -y  # For Ubuntu

# Install Python and pip
sudo yum install python3 python3-pip -y  # Amazon Linux
# OR
sudo apt-get install python3 python3-pip -y  # Ubuntu

# Install system dependencies
sudo yum install python3-devel gcc chrome-driver -y  # Amazon Linux
# OR
sudo apt-get install python3-dev gcc chromium-chromedriver -y  # Ubuntu

# Clone your repository
git clone https://github.com/yourusername/apple-music-key-generator.git
cd apple-music-key-generator

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn

# Setup Systemd Service
sudo nano /etc/systemd/system/apple-music-key-generator.service
```

##### Systemd Service File
```ini
[Unit]
Description=Gunicorn instance for Apple Music Key Generator
After=network.target

[Service]
User=ec2-user  # or ubuntu
Group=ec2-user  # or ubuntu
WorkingDirectory=/home/ec2-user/apple-music-key-generator
Environment="PATH=/home/ec2-user/apple-music-key-generator/venv/bin"
ExecStart=/home/ec2-user/apple-music-key-generator/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:apple-music-key-generator.sock \
    -m 007 \
    src.app:app

[Install]
WantedBy=multi-user.target
```

#### Nginx Configuration
```bash
sudo yum install nginx -y  # Amazon Linux
# OR
sudo apt-get install nginx -y  # Ubuntu

sudo nano /etc/nginx/nginx.conf
```

##### Nginx Configuration
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ec2-user/apple-music-key-generator/apple-music-key-generator.sock;
    }
}
```

#### Start Services
```bash
# Enable and start services
sudo systemctl start apple-music-key-generator
sudo systemctl enable apple-music-key-generator
sudo systemctl restart nginx
```

### 3. AWS Lambda Deployment (Alternative)

#### Requirements
- Zappa for serverless deployment
- AWS Lambda and API Gateway

```bash
pip install zappa
zappa init
zappa deploy
```

## Security Recommendations
1. Use AWS Secrets Manager for sensitive configurations
2. Implement proper IAM roles
3. Use HTTPS and SSL certificates
4. Regular security updates
5. Monitor application logs

## Troubleshooting
- Check `/var/log/nginx/error.log`
- Verify Gunicorn logs
- Ensure all dependencies are installed
- Check security group settings

## Cost Optimization
- Use t2.micro for testing
- Consider spot instances
- Use AWS Free Tier
``` 