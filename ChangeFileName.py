import os

path = "/Users/hazemkhalil/Hard Drive/music"
os.chdir(path)

for file in os.listdir():
	if file == ".DS_Store":
		continue

	file_name, file_ext = os.path.splitext(file)

	file_number = int(file_name.split('-')[0])
	file_number = f"{file_number:02}"

	file_text = file_name.split('-')[1:]
	file_text = '-'.join(file_text)

	new_name = f"{file_number}-{file_text}{file_ext}"

	os.renames(file, new_name)

