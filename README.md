# EdibleAuto


WordPress Automation with Python and Ubuntu

**Overview**

This project focuses on automating a WordPress website. It involves scraping restaurant data and automating content posting using Python scripts and an Ubuntu server.

**Features**
**Data Scraping:** Extracts data from the Michelin website about two and three-starred restaurants using Beautiful Soup, saving the data in a CSV format.

**Automated Posting:** Utilizes Selenium and Chrome WebDriver to automate posting of restaurant information to the WordPress site.

**Scheduled Automation:** Implements a cron job on an Ubuntu server (AWS EC2 instance) for daily script execution.

#Getting Started

**Prerequisites:**
Python
Beautiful Soup
Selenium
Chrome WebDriver
Ubuntu Server (AWS EC2 recommended)

**Installation**
1. Clone the repository.
2. Install required Python libraries.
3. Set up an Ubuntu server on AWS EC2.

**Users will need to run Chromium headless browser prior to running the Autoedible.py script.** To do so you can run the following commands on the EC2 instance:

` to open x display

Xvfb -ac :99 -screen 0 1280x1024x16 & export DISPLAY=:99

to open chrome

chromium-browser

/usr/bin/python3
/home/ubuntu/tru2.py


Xvfb -ac :99 -screen 0 1280x1024x16 
/usr/bin/chromium-browser `

**Usage**
1. Run the data scraping script to generate a CSV file with restaurant information.
2. Execute the posting script, which will use the CSV data to create and publish posts on the WordPress site.
3.Set up a cron job on the Ubuntu server to automate the daily running of the script.

License
MIT
