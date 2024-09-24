import tkinter as tk
import tkinter.ttk as ttk
from pytube import YouTube
from moviepy.editor import *
from tkinter.filedialog import askdirectory

window = tk.Tk()
window.title("YT to mp3 converter")
save_path = "D:/Music/converter_music/"

def convert_command():
    if mp3_flag.get() == 1:
        if default_folder.get() == 1:
            url = url_entry.get()
            # Use pytube to download the video
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            
            # Download the video to a file
            out_file = video.download(output_path=save_path)
            
            # Set up new filename for the MP3
            new_file = out_file.replace(".mp4", ".mp3")
            # Use moviepy to convert video audio to mp3
            video_clip = AudioFileClip(out_file)
            video_clip.write_audiofile(new_file)
            
            # Remove the original video file
            os.remove(out_file)
            
            url_entry.delete(0, tk.END)

            # return new_file  # Return the path to the new file
        elif default_folder.get() == 0:
            new_save_path = askdirectory()
            url = url_entry.get()
            # Use pytube to download the video
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            
            # Download the video to a file
            out_file = video.download(output_path=new_save_path)
            
            # Set up new filename for the MP3
            new_file = out_file.replace(".mp4", ".mp3")
            # Use moviepy to convert video audio to mp3
            video_clip = AudioFileClip(out_file)
            video_clip.write_audiofile(new_file)
            
            # Remove the original video file
            os.remove(out_file)
            
            url_entry.delete(0, tk.END)

            # return new_file  # Return the path to the new file

    elif mp4_flag.get() == 1:
        if default_folder.get() == 1:
            url = url_entry.get()
            # Use pytube to download the video
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=False).first()
            
            # Download the video to a file
            out_file = video.download(output_path=save_path)
            
            # Set up new filename for the MP3
            #new_file = out_file.replace(".mp4", ".mp3")
            # Use moviepy to convert video audio to mp3
            video_clip = VideoFileClip(out_file)
            video_clip.write_videofile(out_file)
            
            # Remove the original video file
            #os.remove(out_file)
            
            url_entry.delete(0, tk.END)

        elif default_folder.get() == 0:
            new_save_path = askdirectory()
            url = url_entry.get()
            # Use pytube to download the video
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=False).first()
            
            # Download the video to a file
            out_file = video.download(output_path=new_save_path)
            
            # Set up new filename for the MP3
            #new_file = out_file.replace(".mp4", ".mp3")
            # Use moviepy to convert video audio to mp3
            #video_clip = AudioFileClip(out_file)
            #video_clip.write_audiofile(new_file)
            
            # Remove the original video file
            #os.remove(out_file)
            
            url_entry.delete(0, tk.END)

mp3_flag = tk.IntVar(window, value=1, name="mp3")
mp4_flag = tk.IntVar(window, value=0, name="mp4")

def mp3_command():
    window.setvar(name = "mp3", value=1)
    window.setvar(name = "mp4", value=0)
    mp3_btn["relief"] = tk.SUNKEN
    mp4_btn["relief"] = tk.RAISED
    mp4_btn["borderwidth"] = 2
    mp3_btn["borderwidth"] = 5
 

def mp4_command():
    window.setvar(name = "mp4", value=1)
    window.setvar(name = "mp3", value=0)
    mp4_btn["relief"] = tk.SUNKEN
    mp3_btn["relief"] = tk.RAISED
    mp4_btn["borderwidth"] = 5
    mp3_btn["borderwidth"] = 2

def default_folder_command():
    print(default_folder.get())

url_entry_convert_btn_frame = tk.Frame()
#convert_btn_frame = tk.Frame()
mp3_4_btn_frame = tk.Frame()
default_folder_frame = tk.Frame()

url_entry = tk.Entry(master=url_entry_convert_btn_frame,
                     width=50
                     )
url_entry.pack(side=tk.LEFT)



mp3_btn = tk.Button(master=mp3_4_btn_frame,
                    text=".mp3",
                    width=10,
                    height=1,
                    command=mp3_command,
                    borderwidth=5,
                    relief=tk.SUNKEN
                    )
mp3_btn.pack(side=tk.LEFT)

mp4_btn = tk.Button(master=mp3_4_btn_frame,
                    text=".mp4",
                    width=10,
                    height=1,
                    command=mp4_command
                    )
mp4_btn.pack(side=tk.LEFT)

convert_btn = tk.Button(master=url_entry_convert_btn_frame,
                        text="Convert",
                        width=10,
                        height=1,
                        command=convert_command
                        )
convert_btn.pack(side=tk.RIGHT)

default_folder = tk.IntVar(value=1)
default_folder_btn = ttk.Checkbutton(master=default_folder_frame,
                                     text="Default folder",
                                     variable=default_folder,
                                     onvalue=1,
                                     offvalue=0,
                                     command=default_folder_command
                                     )
default_folder_btn.pack(side=tk.RIGHT)

url_entry_convert_btn_frame.pack(side=tk.TOP)
#convert_btn_frame.pack(side=tk.RIGHT)
mp3_4_btn_frame.pack(side=tk.LEFT)
default_folder_frame.pack(side=tk.RIGHT)

# Start the event loop.
window.mainloop()