# youtube-mp3-downloader
a simple youtube downloader application built in python with pytube moviepy and tkinter. now with download queuing and auto cleanup

Install instructions:
 download in desired directory
 run the following in terminal:
 python -m pip install tkinter
 python -m pip install pytube
 python -m pip install moviepy
 
 python youtube-mp3.py
 
 
 
 Use instructions:
    paste desired url in first field for a single download.
    If downloading more then one url use the second field.
    Pressing submit stores the url to a list to be downloaded, repeat submitting urls to the second field until all are submitted
    if it is desirable to see current list of submitted urls in console there is a button for that
    finally the bottom right button will download every url submitted in second field sequentially, and create a mp3 file of it
    there is a new experimental feature called "cleanup" it will remove every mp4 file downloaded and leave only the desirable mp3s,
    this can be undesirable as it will delete all mp4 files indiscriminately in the directory in which it is installed.
    
    dont downlaod anything you dont own etc..
