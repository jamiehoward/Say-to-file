import os

# Configuration options
command_list = '/' 
save_path = '/'
file_extension = '.aiff'
voice = 'Lee' # Lee (Australian), Daniel (UK), Alex (US)

# Get the command list
commands = []
with open(command_list) as file_obj:
	for line in file_obj.readlines():
		commands.append(line)


# Cycle through commands to create audio files
print 'Processing...'
print '----------------'
successes = []
for command in commands:
	command = command.rstrip('\n')
	command_text = command
	command_file = command + file_extension

	# Fix punctuation and spaces
	if (' ' in command) == True:
		command_file = command_file.replace(" ", "_")
	if ("'" in command == True):
		command_file = command_file.replace("'", "")
		command_text = command_text.replace("'", "\'")
	if (',' in command == True):
		command_file = command_file.replace(',', "")
	
	# Create file only if it does not exist
	try:
		with open(save_path + command_file):
			#print 'File exists'
			pass
	except:
		terminal_command = 'say -v' + voice + ' -o"' + save_path + command_file + '" "' + command_text + '"'
		try:
			os.system(terminal_command)
			print terminal_command
			successes.append(command_file)
		except IOError:
			print 'File ' + command_file + ' could not be created!';

# End the dialog
print '----------------'
print str(len(successes)) + ' file(s) created'