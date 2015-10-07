import webbrowser 

class Movie():
	"""Documentation for class movie"""

	VALID_RATINGS=["G", "PG", "PG-13","R"]

	def __init__(self, movie_title, movie_sl, pos_img, tr_yt):
		self.title = movie_title
		self.storyline = movie_sl
		self.poster_image_url = pos_img
		self.trailer_youtube_url = tr_yt

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


