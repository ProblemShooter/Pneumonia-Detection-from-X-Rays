# Pneumonia Detection - Production Deployment Guide

## Overview

This guide explains how to deploy your Flask pneumonia detection application to production so others can access it through the internet using a browser.

---

## Deployment Options Comparison

| Platform | Cost | Ease | Speed | Best For |
|----------|------|------|-------|----------|
| **Heroku** | Free → $7/month | ⭐⭐⭐⭐⭐ | 15 mins | Quick demo, learning |
| **Render** | Free → $7/month | ⭐⭐⭐⭐⭐ | 15 mins | Modern alternative to Heroku |
| **Replit** | Free → $7/month | ⭐⭐⭐⭐⭐ | 10 mins | Easiest for beginners |
| **PythonAnywhere** | Free → $5/month | ⭐⭐⭐⭐ | 20 mins | Python-specific hosting |
| **AWS EC2** | $5-15/month | ⭐⭐⭐ | 30 mins | Scalable, enterprise |
| **DigitalOcean** | $5/month | ⭐⭐⭐ | 25 mins | Balanced, reliable |
| **Google Cloud** | Free trial | ⭐⭐⭐ | 30 mins | Enterprise, powerful |
| **Docker + AWS/GCP** | Variable | ⭐⭐ | 45 mins | Production-grade |

**⚡ Fastest & Easiest: Replit or Render (15 mins, free)**

---

# Option 1: Deploy on Replit (FASTEST - 10 Minutes)

## What is Replit?
Replit is a cloud IDE that runs code directly online. No configuration needed!

## Step 1: Create Replit Account
1. Go to https://replit.com
2. Click "Sign up"
3. Use Google/GitHub account
4. Complete setup

## Step 2: Create New Replit
1. Click "Create Replit" button
2. Choose "Import from GitHub"
3. Paste your repository URL (if on GitHub) OR select "Python" template
4. Name it: `pneumonia-detection`
5. Click "Create Replit"

## Step 3: Upload Your Files
**If NOT using GitHub:**
1. Click "Upload file" button
2. Upload these folders:
   ```
   Flask Application/
   ├── app.py
   ├── templates/
   ├── static/
   └── uploads/ (create empty folder)
   
   model_weights/
   ├── vgg19_model_02.h5
   ```
3. Keep folder structure same

## Step 4: Install Dependencies
1. In the terminal at bottom, run:
```bash
pip install flask tensorflow pillow opencv-python numpy werkzeug
```

2. Wait for installation (2-3 minutes)

## Step 5: Modify app.py for Replit

Replace this line in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=False, threaded=False, use_reloader=False)
```

With:
```python
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, threaded=False, use_reloader=False)
```

## Step 6: Run the Application
1. Click the "Run" button (green play button at top)
2. Terminal shows: `Running on http://0.0.0.0:5000`
3. Click the "Open in new tab" link that appears
4. Share this URL with anyone!

## URL Format
Your public URL will be:
```
https://pneumonia-detection.username.repl.co
```

## Advantages
✅ Free tier available
✅ No server management
✅ Instant deployment
✅ Public URL automatically
✅ No credit card needed (for free tier)

## Limitations
❌ Free tier sleeps after 1 hour inactivity
❌ Paid tier: $7/month minimum
❌ Limited processing power
❌ Not ideal for heavy traffic

---

# Option 2: Deploy on Render (Professional - 15 Minutes)

## What is Render?
Modern hosting platform, better than Heroku for free tier. Hosted on AWS infrastructure.

## Step 1: Prepare Your Code

Create a `requirements.txt` file in project root:
```
Flask==2.3.0
tensorflow==2.13.0
Pillow==10.0.0
opencv-python==4.8.0.74
numpy==1.24.3
Werkzeug==2.3.0
gunicorn==21.2.0
```

## Step 2: Create Render Account
1. Go to https://render.com
2. Click "Sign up"
3. Connect with GitHub (recommended) or email
4. Verify email

## Step 3: Create Web Service

