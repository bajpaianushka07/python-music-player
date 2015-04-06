# Python Music Player (PyMP) #
At the moment this is my private music player. The source-code is uploaded, but there are no instructions on how to get this running! :) Some info is on this page. Note that this page does not talk about the underlying ideas, plugins, and more.

## Introduction ##
PyMP is a music player daemon written in Python for Linux operating systems. PyMP is currently heavily in development. At this moment it has little functionality. It will not do what you want it to do, unless you want it to play and scrobble last.fm radio. This means that it **probably** is **not what you are looking for**!

## Requirements ##
Linux
  * dbus
  * gstreamer (arch linux users install gstreamer0.10-plugins)

Python 2
  * pygst (gstreamer)
  * mutagen
  * python simplejson
  * python dateutil

  * python urwid (optional, ncurses interface only)
  * python libnotify (optinonal, only for the libnotify plugin)

## Installation ##
There is no installation needed. You can create symbolic links in your bin folders if you like.

## Starting the Daemon ##
```
./pymp-daemon
```

## Your music collection(s) ##
TODO: This is programmatically not finished yet!




## Connecting to [Last.fm](http://www.last.fm) ##
There is little program which grants PyMP access to use your Last.fm account. Once this is done, PyMP is able to scrobble tracks to last.fm. It can also play Last.fm radio if you pay Last.fm for it. It queues your scrobbles when you are listening offline. You can find this little program here: `./lastfm/setup-lastfm.py`. It justs opens your browser with a Last.fm page where you have to accept.

![http://dl.dropbox.com/u/4362832/pymp-lastfm.png](http://dl.dropbox.com/u/4362832/pymp-lastfm.png)

_Scrobbling last.fm radio to last.fm from PyMP._


## Playing and Queue ##
It is possible to play a song directly by running the following command:
```
./pymp-cli.py play <file>
```

If you want to play a track, only after the running track and queue are empty, then you can queue the track by running the following command:
```
./pymp-cli.py queue <file>
```

## Creating a playlist ##
Instead of only playing and queuing tracks, PyMP also supports playlists. **Currently these playlists can not be stored on disk.** For completeness, here is an example to create and start a playlist.
```
# First create a new list, of type files.
./pymp-cli.py newlist filelist mylist

# Next add a file to the list
./pymp-cli.py lists mylist addtrack "./03. Sonne.mp3"

# Third, tell PyMP that we want to play tracks of the newly added list
./pymp-cli.py player setlist mylist

#Oh, and tell it to start playback of the current lists
./pymp-cli.py player play
```

## Command Line Control ##
PyMP can be controlled over the command line. Currently the following commands are supported:
```
./pymp-cli.py player start
./pymp-cli.py player stop
./pymp-cli.py player next
./pymp-cli.py player prev
```

When you are a last.fm subscriber you can tune to last.fm radio stations by:
`./pymp-cli.py tune RADIOSTATIONNAME `. Here RADIOSTATION has to be substituted by your radio station of desire, e.g. :
```
./pymp-cli.py tune lastfm://user/theunknowncylon/personal
```

## Curses Interface ##
_Note: you have to checkout the branch "cli" for this._

There is a curses interface available, which you can start by running `./pymp-curses.py`. Below you can find two screenshots. Note that the background is my desktop wallpaper (some terminal transparency here).

![http://dl.dropbox.com/u/4362832/pymp0.png](http://dl.dropbox.com/u/4362832/pymp0.png)

_Curses interface - Browsing your music collection._

![http://dl.dropbox.com/u/4362832/pymp1.png](http://dl.dropbox.com/u/4362832/pymp1.png)

_Curses interface - Your playlist._
