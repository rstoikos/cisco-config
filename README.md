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