1. Click "New +" button
2. Select "Web Service"
3. Connect your GitHub repository
   - If code not on GitHub, connect via GitHub and push your code
   - OR use "Deploy via Git URL" option

## Step 4: Configure Deployment Settings

**Fill in these fields:**

| Field | Value |
|-------|-------|
| **Name** | pneumonia-detection |
| **Environment** | Python 3 |
| **Region** | Singapore/India (closest) |
| **Branch** | main |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn -w 4 -b 0.0.0.0:$PORT 'Flask Application.app:app'` |

## Step 5: Environment Variables

1. Scroll to "Environment Variables" section
2. Add (optional, for security):
```
FLASK_ENV = production
TF_CPP_MIN_LOG_LEVEL = 2
```

## Step 6: Deploy

1. Click "Create Web Service"
2. Render builds and deploys (takes 3-5 minutes)
3. Shows green status when done
4. Your URL: `https://pneumonia-detection.onrender.com`

## Step 7: Test Deployment

1. Click the URL
2. Upload X-ray image
3. Verify prediction works

## URL Format
```
https://pneumonia-detection.onrender.com
```

## Advantages
✅ Free tier with 750 hours/month
✅ No credit card for free
✅ Automatic deployments from GitHub
✅ Better performance than Replit
✅ Automatic HTTPS/SSL

## Limitations
❌ Free tier goes to sleep after 15 mins inactivity
❌ $7/month for always-on hosting
❌ Cold start delay on free tier

---

# Option 3: Deploy on Heroku (Classic but Changed)

**⚠️ Note:** Heroku removed free tier in Nov 2022. Minimum cost is $5/month.

## Alternative: Use Heroku CLI for Development

If you have Heroku credits, here's how:

## Step 1: Install Heroku CLI
```bash
# macOS
brew install heroku/brew/heroku

# Linux
curl https://cli-assets.heroku.com/install.sh | sh

# Windows
choco install heroku-cli
```

## Step 2: Create requirements.txt
```
Flask==2.3.0
tensorflow==2.13.0
Pillow==10.0.0
opencv-python==4.8.0.74
numpy==1.24.3
Werkzeug==2.3.0
gunicorn==21.2.0
```

## Step 3: Create Procfile

In project root, create file named `Procfile` (no extension):
```
web: gunicorn -w 1 -b 0.0.0.0:$PORT "Flask Application.app:app"
```

## Step 4: Create runtime.txt

Specify Python version:
```
python-3.11.4
```

## Step 5: Deploy via Terminal

```bash
# Login to Heroku
heroku login

# Create new app
heroku create pneumonia-detection

# Push code to Heroku
git push heroku main

# View logs
heroku logs --tail
```

## URL Format
```
https://pneumonia-detection.herokuapp.com
```

---

# Option 4: Deploy on AWS EC2 (Production-Grade)

## What is AWS EC2?
Virtual server in Amazon cloud. More control, suitable for production.

## Step 1: Create AWS Account
1. Go to https://aws.amazon.com
2. Click "Create AWS Account"
3. Fill details, add payment method
4. Verify

## Step 2: Launch EC2 Instance

1. Go to EC2 Dashboard
2. Click "Launch Instance"
3. **Choose AMI:** Ubuntu 22.04 LTS (free tier eligible)
4. **Instance Type:** t2.micro (free tier)
5. **Key Pair:** Create new
   - Name: `pneumonia-detection-key`
   - Download `.pem` file (keep safe!)
6. **Security Group:** 
   - Allow SSH (port 22)
   - Allow HTTP (port 80)
   - Allow HTTPS (port 443)
   - Allow TCP port 5000 (temporary)
7. Click "Launch"

## Step 3: Connect to Instance

**On macOS/Linux:**
```bash
chmod 400 pneumonia-detection-key.pem
ssh -i pneumonia-detection-key.pem ubuntu@<your-ec2-public-ip>
```

**On Windows:**
Use PuTTY:
1. Download PuTTY
2. Convert .pem to .ppk using PuTTYgen
3. Open PuTTY connection with .ppk file

