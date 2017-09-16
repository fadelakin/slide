# Slide

Slide is a script/program?? I wrote that checks to see the song that is currently playing in Spotify (I removed the iTunes implementation because I don't use iTunes).

Once I know the song that is playing, the script searches the iTunes store for the album art relating to that song using the artist name and the song name to narrow it down. 

I then save the album art to be able to get the dominant color and the color palette of the album art. ColorThief returns the color palette as an array of tuples but that doesn't fit my needs so I convert the RGB tuples into hex code format. 

After that, we generate a patterned gif. I actually don't how this part works. I used this project to generate the pattern: https://github.com/eleanorlutz/AnimatedPythonPatterns 

## Pattern examples

XO TOUR Llif3 by Lil Uzi Vert
![screen](XO TOUR Llif3.gif "XO TOUR Llif3")

Signs by Drake
![screen](Signs.gif "Signs")

Crazy by Thief
![screen](Crazy.gif "Crazy")