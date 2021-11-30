#!/bin/env python
import tkinter as tk
from pytube import YouTube
from moviepy.video.io.VideoFileClip import AudioFileClip
import os
from os import listdir
root=tk.Tk()
listobj=[]
root.geometry("1200x400")
root.title("Vlad's fancy youtube to mp3 downloader")



single_field=tk.StringVar()
multi_field=tk.StringVar()



def downloader(arg1):

    #link = arg1 #input("Enter the line: ")
    #for paste in link:
    yt = YouTube(arg1)
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length,"seconds")
    print("Description: ",yt.description)
    print("Ratings: ",yt.rating)
    list = yt.streams.filter(only_audio=True)
    print(list) 
    filename = list.get_audio_only().download()
    clip = AudioFileClip(filename)
    clip.write_audiofile(filename[:-4] + " .mp3")
    clip.close()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-all done",yt.title)


    #t_streams.order_by('resolution')
    #t.streams.desc()
    #result.first()
    #print(result)
    #result.download() 
def downloadlist():
    global listobj
    #chuncks = listobj.split(',')
    for chunck in listobj:
        print(chunck)
        downloader(chunck)
    listobj.clear()
    
def showlistobj():
    global listobj
    print(listobj)

def submit():
    global listobj
    single=single_field.get()
    multi=multi_field.get()
    
    print("First Field : " + single)
    print("Second Field : " + multi)
    
    if single != "":                  ### if 1st field is full, donwload it, if not add 2nd fields value to list
        downloader(single)
    elif multi != "": 
        listobj.append(multi)    
    
    
    single_field.set("")
    multi_field.set("")
    

def cleanup():

    folder_path=os.getcwd() + '/'
    print(folder_path)
    for file_name in listdir(folder_path):
            if(file_name.endswith('.mp4')):
                os.remove(folder_path + file_name)



#######fields and buttons


single_label = tk.Label(root, text = 'paste your youtub url here to be downloaded (single)', font = ('calibre',16,'bold'))
single_entry = tk.Entry(root, textvariable = single_field)

multi_label = tk.Label(root, text = 'sumbit multipe urls here one at a time \nthen download them all with the bottom right button', font = ('calibre',16,'bold'))
multi_entry = tk.Entry(root, textvariable = multi_field,)
sub_btn=tk.Button(root,text = 'Submit', command = submit)
showlist_btn=tk.Button(root,text="show a list of urls that you have submitted so far", command = showlistobj, font = ('calibre',16,'bold'))

downloadlist_btn=tk.Button(root,text="download all the stuff you've submitted in the second box!", command= downloadlist, font = ('calibre',16,'bold'))

cleanup_btn=tk.Button(root,text = 'clean up (deletes all leftover mp4 files in current directory, be careful)', command = cleanup(), font = ('calibre',16,'bold'))



###putting stuff into  places

single_label.grid(row=0,column=0)
single_entry.grid(row=0,column=1)
multi_label.grid(row=1,column=0)
multi_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
showlist_btn.grid(row=3,column=0)
downloadlist_btn.grid(row=10,column=2)
cleanup_btn.grid(row=14,column=2)



root.mainloop()
