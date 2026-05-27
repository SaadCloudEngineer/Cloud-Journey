#!/bin/bash
# ================================
# Cloud Engineer Setup Script
# Engineer: Saad Khan Pathan
# ================================

echo "==============================="
echo "  CLOUD ENGINEER DAILY SETUP"
echo "==============================="

# Variables
ENGINEER="Saad"
DATE=$(date)
PROJECT="CloudEngineerSaad"

echo "Engineer : $ENGINEER"
echo "Date     : $DATE"
echo "Project  : $PROJECT"
echo ""

# Step 1 — Check System
echo "STEP 1: SYSTEM CHECK"
echo "---------------------"
echo "Memory status:"
free -h | grep Mem
echo ""
echo "Disk status:"
df -h / | grep -v Filesystem
echo ""

# Step 2 — Create Structure
echo "STEP 2: PROJECT STRUCTURE"
echo "---------------------"
mkdir -p $PROJECT/day3
echo "✅ Day 3 folder created!"

# Step 3 — Create Log
echo ""
echo "STEP 3: CREATING LOG"
echo "---------------------"
LOG_FILE="$PROJECT/day3/setup.log"
echo "Setup started: $DATE" > $LOG_FILE
echo "Engineer: $ENGINEER" >> $LOG_FILE
echo "Status: Complete" >> $LOG_FILE
echo "✅ Log file created!"
echo ""

# Step 4 — Run Python Script
echo "STEP 4: RUNNING PYTHON"
echo "---------------------"
python3 ~/aws_simulation.py
echo ""

# Done
echo "==============================="
echo "✅ Daily Setup Complete!"
echo "💪 Keep going $ENGINEER!"
echo "🎯 Top 5% Cloud Engineer!"
echo "==============================="