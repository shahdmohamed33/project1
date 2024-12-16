from tkinter import *
from pytube import YouTube

def download_video():
    url = url_entry.get()
    yt = YouTube(url)
    quality = quality_var.get()
    
    if quality == "high":
        video = yt.streams.get_highest_resolution()
    else:
        video = yt.streams.get_lowest_resolution()
        
    video.download()
    status_label.config(text="Download completed successfully!")

# Setting up the application window
window = Tk()
window.title("YouTube Video Downloader")
window.geometry("400x250")

# URL input field
Label(window, text="Enter your YouTube link here:").pack(pady=10)
url_entry = Entry(window, width=50)
url_entry.pack(pady=10)

# Quality options
quality_var = StringVar(value="high")
Label(window, text="Select quality:").pack(pady=10)
Radiobutton(window, text="High Quality", variable=quality_var, value="high").pack()
Radiobutton(window, text="Low Quality", variable=quality_var, value="low").pack()

# Download button
download_button = Button(window, text="Download Video", command=download_video)
download_button.pack(pady=20)

# Download status label
status_label = Label(window, text="")
status_label.pack()

# Start the application loop
window.mainloop()