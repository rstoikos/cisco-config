import threading
import paramiko
import subprocess
import getpass
import sys
import time
import os
import getopt
import socket
from sys import argv


# Promt symbol
prompt = '\t# '

def clear_screen():
    os.system('clear')

def pause():
	print "\n"
	programPause = raw_input('\tPress the <ENTER> key to continue...')
	print "\n"

def main_menu():
	clear_screen()
	print '\n\n'
	print '\t* * * * * * * * * * * * * * * * * * * * * * * * * * * *'
	print '\t*    ______  __       _______.  ______   ______         *' 
	print '\t*   /      ||  |     /       | /      | /  __  \        *'
	print '\t*  |  ,-----|  |    |   (----`|  ,-----|  |  |  |       *'
	print '\t*  |  |     |  |     \   \    |  |     |  |  |  |       *'
	print '\t*  |  `----.|  | .----)   |   |  `----.|  `--`  |       *'
	print '\t*   \______||__| |_______/     \______| \______/        *'
	print '\t*    ______   ______   .__   __.  _______               *'
	print '\t*   /      | /  __  \  |  \ |  | |   ____|              *'
	print '\t*  |  ,----`|  |  |  | |   \|  | |  |__                 *'
	print '\t*  |  |     |  |  |  | |  . `  | |   __|                *'
	print '\t*  |  `----.|  `--`  | |  |\   | |  |                   *'
	print '\t*   \______| \______/  |__| \__| |__|                   *'
	print '\t*                                           by Rstoikos *'
	print '\t* * * * * * * * * * * * * * * * * * * * * * * * * * * *'
	print '\n\n\t Choose number wisely:\n\n'
	print '\t\t1. Load IP addresses from file'
	print '\t\t2. Load commands to be executed from file\n'
	print '\t\t3. Show IP addresses loaded from file '
	print '\t\t4. Show commands that was loaded from file\n'
	print '\t\t5. Submit your credentials\n'
	#print '\t\t6. Submit just one IP to connect'
	#print '\t\t7. Submit just one command to execute in remote device\n'
	print '\t\t6. Start executing commands in every IP address in your file'
	print '\n\n\t\tq. Quit'
	choice = raw_input('\n\n >> ')
	if choice == "1":
		get_ip_addresses_file()
	elif choice == "2":
		get_cmds_file()	
	elif choice == "3":
		show_ip_addresses_file()
	elif choice == "4":
		show_cmds_from_file()
	elif choice == "5":
		get_user_credentials()
	#elif choice == "6":
	#	get_one_ip()
	#elif choice == "7":
	#	get_one_cmd()
	elif choice == "6":
		start_cmds_to_ip_from_file()
	elif choice == "q":
		quit()
	else:
		print "invalid selection"


def get_ip_addresses_file():
	global ips
	try:
		print "\tEnter IP addresses file name "
		ips = raw_input(prompt)
		f = open(ips,'r')
	except IOError:
		print "\tThere is no such file"
		pause()
	else:
		print "\tFile successfully loaded"
		f.close()
		pause()

def get_cmds_file():
	global cmds
	try:
		print "\tEnter commands file name "
		cmds = raw_input(prompt)
		f = open(cmds,'r')
	except IOError:
		print "\tThere is no such file"
		pause()
	else:
		print "\tFile successfully loaded"
		f.close()
		pause()
		

def show_ip_addresses_file():
	try:
		myfile = open(ips, 'r')
		print "\tIP addresses: \n"
		for ip in myfile:
			ip = ip.strip('\n')
			print "\t" , ip
		pause()
	except:
		print "\tNo file with IP addresses has been loaded\n"
		pause()
		get_ip_addresses_file()
		
	
def show_cmds_from_file():
	try:
		myfile = open(cmds, 'r')
		print "\tCommands to be executed: \n"
		for cmd in myfile:
			cmd = cmd.strip('\n')
			print "\t" , cmd
		pause()
	except:
		print "\tNo file with commands to be executed has been loaded\n"
		pause()
		get_cmds_file()
		
	
def get_user_credentials():
	global username
	global password
	global enable_password
	print "\tEnter Username: "
	username = raw_input(prompt)
	print "\tEnter Password: "
	password = getpass.getpass('\tPassword:')
	print "\tEnter Enable Password: "
	enable_password = getpass.getpass('\tEnable Password:')
	

def check_user_credentials():
	try:
		if username or password or enable_password != "":
			print "\tCredentials are loaded\n"
	except:
		print "\tNo credentials loaded yet\n"
		get_user_credentials()


def start_cmds_to_ip_from_file():
	check_user_credentials()
	print "\tWe are about to connect to these \n"
	show_ip_addresses_file()
	print "\tAnd we will submit \n"
	show_cmds_from_file()
	choice = ""
	while choice != "y" or "n":
		print "\tYou are going to start connecting in your routers and execute commnads, are you sure? (y) or (n) ?"
		choice = raw_input('\t\n\n >> ')
		if choice == "n":
			main_menu()
		elif choice == "y":	
			myfile = open(ips, 'r')
			for ip in myfile:
				ip = ip.strip('\n')
				ssh_command(ip)
		else:
			print "\t please choose 'y' or 'n' "
			pause()
		break
	
		
def file_cmds():
	mycmds = open(cmds, 'r')
	for cmd in mycmds:
		cmd = cmd.strip('\n')
		shell.send(cmd)
		print "Executing: ", cmd
		shell.send('\n')
		time.sleep(1)
		output = shell.recv(50000)
		print output
	

def ssh_command(ip):
	clear_screen()
	global shell
	try:
		print "\tConnecting to: ", ip
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(ip, username=username, password=password, allow_agent=False, look_for_keys=False)
		shell = ssh_client.invoke_shell(height=1240)
		shell.send('en\n')
		time.sleep(1)
		shell.send(enable_password)
		time.sleep(1)
		shell.send('\n')
		time.sleep(1)
		shell.send('terminal length 0\n')
		time.sleep(1)
		file_cmds()
	except paramiko.SSHException:
		print '\tAuthenctication Failure'
	except socket.error:
		print '\tUnable to connect to: ', ip
	ssh_client.close()
	pause()
	

while True:
	main_menu()
