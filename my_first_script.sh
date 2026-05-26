#!/bin/bash
# ================================
# My First Shell Script
# Cloud Engineer: Saad
# ================================

echo "================================"
echo "   CLOUD ENGINEER SETUP SCRIPT"
echo "================================"

# Variables
NAME="Saad"
GOAL="Top 5% Cloud Engineer"

echo "Engineer : $NAME"
echo "Goal     : $GOAL"

# Create folder structure
echo ""
echo "Creating project folders..."

mkdir -p CloudProject/networking
mkdir -p CloudProject/linux
mkdir -p CloudProject/python
mkdir -p CloudProject/aws

echo "✅ Networking folder created!"
echo "✅ Linux folder created!"
echo "✅ Python folder created!"
echo "✅ AWS folder created!"

# Check disk space
echo ""
echo "Checking disk space..."
df -h /

echo ""
echo "================================"
echo "✅ Setup Complete!"
echo "Welcome $NAME to Cloud Journey!"
echo "================================"