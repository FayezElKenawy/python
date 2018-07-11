import fresh_tomatoes
import movieclass

the_lord_of_the_rings = movieclass.MovieClass("the lord of the rings",
                "https://en.wikipedia.org/wiki/The_Lord_of_the_Rings_(film_series)#/media/File:Ringstrilogyposter.jpg",
                "https://www.youtube.com/watch?v=V75dMMIW2B4")
the_hobbit = movieclass.MovieClass("the hobbit",
                "https://en.wikipedia.org/wiki/The_Hobbit_(film_series)#/media/File:The_Hobbit_trilogy_dvd_cover.jpg",
                "https://www.youtube.com/watch?v=JTSoD4BBCJc")
Pirates_of_the_Caribbean = movieclass.MovieClass("Pirates of the Caribbean",
                r"piratescover.jpg",
                "https://www.youtube.com/watch?v=KtsNKGrUMtk")
The_Fate_of_the_Furious = movieclass.MovieClass("The Fate of the Furious",
                "https://en.wikipedia.org/wiki/The_Fate_of_the_Furious#/media/File:The_Fate_of_The_Furious_Theatrical_Poster.jpg",
                "https://www.youtube.com/watch?v=uisBaTkQAEs")
Movies = [the_lord_of_the_rings,the_hobbit,Pirates_of_the_Caribbean,The_Fate_of_the_Furious]
print("__name__  " + movieclass.MovieClass.__name__)#the name of the class
print("__module__  " + movieclass.MovieClass.__module__)#the name of the module that contain the class