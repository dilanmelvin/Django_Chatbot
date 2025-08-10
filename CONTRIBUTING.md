# Contributing to Django Gemini Chatbot

Thank you for considering contributing to this project! 🎉

## How to Contribute

### 🐛 Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourusername/django-gemini-chatbot/issues)
2. If not, create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment details (Python version, OS, etc.)

### 💡 Suggesting Features

1. Check existing [Issues](https://github.com/yourusername/django-gemini-chatbot/issues) for similar suggestions
2. Create a new issue with:
   - Clear description of the feature
   - Use case/motivation
   - Possible implementation approach

### 🔧 Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/django-gemini-chatbot.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   ```bash
   python manage.py test
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add: your feature description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Provide clear description of changes
   - Reference any related issues
   - Add screenshots if UI changes

## Development Setup

1. **Clone and setup**
   ```bash
   git clone https://github.com/yourusername/django-gemini-chatbot.git
   cd django-gemini-chatbot
   pip install -r requirements.txt
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Add your Gemini API key
   ```

3. **Setup database**
   ```bash
   python manage.py migrate
   ```

4. **Run development server**
   ```bash
   python manage.py runserver
   ```

## Code Style Guidelines

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions small and focused
- Use type hints where appropriate

## Areas for Contribution

- 🎨 **UI/UX improvements**
- 🔧 **New features** (voice chat, file uploads, etc.)
- 🐛 **Bug fixes**
- 📚 **Documentation**
- 🧪 **Tests**
- 🌐 **Internationalization**
- ⚡ **Performance optimizations**

## Questions?

Feel free to ask questions in:
- [GitHub Discussions](https://github.com/yourusername/django-gemini-chatbot/discussions)
- [Issues](https://github.com/yourusername/django-gemini-chatbot/issues) with "question" label

Thank you for contributing! 🚀
