# 🚀 Deployment Guide

## Local Development
```bash
python manage.py runserver
```
Visit: http://127.0.0.1:8000/

## Production Deployment

### 1. Environment Setup
```bash
# Set production environment
DEBUG=False
SECRET_KEY=your_production_secret_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 2. Database Setup
For production, consider using PostgreSQL:
```bash
pip install psycopg2-binary
```

### 3. Static Files
```bash
python manage.py collectstatic
```

### 4. Platform-Specific Deployments

#### Heroku
1. Create `Procfile`:
   ```
   web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn chatbot_project.wsgi
   ```
2. Add to `requirements.txt`:
   ```
   gunicorn==20.1.0
   ```

#### Railway
1. Add `railway.json`:
   ```json
   {
     "build": {
       "builder": "NIXPACKS"
     },
     "deploy": {
       "startCommand": "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:$PORT"
     }
   }
   ```

#### DigitalOcean App Platform
1. Configure via dashboard
2. Set environment variables
3. Deploy from GitHub

### 5. Security Checklist
- [ ] Set `DEBUG=False`
- [ ] Use strong `SECRET_KEY`
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up HTTPS
- [ ] Enable security middleware
- [ ] Configure database backups

### 6. Monitoring
- Set up logging
- Monitor API usage
- Track performance metrics
