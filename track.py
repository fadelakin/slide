# TODO: Link up to arduino or internet connected lightbulbs. you know the rest

from PIL import Image, ImageFilter
from io import BytesIO
from colorthief import ColorThief

import itunes # pip install pyitunes
import requests
import applescript # pip install py-applescript
import json

def get_currently_playing_song():
    tell_spotify = applescript.AppleScript('''
    on is_running(appName)
    	tell application "System Events" to (name of processes) contains appName
    end is_running
    on Playing()
    	set SpotifyRunning to is_running("Spotify")
    	if SpotifyRunning then
    		tell application "Spotify"
    			set songTitle to the name of the current track
    			set songArtist to the artist of the current track
    			set songAlbum to the album of the current track
                set player to "Spotify"
    			set result to songArtist & "%-%" & songTitle & "%-%" & songAlbum & "%-%" & player
    			if player state is playing then
    				return result
    			else
    				return "None" & "%-%" & "None" & "%-%" & "None"
    			end if
    		end tell
    	end if
    end Playing
    ''')

    try:
        output = tell_spotify.call('Playing').split('%-%')

        song = dict()
        song['artist'] = output[0]
        song['name'] = output[1]
        song['album'] = output[2]
        song['player'] = output[3]
        get_song_artwork(song)
    except AttributeError:
        print("Spotify is most likely not running. Start it and play some music then run the script again.")

def get_song_artwork(song):
    try:
        song_name = song['name']
        song_artist = song['artist']
        song_player = song['player']
        song_album = song['album']

        print("Name: {}".format(song_name))
        print("Album: {}".format(song_album))
        print("Artist: {}".format(song_artist))
        print("Player: {}".format(song_player))

        # search itunes store to get our album art
        results = itunes.search(query="{} {}".format(song_artist, song_name))
        try:
            desired_song = results[0] # the first result is most likely our desired result
            desired_artwork_url = desired_song.artwork['600']
            response = requests.get(desired_artwork_url)
            img = Image.open(BytesIO(response.content))
            img.save('art.png')
            get_color_palette_from_cover()
        except IndexError:
            print("Could not get album art for this song so no color values.")
    except AttributeError:
        print("Something went wrong. Fix it boi.")

def get_color_palette_from_cover():
    color_thief = ColorThief('art.png')
    # dominant color
    dominant_color = color_thief.get_color(1)
    # build a color palette
    palette = color_thief.get_palette(5)
    print("Dominant Color: {}".format(dominant_color))
    print("Color Palette: {}".format(palette))
    mess_with_lights(palette)

def mess_with_lights(palette):
    pass

if __name__ == '__main__':
    get_currently_playing_song()
