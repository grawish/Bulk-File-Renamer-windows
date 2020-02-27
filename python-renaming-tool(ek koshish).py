import os
i=0
os.system("cls")
os.system("@echo off")
print("""
                       (                   (                                         
   (         (     )   )\ )      (         )\ )                                      
 ( )\    (   )\ ( /(  (()/(  (   )\   (   (()/(   (            )     )      (   (    
 )((_)  ))\ ((_))\())  /(_)) )\ ((_) ))\   /(_)) ))\  (     ( /(    (      ))\  )(   
((_)_  /((_) _ ((_)\  (_))_|((_) _  /((_) (_))  /((_) )\ )  )(_))   )\  ' /((_)(()\  
 | _ )(_))( | || |(_) | |_   (_)| |(_))   | _ \(_))  _(_/( ((_)_  _((_)) (_))   ((_) 
 | _ \| || || || / /  | __|  | || |/ -_)  |   // -_)| ' \))/ _` || '  \()/ -_) | '_| 
 |___/ \_,_||_||_\_\  |_|    |_||_|\___|  |_|_\\___||_||_| \__,_||_|_|_| \___| |_|   
                                                                                     
""")
print("Select the type of renaming:  \n\n\n")
print("\t0. XYZ<original-name>\n\t1. <original-name>XYZ\n\t2. <new-name>XYZ\n\t3. XYZ<new-name>\n\t4. XYZ\n\n Where XYZ is number increasing.\n\n5. list current directory\n\n")
print(os.path.dirname(__file__))
choice = input("Enter the type you select:  ")
if choice is "0":
	for x in os.listdir(os.path.dirname(__file__)):
		if x == os.path.basename(__file__) or x == "readme.txt":
			print("File mil gyi")
		else:
			i=i+1
			os.system("move \"" + x + "\" \"" + str(i) + os.path.splitext(x)[0] + os.path.splitext(x)[1] + "\"")
elif choice is "1":
	for x in os.listdir(os.path.dirname(__file__)):
		if x == os.path.basename(__file__) or x == "readme.txt":
			print("File mil gyi")
		else:
			i=i+1
			os.system("move \"" + x + "\" \"" + os.path.splitext(x)[0] + str(i) + os.path.splitext(x)[1] + "\"")
elif choice is "2":
	prefilename = input("Enter the pre-number filename")
	for x in os.listdir(os.path.dirname(__file__)):
		if x == os.path.basename(__file__) or x == "readme.txt":
			print("File mil gyi")
		else:
			i=i+1
			os.system("move \"" + x + "\" \"" + prefilename + str(i) + os.path.splitext(x)[1] + "\"")
elif choice is "3":
	postfilename = input("Enter the pre-number filename")
	for x in os.listdir(os.path.dirname(__file__)):
		if x == os.path.basename(__file__) or x == "readme.txt":
			print("File mil gyi")
		else:
			i=i+1
			os.system("move \"" + x + "\" \"" + str(i) + postfilename + os.path.splitext(x)[1] + "\"")
elif choice is "4":
	for x in os.listdir(os.path.dirname(__file__)):
		if x == os.path.basename(__file__) or x == "readme.txt":
			print("File mil gyi")
		else:
			i=i+1
			os.system("move \"" + x + "\" \"" + str(i) + os.path.splitext(x)[1] + "\"")
elif choice is "5":
	os.system("dir")
	input("\n\nPress any key to continue\n")
else:
	print("Please enter a valid choice")