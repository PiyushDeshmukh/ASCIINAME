### [ASCIINAME](http://piyushdeshmukh.github.io/ASCIINAME/)
ASCIINAME is a tool that displays text in ASCII art form. Originally, it was designed to write names in ASCII art form, but I am looking forward to support more Unicode characters in near future, for now, only strings with one word containing alphabets only are supported.

### PRE-REQUISITES
To run this python script, you need python and c++ installed on your LINUX machine. Google them if you don't have them installed.   
The script is written in python 2.7.6. It is recommended to place the script in a separate directory as it will generate some files during runtime.   

### USAGE
To run the script, type `python asciiname.py` in terminal.    

The script will generate a c++ file which when executed shall convert a text into ASCII art. The script will also compile the .cpp file for you and create an executable which will be run with the help of the OS module in python.

### MORE POINTS TO REMEMBER
The script creates 2 files namely, the name entered from stdin as a .cpp and a executable. The ASCII art generated is due to the .cpp file and not due to the asciiname.py file. Please remember that this  script does not delete the generated temporary files automatically, you need to respond according to your wish at the end.
This is kept deliberately, so that one does not need to run .py file solely from starting, he can get executable or .cpp file of desired string automatically. Please consider entering your password (if asked), deleting those files require to execute `rm` as sudo.

### How it works?
Read more at [ASCIINAME](http://piyushdeshmukh.github.io/ASCIINAME/)
