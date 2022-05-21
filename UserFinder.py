#!/usr/bin/python3

from ast import Try, arg
from time import sleep
import requests
import argparse
import sys

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
    count = 0
    file = f.readlines()
    f.close()
    length = len(file)
    for username in file:
        send_request(username.strip())
        count +=1
        drawProgressBar(count/length)
        sleep(0.001)
    print("\nSearch completed ! \n")
    

def drawProgressBar(percent, barLen = 20):
    # percent float from 0 to 1. 
    sys.stdout.write("\r")
    sys.stdout.write("[{:<{}}] {:.0f}%".format("=" * int(barLen * percent), barLen, percent * 100))
    sys.stdout.flush()

def send_request(username):
    payload = {username_variable:username, password_variable:"aaaaaaaaa"}
    r = requests.post(url,data=payload, cookies=cookie)
    result = r.text
    if(error_string in result):
        OK_USERS.append(username)

def display():

    BANNER = " █████  █████                            ███████████  ███                 █████ \n"                
    BANNER+= "░░███  ░░███                            ░░███░░░░░░█ ░░░                 ░░███ \n"                   
    BANNER+= " ░███   ░███   █████   ██████  ████████  ░███   █ ░  ████  ████████    ███████   ██████  ████████ \n" 
    BANNER+= " ░███   ░███  ███░░   ███░░███░░███░░███ ░███████   ░░███ ░░███░░███  ███░░███  ███░░███░░███░░███ \n" 
    BANNER+= " ░███   ░███ ░░█████ ░███████  ░███ ░░░  ░███░░░█    ░███  ░███ ░███ ░███ ░███ ░███████  ░███ ░░░ \n" 
    BANNER+= " ░███   ░███  ░░░░███░███░░░   ░███      ░███  ░     ░███  ░███ ░███ ░███ ░███ ░███░░░   ░███ \n" 
    BANNER+= " ░░████████   ██████ ░░██████  █████     █████       █████ ████ █████░░████████░░██████  █████ \n"    
    BANNER+= "   ░░░░░░░░   ░░░░░░   ░░░░░░  ░░░░░     ░░░░░       ░░░░░ ░░░░ ░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░ \n" 
    print("\n"+ BANNER) 
    print("             A situational tool for non-existing problems")
    print("             made by RemiEC \n \n \n")                                                
                                                                                                  
                                                                                                  

def main():
    display()
    parser = argparse.ArgumentParser(description='Find usernames based on error messages\' differences')
    parser.add_argument("url", help="Enter the target url")
    parser.add_argument("wordlist",  help="Wordlist of potential usernames")
    parser.add_argument("error_string", help="Text displayed when username OK but password KO")
    parser.add_argument("username_variable",  help="Name of username variable in POST request")
    parser.add_argument("password_variable", help="Name of password variable in POST request")
    parser.add_argument("-c", "--cookie", help="Cookie to be added")
    parser.add_argument("-o", "--output", help="Output results to file")
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
        print("Beginning search ... ")
        analysis()
        if (len(OK_USERS) == 0):
            print("No username found :(")
        else:
            
            if(output != ""):
                print ("Valid usernames found ! I saved them in your output file \n")
                f=open(output, "w")
                for element in OK_USERS:
                    print(element)
                    f.write(element)
                f.close()
            else:
                print ("Valid usernames found !")
                for element in OK_USERS:
                    print(element)
            
    except Exception:
        if (len(OK_USERS) == 0):
            print("Error encountered, no username were found :(")
        else:
            print ("Error encountered, here are the results I managed to get (also saved in your output file) :  \n")
            if(output != ""):
                f=open(output, "w")
                for element in OK_USERS:
                    print(element)
                    f.write(element)
                f.close()
            else:
                print ("Error encountered, here are the results I managed to get :")
                for element in OK_USERS:
                    print(element)

    except KeyboardInterrupt:

        print("\n\nSeems like you got a bit impatient >:(")
        if (len(OK_USERS) == 0):
            print("I didn't have time to find anything juicy")
        else:
            print ("Here is what I managed to get anyway (also saved in your output file) :  \n")
            if(output != ""):
                f=open(output, "w")
                for element in OK_USERS:
                    print(element)
                    f.write(element)
                f.close()
            else:
                print ("Here is what I managed to get anyway")
                for element in OK_USERS:
                    print(element)
        

main()
