import webbrowser
class MovieClass():
    def __init__(self, movie_title,poster_image_url,trailer_youtube_url):
        self.title = movie_title,
        self.poster_image_url = poster_image_url,
        self.trailer_youtube_url = trailer_youtube_url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        webbrowser.open(self.poster_image_url)
    
        
