# provide source folder where all pictures are (on phone)
# check the date from either the name of the file or date modified
	# name of the file should be sufficient, at least until they change it
# parse the year and month
# copy from source folder to target folder
# report error if file is not copied
# also create new folders if they do not exist yet (for future months)




def sort_pictures(source_folder, target_folder)
	for filename in source_folder:
		year = filename[0:3]
		month = filename[4:5]
		copy_to_folder(target_folder, filename, year, month)
		print(success_message)


def copy_to_folder(target_folder, filename, year, month)
	# do the windows operations
	# report error (raise exception?) if file not copied, or any windows operation fails
	# log the operations in a .log file
