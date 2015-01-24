import re
import os

def create():
	array_strings = []
	array_strings.append("((j == 0 || j == 9) && i != 0) || ((i == 0 || i == 4) && j >= 1 && j <= 8)")
	array_strings.append("j == 0 || (j == 9 && i != 0 && i != 4 && i != 9) || ((i == 0 || i == 4 || i == 9) && j <= 8 && j >= 0)")
	array_strings.append("(j == 0 && i != 0 && i != 9) || ((i == 0 || i == 9) && j > 0 && j < 9) || ((i == 1 || i == 8) && j == 9)")
	array_strings.append("j == 1 || ((i == 0 || i == 9) && j >= 0 && j < 9) || (j == 9 && i > 0 && i < 9)")
	array_strings.append("((i == 0 || i == 9) && j >= 0 && j <= 9) || j == 0 || (i == 4 && j >= 0 && j < 7)")
	array_strings.append("(i == 0 && j >= 0 && j <= 9) || j == 0 || (i == 4 && j >= 0 && j < 7)")
	array_strings.append("(j == 0 && i > 0 && i < 9) || (i == 0 && j > 0 && j < 9) || (i == 9 && j > 0 && j <= 9) || (j == 9 && i > 5) || (i == 5 && j > 3 && j < 9) || (i == 1 && j == 9)")
	array_strings.append("(i == 4 && j >= 0 && j <= 9) || j == 0 || j == 9")
	array_strings.append("((i == 0 || i == 9) && j >= 0 && j < 9) || j == 4")
	array_strings.append("(i == 0 && j >= 0 && j <= 9) || (j == 5 && i < 9) || (i == 9 && j > 0 && j < 5) || (j == 0 && i > 6 && i < 9)")
	array_strings.append("j == 0 || (i - j == 3 && j >= 0 && j < 9) || (i + j == 7 && j > 1)")
	array_strings.append("(i == 9 && j >= 0 && j <= 9) || j == 0")
	array_strings.append("j == 0 || (i - j == 0 && j > 0 && j < 5) || j == 9 || (i + j == 9 && j > 4 && j < 9)")
	array_strings.append("j == 0 || (i - j == 0 && j >= 0 && j <= 9) || j == 9")
	array_strings.append("((i == 0 || i == 9) && j > 0 && j < 9) || ((j == 0 || j == 9) && i > 0 && i < 9)")
	array_strings.append("j == 0 || ((i == 0 || i == 4) && j >= 0 && j < 9) || (j == 9 && i > 0 && i < 4)")
	array_strings.append("(i == 0 && j > 0 && j < 9) || (j == 0 && i > 0 && i < 9) || (i == 9 && j > 0 && j < 8) || (j == 9 && i > 0 && i < 8) || (i == j && j > 5)")
	array_strings.append("j == 0 || ((i == 0 || i == 4) && j >= 0 && j < 9) || (j == 9 && i > 0 && i < 4) || (i - j == 2 && j > 1 && j <= 9) || (i == 9 && (j == 8 || j == 9))")
	array_strings.append("((i == 0 || i == 4 || i == 9) && j > 0 && j < 9) || (j == 0 && i > 0 && i < 4) || (j == 9 && i > 4 && i < 9)")
	array_strings.append("(i == 0 && j >= 0 && j < 9) || j == 4")
	array_strings.append("((j == 0 || j == 9) && i != 9) || (i == 9 && j > 0 && j < 9)")
	array_strings.append("(i == j + 5 && j >= 0 && j < 5) || ((j == 0 || j == 8) && i < 5) || (i + j == 13 && j > 4 && j < 9)")
	array_strings.append("j == 0 || j == 9 || (i + j == 9 && j >= 0 && j < 5) || (i - j == 0 && j > 4 && j <= 9)")
	array_strings.append("(i == j || i + j == 9) && j >= 0 && j <= 9")
	array_strings.append("((i == j || i + j == 9) && j >= 0 && j <= 9 && i < 5) || ((j == 4 || j == 5) && i >= 5)")
	array_strings.append("((i == 0 || i == 9 || i + j == 9) && j >= 0 && j <= 9)")
	return array_strings

def process(name):
	array = create()
	condition = ""
	i = 0
	NAME = name[:len(name) - 1:]
	for ele in NAME :
		condition = condition + "(" + re.sub('[j]',"(j - " + str(i) + ")", array[ord(ele) - ord('A')]) + ") || "
		i += 11
	condition = condition + "(" + re.sub('[j]',"(j - " + str(i) + ")", array[ord(name[len(name) - 1::]) - ord('A')]) + ")"
	return condition

def make_file(condition, char):
	out = "# include <iostream>\nusing namespace std;\nint main()\n{\n   int i,j;\n   for (i = 0 ; i < 10 ; ++i)\n   {\n      "
	out = out + "for (j = 0 ; j < 140 ; ++j)\n      {\n         if (" + condition + ") cout<<\"" + char + "\"; \n         else cout<<' ';\n"
	out = out + "      }\n      cout<<endl;\n   }\n   return 0;\n}"
	return out


if __name__ == "__main__" :
	length = 13
	while length > 12 : 
		name = str(raw_input("Enter the name you want to display using ASCII art : "))
		length = len(name)
		if length > 12 :
			print ("Please enter a name less than 12 characters.")
		if not name.isalpha():
			print ("Please enter alphabets only.")
		     	length = 13
	char = raw_input("Enter the character you want to display the art in : ")
	while not (len(char) == 1 and char != ' '):
	     char = raw_input("Enter a single character and not a group of characters (and neither space) : ")
	cond = process(name.upper())          ## form the string in `if` condition
	out = make_file(cond, char)   ## design .cpp file
	FILE = open(name + ".cpp", 'w')
	FILE.write(out)
	FILE.close()
	os.system("make " + name)
	print ("\n\n\n")
	str(os.system("./" + name))
	print ("\n\n\n")
	
	## Deletion of .cpp file
	choice = raw_input("Do you want to delete " + name + ".cpp ? (Y/N) : ")
	while not (choice == 'Y' or choice == 'N'):
	     choice = raw_input("Enter your choice as 'Y' for yes or 'N' for no : ")
	if choice == 'Y':
	     os.system("sudo rm " + name + ".cpp")
	
	## Deletion of executable file
	choice = raw_input("Do you want to delete the executable ? (Y/N) : ")
	while not (choice == 'Y' or choice == 'N'):
	     choice = raw_input("Enter your choice as 'Y' for yes or 'N' for no : ")
	if choice == 'Y':
	     os.system("sudo rm " + name)
