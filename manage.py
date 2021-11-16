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
		print("Removing .git")
		os.system("rmdir ./.git")

		# Write README.md
		f = open("README.md","w")
		f.write("# " + arglist[2] + "\n" + "Project Description")
		f.close()

		# Rename root folder
		print("Renaming root dir")
		os.rename("template",arglist[2])

		# Add gitignore file
		f = open(arglist[2]+"/.gitignore","w")
		f.write("*.iml\n.gradle\n/local.properties\n/.idea/caches\n/.idea/libraries\n/.idea/modules.xml\n/.idea/workspace.xml\n/.idea/navEditor.xml\n/.idea/assetWizardSettings.xml\n.DS_Store\n/build\n/captures\n.externalNativeBuild\n.cxx")
		f.close()

		# Rename folders to hidden folders
		print("Renaming hidden dirs")
		os.rename(arglist[2]+"/gradle",arglist[2]+"/.gradle")
		os.rename(arglist[2]+"/idea",arglist[2]+"/.idea")

		# Search for meraBharat in each file and replace it with app_name (arglist[2])
except:
	print("============================================")
	print("\nmanage.py expects at least 1 argument,\n0 were given.\n\nE.g.: python manage.py --help\n")
	print("============================================")
