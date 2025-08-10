# 🤖 Django Gemini AI Chatbot

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-v4.2+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A modern, responsive chatbot powered by **Google's Gemini AI** with a clean Django backend and beautiful web interface.

## ✨ Features

- 🤖 **Google Gemini AI Integration** - Powered by the latest Gemini 1.5 Flash model
- 📱 **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- 💬 **Real-time Chat** - Instant responses with typing indicators
- 💾 **Chat History** - All conversations saved in database
- 🎨 **Modern UI** - Beautiful gradient design with smooth animations
- ⚡ **Fast & Lightweight** - Optimized for performance
- 🔒 **Secure** - Environment-based configuration
- 🆓 **Free to Use** - Generous Gemini API free tier

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API key ([Get it here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-gemini-chatbot.git
   cd django-gemini-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   # Edit .env file and add your Gemini API key
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```

4. **Setup database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the application**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser**
   ```
   http://127.0.0.1:8000/
   ```

## 🔧 Configuration

### Environment Variables

Edit the `.env` file:

```env
# Get your API key from: https://makersuite.google.com/app/apikey
GEMINI_API_KEY=your_gemini_api_key_here

# Generate a new secret key for production
SECRET_KEY=your_django_secret_key_here

# Set to False in production
DEBUG=True
```

### Getting Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key to your `.env` file

## 📁 Project Structure

```
django-gemini-chatbot/
├── 📁 chatbot_project/          # Django project settings
│   ├── settings.py              # Main configuration
│   ├── urls.py                  # URL routing
│   └── ...
├── 📁 chatbot/                  # Main application
│   ├── models.py                # Database models
│   ├── views.py                 # API endpoints
│   ├── admin.py                 # Admin interface
│   └── ...
├── 📁 templates/                # HTML templates
│   └── chatbot/
│       └── index.html           # Main chat interface
├── 📁 static/                   # Static files
├── 📄 manage.py                 # Django management
├── 📄 requirements.txt          # Python dependencies
├── 📄 .env                      # Environment variables
└── 📄 README.md                 # This file
```

## 🎨 Screenshots

### Desktop View
The chatbot features a modern, gradient-based design with smooth animations and a responsive layout.

### Mobile View
Fully responsive design that works seamlessly on all mobile devices.

## 🛠️ Tech Stack

- **Backend**: Django 4.2+
- **AI Model**: Google Gemini 1.5 Flash
- **Database**: SQLite (default) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **HTTP Client**: Python Requests

## 🔧 Customization

### Changing AI Model
Edit `chatbot/views.py` to use different Gemini models:
```python
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
```

### Styling
Modify the CSS in `templates/chatbot/index.html` to customize:
- Colors and gradients
- Animations and transitions
- Layout and spacing

### Adding Features
- **User Authentication**: Extend models for user-specific chats
- **File Uploads**: Add support for image/document analysis
- **Voice Chat**: Integrate speech-to-text and text-to-speech
- **Chat Export**: Add functionality to export conversations

## 🚀 Deployment

### Local Development
```bash
python manage.py runserver
```

### Production Deployment
1. Set `DEBUG=False` in `.env`
2. Generate a new `SECRET_KEY`
3. Configure your database (PostgreSQL recommended)
4. Set up static files serving
5. Deploy to your preferred platform (Heroku, Railway, DigitalOcean, etc.)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Gemini AI](https://ai.google.dev/) for the powerful AI model
- [Django](https://www.djangoproject.com/) for the robust web framework
- The open-source community for inspiration and tools

## 📞 Support

If you have any questions or run into issues:

- 📧 **Email**: dilan4524melvin@gmail.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/dilanmelvin/Django_Chatbot/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/dilanmelvin/Django_Chatbot/discussions)

---

<div align="center">
  <strong>⭐ Star this repository if you found it helpful!</strong>
</div>

<div align="center">
  Made with ❤️ and 🤖 AI
</div>
