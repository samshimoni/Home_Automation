#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M")
fswebcam -r 1280x720 --no-banner /home/$USER/Desktop/Home_Automation/Camera/$DATE.jpg

