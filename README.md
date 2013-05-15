Say-to-file
===========

<h2>Summary:</h2>
For the BT Harrow project. Creates <code>say</code> audio files for all text lines in specified file

<h2>Purpose:</h2>
Utility to create text-to-speech audio files for every line in a specified file.

<h2>Requirements:</h2>
This utility was written on a Mac, and will work with the bash "say" command that comes on a Mac. However, this utility was written for the sole purpose of creating audio files from the <code>say</code> command to be used on a Linux box that does not support such a command. That being said, and as far as I know, this needs to run on a Mac (I'm running 10.7).

<h2>How to use:</h2>
<li>
	<ol>Look over the audio_file file and see if there is anything you would like to remove or add to the list</ol>
	<ol>Edit the <code>command_list</code> variable within create_response_sounds.py file (line 4) with the absolute path to audio_file</ol>
	<ol>Edit the <code>save_path</code> variable to point to the absolute path where you would like the files saved (line 5)</ol>
	<ol>Change the file extension or text-to-speech voice if you like (or if your system does not have the default "Lee").</ol>
	<ol>Finally, open a terminal, navigate to the directory where create_response_sounds.py is located, and run "python create_response_sounds.py"</ol>
</li>

<b>Note: </b> The script does some rough checking to see if file exists, so you shouldn't have a problem with duplicate audio segments.

<h2>Final note:</h2>
This is the first version of the file that I wrote in about an hour, so there are sure to be some things I can improve upon. Have fun.

<h4>Jamie Howard</h4>