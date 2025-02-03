#!/bin/bash

# UFW Firewall Setup Script
# Blocks all incoming traffic except for SSH (22), HTTP (80), and HTTPS (443)

echo "Updating package lists..."
sudo apt update -y

echo "Installing UFW..."
sudo apt install ufw -y

echo "Allowing SSH (port 22) to prevent lockout..."
sudo ufw allow 22/tcp

echo "Allowing HTTP (port 80)..."
sudo ufw allow 80/tcp

echo "Allowing HTTPS (port 443)..."
sudo ufw allow 443/tcp

echo "Enabling UFW..."
sudo ufw --force enable

echo "Checking UFW status..."
sudo ufw status

echo "Firewall setup completed successfully!"
