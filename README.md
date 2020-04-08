# cisco-config
Python app for mass cisco configuration

This simple Python script accepts input from 2 files.

In the first file the IP addresses of the devices that you want to connect separated by a newline  
e.g  
1.1.1.1  
2.2.2.2  
3.3.3.3  

In the second file the actual commands to be executed should also be separated by a newline  
e.g  
show ip int b | e un  
show ip route | i O  

The script asks for your credentials and then executes for every IP address in the file every cmd in the 2nd file

![image](https://github.com/rstoikos/cisco-config/blob/master/diagram.png)

assuming our files is named 'hosts' and has these 3 entries
```
192.168.56.103
192.168.56.104
192.168.56.105

```
and our file with the commands we want to execute is called 'cmds'
```
show ip int b | e un
```
Then when we run the script

```
	 Choose number wisely:


		1. Load IP addresses from file
		2. Load commands to be executed from file

		3. Show IP addresses loaded from file 
		4. Show commands that was loaded from file

		5. Submit your credentials

		6. Start executing commands in every IP address in your file


		q. Quit


 >> 1
	Enter IP addresses file name 
	# hosts
	File successfully loaded


	Press the <ENTER> key to continue...
  
   >> 2
	Enter commands file name 
	# cmds
	File successfully loaded


	Press the <ENTER> key to continue...
 >> 3
	IP addresses: 

	192.168.56.103
	192.168.56.104
	192.168.56.105


	Press the <ENTER> key to continue...

 >> 4
	Commands to be executed: 

	show ip int b | e un


	Press the <ENTER> key to continue...

```
```

 >> 5
	Enter Username: 
	# renos
	Enter Password: 
	Password:
	Enter Enable Password: 
	Enable Password:

 >> 6
	Credentials are loaded

	We are about to connect to these 

	IP addresses: 

	192.168.56.103
	192.168.56.104
	192.168.56.105


	Press the <ENTER> key to continue...


	And we will submit 

	Commands to be executed: 

	show ip int b | e un


	Press the <ENTER> key to continue...


	You are going to start connecting in your routers and execute commnads, are you sure? (y) or (n) ?
```
Then he output is:
```
	Connecting to:  192.168.56.103
Executing:  show ip int b | e un

r4>en
Password: 
r4#terminal length 0
r4#show ip int b | e un
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.56.103  YES DHCP   up                    up      
Ethernet0/2            10.0.0.2        YES NVRAM  up                    up      
Loopback0              192.168.50.4    YES NVRAM  up                    up      

r4#


	Press the <ENTER> key to continue...
  
	Connecting to:  192.168.56.104
Executing:  show ip int b | e un

r3>en
Password: 
r3#terminal length 0
r3#show ip int b | e un
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            10.0.2.5        YES NVRAM  up                    up      
Ethernet0/1            10.0.0.6        YES NVRAM  up                    up      
Ethernet0/2            192.168.56.104  YES DHCP   up                    up      
Loopback0              192.168.50.3    YES NVRAM  up                    up      

r3#


	Press the <ENTER> key to continue...

```
and the script continues untill finished

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/rstoikos/cisco-config)