## Step 4: Install Requirements

```bash
# Update system
sudo apt update
sudo apt upgrade -y

# Install Python and dependencies
sudo apt install -y python3-pip python3-venv git

# Install system dependencies for OpenCV
sudo apt install -y libsm6 libxext6 libxrender-dev

# Clone repository (if on GitHub)
git clone https://github.com/yourusername/pneumonia-detection.git
cd pneumonia-detection
```

## Step 5: Setup Python Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt
```

## Step 6: Install Nginx (Reverse Proxy)

```bash
sudo apt install -y nginx
```

## Step 7: Configure Nginx

Create `/etc/nginx/sites-available/pneumonia-detection`:

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/pneumonia-detection /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## Step 8: Setup Systemd Service

Create `/etc/systemd/system/pneumonia-detection.service`:

```ini
[Unit]
Description=Pneumonia Detection Flask App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/pneumonia-detection
ExecStart=/home/ubuntu/pneumonia-detection/venv/bin/python app.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start service:
```bash
sudo systemctl enable pneumonia-detection
sudo systemctl start pneumonia-detection
sudo systemctl status pneumonia-detection
```

## Step 9: Get Domain Name (Optional)

1. Buy domain from:
   - Route53 (AWS)
   - GoDaddy
   - Namecheap
   - Google Domains

2. Point domain to EC2 Elastic IP

## Step 10: Setup HTTPS/SSL

```bash
# Install Certbot
sudo apt install -y certbot python3-certbot-nginx

# Get free SSL certificate
sudo certbot certonly --nginx -d your-domain.com

# Auto-renew
sudo systemctl enable certbot.timer
```

## URL Format
```
https://your-domain.com
or
http://your-ec2-public-ip
```

## Advantages
✅ Full control
✅ Scalable
✅ Production-grade
✅ Cheap (free tier 1 year)
✅ Good for learning

## Limitations
❌ Manual server management
❌ Need SSH knowledge
❌ More configuration
❌ Security responsibility

---

# Option 5: Docker + AWS ECS (Enterprise)

## What is Docker?
Containerizes your app with all dependencies. Guarantees it runs same everywhere.

## Step 1: Create Dockerfile

In project root, create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsm6 libxext6 libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 5000

# Run app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "Flask Application.app:app"]
```

## Step 2: Create .dockerignore

```
venv
__pycache__
*.pyc
.git
.gitignore
README.md
```

## Step 3: Build Docker Image

```bash
docker build -t pneumonia-detection:latest .
```

## Step 4: Test Locally

```bash
docker run -p 5000:5000 pneumonia-detection:latest
```

## Step 5: Push to AWS ECR (Elastic Container Registry)

```bash
# Login
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

# Tag image
docker tag pneumonia-detection:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/pneumonia-detection:latest

# Push
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/pneumonia-detection:latest
```

## Step 6: Deploy with ECS

1. Go to AWS ECS Dashboard
2. Create cluster
3. Create task definition pointing to your ECR image
4. Create service
5. Configure load balancer
6. Access via provided URL

---

# Quick Comparison: Which Should You Choose?

## Choose **Replit** if:
- ✅ You want to deploy in 10 minutes
- ✅ You're learning/prototyping
- ✅ You don't mind free tier limitations
- ✅ You want zero server management

## Choose **Render** if:
- ✅ You want a balance of ease and features
- ✅ You need GitHub integration
- ✅ You want professional hosting
- ✅ You can afford $7/month

## Choose **AWS EC2** if:
- ✅ You want full control
- ✅ You're learning DevOps
- ✅ You want free tier (1 year)
- ✅ You need scalability

## Choose **Docker + ECS** if:
- ✅ You need production-grade deployment
- ✅ You have DevOps experience
- ✅ You want to scale to millions of users
- ✅ You're building for enterprise

---

# Post-Deployment Checklist

After deploying, verify:

- [ ] Application loads without errors
- [ ] Image upload works
- [ ] Predictions return correct results
- [ ] File uploads are cleaned up
- [ ] Model weights load properly
- [ ] HTTPS is enabled (if applicable)
- [ ] Logging shows no errors
- [ ] Memory usage is reasonable
- [ ] Response time is acceptable (<5 seconds)

---

# Monitoring & Logging

## Monitor Performance

```bash
# Render
- Dashboard shows error logs automatically

