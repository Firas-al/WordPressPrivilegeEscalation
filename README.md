# Wordpress Privilege Escalation

## Introduction

Supose you have a wordpress website as a target, and you have a user and a password which are correct but you can't set up nothing in the site. For you, i have this python tool.

## Requisites

- Python 3.x

## How to Use

With python installed, run the `main.py` on the target host with the known and the target user:

    python main.py -h LOGIN_HOST -u KNOWN_USER -p KNOWN_PASSWORD -t TARGET_USER -f PASSWORDS_TXT_FILE
    
    Example:
      python main.py -h http://wordpress.site/wp-login.php -u think -p 123 -t admin -f passwords.txt
      
