import tkinter as tk
from pytube import YouTube
root=tk.Tk()
listobj=""
root.geometry("1200x400")
root.title("Vlad's fancy youtube downloader")



name_var=tk.StringVar()
passw_var=tk.StringVar()
console=tk.StringVar()


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
    stream = list.first()
    stream.download()
    print("aall done",yt.title)


    #t_streams.order_by('resolution')
    #t.streams.desc()
    #result.first()
    #print(result)
    #result.download() 
def downloadlist():
    global listobj
    chuncks = listobj.split(',')
    for chunck in chuncks:
        print(chunck)
        downloader(chunck)
    listobj=""
def showlistobj():
    global listobj
    print(listobj)
    console.set(listobj)
    
def submit():
    global listobj
    name=name_var.get()
    passw=passw_var.get()
    
    print("First Field : " + name)
    print("Second Field : " + passw)
    
    if name != "":                  ### if 1st field is full, donwload it, if not add 2nd fields value to list
        downloader(name)
    listobj = listobj + passw + ','
    
    
    
    name_var.set("")
    passw_var.set("")



#######fields and buttons
console_label=tk.Label(root, text = "console")
console_entry=tk.Entry(root,textvariable = console)

    
name_label = tk.Label(root, text = 'paste your youtub url here to be downloaded')
name_entry = tk.Entry(root, textvariable = name_var)

passw_label = tk.Label(root, text = 'place a url here and submit to add to the waitlist', font = ('calibre',10,'bold'))
passw_entry = tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit)
showlist_btn=tk.Button(root,text="show list object", command = showlistobj)

downloadlist_btn=tk.Button(root,text="download all the stuff you've submitted in the bottom box!", command= downloadlist)




###putting stuff into  places
console_label.grid(columnspan=20, rowspan=10, ipadx=500, ipady=100)
console_entry.grid(columnspan=70, rowspan=50, ipadx=500, ipady=100)
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
showlist_btn.grid(row=3,column=0)
downloadlist_btn.grid(row=6,column=6)



root.mainloop()
