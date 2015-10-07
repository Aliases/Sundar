import media 
import fresh_tomatoes

toy_story= media.Movie("toy story", "A story description", "http://www.dan-dare.org/FreeFun/Images/CartoonsMoviesTV/ToyStory2Wallpaper2800.jpg", "https://www.youtube.com/watch?v=nkqVm5aiC28&index=8&list=PLe2Pj2JNJo9l3nnGnjUDvCWWB7vJoHJH1")

#print(toy_story.storyline)

avatar= media.Movie("Avatar", "2nd story description", "http://www.dan-dare.org/FreeFun/Images/CartoonsMoviesTV/ToyStory2Wallpaper2800.jpg", "https://www.youtube.com/watch?v=nkqVm5aiC28&index=8&list=PLe2Pj2JNJo9l3nnGnjUDvCWWB7vJoHJH1")

#print(storyline)

#avatar.show_trailer()

movies=[toy_story, avatar]

#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)