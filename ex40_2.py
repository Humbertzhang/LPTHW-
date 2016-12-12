class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
song_lyrics =["Soft Kitty~","Warm Kitty~","Little ball of a fur~",
					 "Happy Kitty~","Sleepy Kitty~","Po~Po~Po~"]

song = Song(song_lyrics)

song.sing_me_a_song()