# Heroku
heroku logs --tail

# AWS EC2
sudo journalctl -u pneumonia-detection -f
```

## Common Deployment Issues

### Issue: Model takes too long to load
**Solution:** Pre-warm model on startup
```python
# Load model once at startup
model_03 = build_model()
# Then reuse for all predictions
```

### Issue: Memory errors with large model
**Solution:** Reduce batch size or use model quantization
```python
# Option 1: Use smaller model
model.save('model_quantized.tflite')

# Option 2: Use memory-efficient loading
```

### Issue: Images not uploading
**Solution:** Check `/uploads` folder permissions
```bash
mkdir -p Flask\ Application/uploads
chmod 777 Flask\ Application/uploads
```

### Issue: Slow predictions
**Solution:** Use async processing
```python
from celery import Celery
# Implement async task queue
```

---

# Security Best Practices

1. **Environment Variables**
   ```python
   import os
   SECRET_KEY = os.environ.get('SECRET_KEY')
   DEBUG = os.environ.get('DEBUG', False)
   ```

2. **File Upload Validation**
   ```python
   ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
   MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
   ```

3. **HTTPS/SSL**
   - Always use HTTPS in production
   - Use Let's Encrypt (free)

4. **Rate Limiting**
   ```python
   from flask_limiter import Limiter
   limiter = Limiter(app, key_func=lambda: request.remote_addr)
   @app.route('/predict', methods=['POST'])
   @limiter.limit("10/minute")
   def upload():
       ...
   ```

5. **Hide Sensitive Data**
   - Don't log model paths
   - Don't expose error details to users
   - Use `.env` files for secrets

---

# Performance Optimization

## 1. Model Optimization
```python
# Reduce model size
import tensorflow_lite as tflite
converter = tflite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

# Or use quantization
converter.optimizations = [tflite.Optimize.DEFAULT]
```

## 2. Caching
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_prediction(img_hash):
    # Cache prevents re-predicting same image
    return model.predict(...)
```

## 3. Async Processing
```python
from flask_executor import Executor
executor = Executor(app)

@app.route('/predict-async', methods=['POST'])
def predict_async():
    future = executor.submit_stored('prediction_id', getResult, img_path)
    return {'prediction_id': 'prediction_id'}
```

## 4. Load Balancing
- Use multiple workers: `gunicorn -w 4`
- Use CDN for static files
- Enable gzip compression

---

# Scaling Your Application

## Horizontal Scaling (Multiple Servers)
```
Load Balancer
   ├── Server 1 (App)
   ├── Server 2 (App)
   └── Server 3 (App)
   
Shared Storage
   └── Model weights (shared volume)
```

## Vertical Scaling (Bigger Server)
- Upgrade instance type (t2.small → t2.medium)
- Add more RAM
- Faster CPU

## Database (Optional Future)
```python
# Store prediction results
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
```

---

# Summary: Deployment Decision Tree

```
Are you new to deployment?
  ├─ YES → Use Replit (easiest)
  └─ NO → Continue below

Can you wait 5 seconds for model to load?
  ├─ NO → Use Render or Heroku
  └─ YES → Continue below

Do you want to learn DevOps?
  ├─ YES → Use AWS EC2
  └─ NO → Use Render

Are you building for enterprise?
  ├─ YES → Use Docker + ECS
  └─ NO → Use Render
```

---

## Next Steps

1. **Choose a platform** from options 1-5
2. **Follow the step-by-step guide** for that platform
3. **Test your deployment** thoroughly
4. **Share your URL** with others
5. **Monitor logs** for errors
6. **Optimize** based on usage patterns

---

**End of Deployment Guide**
