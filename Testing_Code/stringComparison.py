print("\tString Comparison")
string1 = ""
string2 = ""
continuar = 1
while(continuar):
	string1 = input("Enter string 1: ")
	string2 = input("Enter string 2: ")
	if(string1 == string2): print("Equal")
	else: print("No equal")
	continuar = int(input("Continue? (1/0): "))
print("Program Terminated")
