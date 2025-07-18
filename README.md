# Apple Music Key Generator Web Application

## 🌐 Overview
A simple, modern web application for generating random keys with a clean, responsive design.

## ✨ Features
- Generate random keys
- Copy to clipboard functionality
- Responsive design
- Error handling
- Logging

## 🛠 Technologies
- Python
- Flask
- HTML5
- CSS3
- JavaScript (ES6+)

## 📦 Prerequisites
- Python 3.8+
- pip

## 🚀 Installation

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/apple-music-key-generator.git
cd apple-music-key-generator
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🖥️ Running the Application

### Development Mode
```bash
python app.py
```

### Production Mode
```bash
# Using Gunicorn
gunicorn --bind 0.0.0.0:5000 app:app
```

## 🌈 Customization
- Modify `static/css/styles.css` to change design
- Update `app.py` to change key generation logic

## 🔒 Security
- Keys are saved with timestamps
- Basic error handling
- Logging implemented

## 📝 Logging
Logs are saved in `app.log`

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to the branch
5. Create Pull Request

## 📄 License
[Specify your license]

## 🚧 Limitations
- Simple key generation
- No persistent storage
- Minimal error handling

---

**Disclaimer**: Use responsibly and respect terms of service.
