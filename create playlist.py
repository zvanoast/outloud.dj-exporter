import sys, re, mmap

with open(sys.argv[1], 'r', encoding='utf-8') as playlistFile, open(sys.argv[2], 'w', encoding="utf-8") as outputFile:
	playlist = playlistFile.read()
	songNames = re.findall(r'(?<="title">)(.*)(?=</p>)', playlist)
	artistNames = re.findall(r'(?<="artist">)(.*)(?=</p>)', playlist)

	if len(songNames) != len(artistNames):
		raise Exception('Song names and Artist names are different #s')

	for song, artist in zip(songNames, artistNames):
		outputFile.write(f"{song} - {artist}\n")