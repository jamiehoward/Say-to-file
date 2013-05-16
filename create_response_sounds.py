import os

# Configuration options
command_list = '/audio_list'
save_path = '/audio/mp3/'
tmp_path = '/audio/tmp/'
file_extension = '.mp3'
tmp_extension = '.aiff'
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
	tmp_file = command

	# Fix punctuation and spaces
	if (' ' in command) == True:
		tmp_file = tmp_file.replace(" ", "_")
	if ("'" in command) == True:
		tmp_file = tmp_file.replace("'", "")
		command_text = command_text.replace("'", "\'")
	if (',' in command) == True:
		tmp_file = tmp_file.replace(',', "")
	if ('?' in command) == True:
		tmp_file = tmp_file.replace('?', "")
	if ('.' in command) == True:
		tmp_file = tmp_file.replace('.', "")

	command_file = tmp_file + file_extension
	tmp_file = tmp_file + tmp_extension
	
	# Create file only if it does not exist
	try:
		with open(save_path + command_file):
			#print 'File exists'
			pass
	except:
		tmp_command = 'say -v' + voice + ' -o"' + tmp_path + tmp_file + '" "' + command_text + '"'
		lame_command = 'lame --quiet ' + tmp_path + tmp_file + ' ' + save_path + command_file
		try:
			os.system(tmp_command)
			os.system(lame_command)
			os.system('rm -f ' + tmp_path + tmp_file)
			# print tmp_command
			print lame_command
			# print "\n"
			successes.append(command_file)
		except IOError:
			print 'File ' + command_file + ' could not be created!';

# End the dialog
print '----------------'
print str(len(successes)) + ' file(s) created'