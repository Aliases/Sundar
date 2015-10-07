import os
def rename_files():
	# get file names from folder
	file_list =os.listdir(r"/Users/A/Documents/Sundar/Python/prank")
	#print(file_list)
	saved_path = os.getcwd()
	print("Current working directory is "+saved_path)
	os.chdir(r"/Users/A/Documents/Sundar/Python/prank")

	#rename the file names
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None,"0123456789") )
	os.chdir(saved_path)


#rename_files()