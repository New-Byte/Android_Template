'''
Management file to manage operations on project/app.
Author:             Iron-Legion@GCOEJ
Date:               01 NOVEMBER 2021
'''

import sys
import os

arglist = sys.argv

try:
	# Help options
	if arglist[1] == "--help" or arglist[1] == "-h":
		print("\n--------------------Help Options--------------------\n")
		print("create OR -c:\tCreates project.")

	elif arglist[1] == "-c" or arglist[1] == "create":
		# Clone repository from github and remove .git dir.
		# os.system("git clone https://github.com/New-Byte/Android_Template.git")
		os.system("attrib -h .git")
		os.rename(".git","git")
		os.system("rmdir /Q /S git")

		# Write README.md
		f = open("./README.md","w")
		f.write("# " + arglist[2] + "\n" + "Project Description")
		f.close()

		# Rename root folder
		os.system("ren " +"template " + arglist[2])

		# Add gitignore file
		f = open(arglist[2]+"/android/.gitignore","w")
		f.write("*.iml\n.gradle\n/local.properties\n/.idea/caches\n/.idea/libraries\n/.idea/modules.xml\n/.idea/workspace.xml\n/.idea/navEditor.xml\n/.idea/assetWizardSettings.xml\n.DS_Store\n/build\n/captures\n.externalNativeBuild\n.cxx")
		f.close()

		# Rename folders to hidden folders
		os.rename(arglist[2]+"/android/gradle1", arglist[2]+"/android/.gradle")
		os.rename(arglist[2]+"/android/idea", arglist[2]+"/android/.idea")

		# Search for meraBharat in each file and replace it with app_name (arglist[2])

		# Read all files in android dir.
		path = arglist[2]+"/android"
		filelist = []
		for root, dirs, files in os.walk(path):
			for file in files:
				filelist.append(os.path.join(root,file))

		# Read each file
		for x in filelist:
			try:
				f = open(x,"r")
				f_data = f.readlines()
				f.close()
			except:
				continue
			flag = 0
			# Check if MeraBharat is present in file
			for y in range(len(f_data)):
				if "MeraBharat" in f_data[y]:
					flag = 1
					# Replace MeraBharat with app_name
					f_data[y] = f_data[y].replace("MeraBharat", arglist[2])
				elif "meraBharat".lower() in f_data[y]:
					flag = 1
					f_data[y] = f_data[y].replace("MeraBharat".lower(), arglist[2].lower())
				elif "meraBharat".upper() in f_data[y]:
					flag = 1
					f_data[y] = f_data[y].replace("MeraBharat".upper(), arglist[2].upper())
			# Update file
			if flag:
				f = open(x,"w")
				f.writelines(f_data)
				f.close()

except:
	print("============================================")
	print("\nmanage.py expects at least 1 argument,\n0 were given.\n\nE.g.: python manage.py --help\n")
	print("============================================")
