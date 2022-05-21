#!/usr/bin/python3

from ast import Try, arg
from time import sleep
import requests
import argparse

wordlist = ""
url = ""
error_string = ""
cookie = ""
username_variable = ""
password_variable = ""
OK_USERS = []
Connection_OK = False
output= ""

def analysis():
    f = open(wordlist,"r")
    for username in f:
        send_request(username.strip())
        sleep(0.001)
    f.close()

def send_request(username):
    payload = {username_variable:username, password_variable:"aaaaaaaaa"}
    r = requests.post(url,data=payload, cookies=cookie)
    result = r.text
    if(error_string in result):
        OK_USERS.append(username)

def display():

    BANNER = "    █████  █████                            ███████████  ███                 █████ \n"                
    BANNER+= "   ░░███  ░░███                            ░░███░░░░░░█ ░░░                 ░░███ \n"                   
    BANNER+= "    ░███   ░███   █████   ██████  ████████  ░███   █ ░  ████  ████████    ███████   ██████  ████████ \n" 
    BANNER+= "    ░███   ░███  ███░░   ███░░███░░███░░███ ░███████   ░░███ ░░███░░███  ███░░███  ███░░███░░███░░███ \n" 
    BANNER+= "    ░███   ░███ ░░█████ ░███████  ░███ ░░░  ░███░░░█    ░███  ░███ ░███ ░███ ░███ ░███████  ░███ ░░░ \n" 
    BANNER+= "    ░███   ░███  ░░░░███░███░░░   ░███      ░███  ░     ░███  ░███ ░███ ░███ ░███ ░███░░░   ░███ \n" 
    BANNER+= "    ░░████████   ██████ ░░██████  █████     █████       █████ ████ █████░░████████░░██████  █████ \n"    
    BANNER+= "      ░░░░░░░░   ░░░░░░   ░░░░░░  ░░░░░     ░░░░░       ░░░░░ ░░░░ ░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░ \n" 
    print("\n"+ BANNER) 
    print("             A situational tool for non-existing problems")
    print("             made by RemiEC \n \n \n")                                                
                                                                                                  
                                                                                                  

def main():
    display()
    parser = argparse.ArgumentParser(description='Find usernames based on differences in error messages')
    parser.add_argument("url", help="Enter the target url")
    parser.add_argument("wordlist",  help="Wordlist of potential usernames")
    parser.add_argument("error_string", help="Text displayed when username OK but password KO")
    parser.add_argument("username_variable",  help="Name of username variable in POST request")
    parser.add_argument("password_variable", help="Name of password variable in POST request")
    parser.add_argument("--cookie", metavar="", help="Cookie to be added, e.g. {\"cookie\":\"value\"}")
    parser.add_argument("--output", metavar="filename", help="Output results to file")
    args = parser.parse_args()
    global wordlist 
    wordlist = args.wordlist
    global url 
    url = args.url
    global error_string 
    error_string = args.error_string
    global cookie 
    cookie = args.cookie
    global username_variable 
    username_variable = args.username_variable
    global password_variable 
    password_variable = args.password_variable
    global output
    output = args.output

    try:
        print("Beginning search ... \n")
        analysis()
        if (len(OK_USERS) == 0):
            print("No username found :(")
        else:
            print ("Valid usernames found ! \n")
            if(output != None):
                f=open(output, "w")
                for element in OK_USERS:
                    print(element)
                    f.write(element)
                f.close()
            else:
                for element in OK_USERS:
                    print(element)
            
    except Exception:
        print("\n Error :| ")

main()
