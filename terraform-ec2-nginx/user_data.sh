#!/bin/bash

# Update package repository
sudo yum update -y

# Install Nginx
sudo amazon-linux-extras enable nginx1
sudo yum install -y nginx

# Start and enable Nginx
sudo systemctl start nginx
sudo systemctl enable nginx

# Replace default index.html with custom HTML
cat <<EOF | sudo tee /usr/share/nginx/html/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Terraform EC2 + Nginx</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; text-align: center; padding: 50px; }
        h1 { color: #2E86C1; font-size: 48px; }
        p { font-size: 20px; color: #555; }
        .footer { margin-top: 30px; font-size: 14px; color: gray; }
    </style>
</head>
<body>
    <h1>Hello from Terraform + Nginx!</h1>
    <p>This page is deployed automatically using <b>Terraform</b> on AWS EC2.</p>
    <div class="footer">Powered by Nginx on Amazon Linux 2</div>
</body>
</html>
EOF


#this script installs Nginx automatically when the EC2 instance launches