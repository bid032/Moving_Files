



logo = """

 _______ _     ____ _______                  _             _             
|__   __| |   |___ \__   __|                (_)           | |            
   | |  | |__   __) | | | ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  _ __ 
   | |  | '_ \ |__ <  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
   | |  | | | |___) | | |  __/ |  | | | | | | | | | | (_| | || (_) | |   
   |_|  |_| |_|____/  |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_| 
					
		    TH3 TERMINATOR SCRIPT TOOL :")
		   Coded by Bido. => Abdallah Ahmed
		   https://www.facebook.com/bido.32
"""


print(logo)



import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))

print("\nWlcome in Moving Files Script - Enjoy dear\n")



for filename in os.listdir(current_dir):


	# Moving Images.
	if filename.endswith((".png" , ".jpg" , ".jpeg" , ".gif" , ".ico" , ".aif" , ".psp" , ".wmf" , ".bmp")):
		if not os.path.exists("Images"):
			os.mkdir('Images')
		shutil.move(filename , "Images")
		print('Done Moving Images\n')


	# Moving Apps.
	if filename.endswith(".exe"):
		if not os.path.exists("Apps"):
			os.mkdir('Apps')
		shutil.move(filename , "Apps")
		print('Done Moving Apps Files\n')


	# Moving Ios.
	if filename.endswith(".ios"):
		if not os.path.exists("Ios"):
			os.mkdir('Ios')
		shutil.move(filename , "Ios")
		print('Done Moving Ios Files\n')


	# Moving Audio.
	if filename.endswith((".mp3" , ".act" , ".aac" , ".amr" , ".aiff" , ".ogg")):
		if not os.path.exists("Audio"):
			os.mkdir('Audio')
		shutil.move(filename , "Audio")
		print('Done Moving Audio Files\n')


	# Moving Docs.
	if filename.endswith((".pdf" , ".doc" , "docx" , ".word" , ".ppt" , ".xls")):
		if not os.path.exists("Docs"):
			os.mkdir('Docs')
		shutil.move(filename , "Docs")
		print('Done Moving Docs Files\n')


	# Moving Arrchive.
	if filename.endswith((".zip" , ".tar" , ".rar" , ".gz")):
		if not os.path.exists("Arrchive"):
			os.mkdir('Arrchive')
		shutil.move(filename , "Arrchive")
		print('Done Moving Arrchive Files\n')


	# Moving Code.
	if filename.endswith((".py" , ".php" , ".html" , ".cmd" , ".txt" , ".js" , ".shtml")):
		if not os.path.exists("Codes"):
			os.mkdir('Codes')
		shutil.move(filename , "Codes")
		print('Done Moving Codes Files\n')


	# Moving Videos.
	if filename.endswith((".mp4" , ".flv" , ".rar" , ".avi" , ".rmvb" , ".mkv" , ".dvd")):
		if not os.path.exists("Videos"):
			os.mkdir('Videos')
		shutil.move(filename , "Videos")
		print('Done Moving Videos Files\n')

print("\nMoving Your Files is Successful")