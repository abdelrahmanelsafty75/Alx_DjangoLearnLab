# Deployment Configuration for HTTPS (Nginx Example)

To enforce HTTPS at the web server level, we must configure Nginx to listen on port 443 and provide the SSL/TLS certificates.

## Nginx Server Block Setup

```nginx
server {
    listen 80;
    server_name yourdomain.com [www.yourdomain.com](https://www.yourdomain.com);
    
    # Redirect all HTTP traffic to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com [www.yourdomain.com](https://www.yourdomain.com);

    # SSL/TLS Certificates (Generated via Let's Encrypt / Certbot)
    ssl_certificate /etc/letsencrypt/live/[yourdomain.com/fullchain.pem](https://yourdomain.com/fullchain.pem);
    ssl_certificate_key /etc/letsencrypt/live/[yourdomain.com/privkey.pem](https://yourdomain.com/privkey.pem);

    location / {
        proxy_pass [http://127.0.0.1:8000](http://127.0.0.1:8000); # Proxy to Django Gunicorn
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https; # Important for Django to know it's HTTPS
    }
}

