#!/bin/bash

NAME="Saad Khan"
AGE=22
GENDER="Male"
EMAIL="saadkhanpathan38@gmail.com"
CITY="Burjuman, Dubai"
GOAL="Top 5% Cloud Engineer"
DATE=$(date)

echo "================================"
echo "   CLOUD ENGINEER PROFILE"
echo "================================"
echo "Name   : $NAME"
echo "Age    : $AGE"
echo "Gender : $GENDER"
echo "Email  : $EMAIL"
echo "City   : $CITY"
echo "Goal   : $GOAL"
echo "Date   : $DATE"
echo "================================"

# Create FOLDERS using mkdir
mkdir -p CloudProfile/personal
mkdir -p CloudProfile/skills
mkdir -p CloudProfile/projects
echo "✅ Folders created!"

# Create FILE inside personal folder
touch CloudProfile/personal/profile.txt

# Write info into file
echo "Name   : $NAME" >> CloudProfile/personal/profile.txt
echo "Age    : $AGE" >> CloudProfile/personal/profile.txt
echo "Gender : $GENDER" >> CloudProfile/personal/profile.txt
echo "Email  : $EMAIL" >> CloudProfile/personal/profile.txt
echo "City   : $CITY" >> CloudProfile/personal/profile.txt
echo "Goal   : $GOAL" >> CloudProfile/personal/profile.txt
echo "Date   : $DATE" >> CloudProfile/personal/profile.txt
echo "✅ Profile written!"

# Read file with FULL PATH
cat CloudProfile/personal/profile.txt

echo "================================"
echo "   Profile Setup Complete!"
echo "================================"