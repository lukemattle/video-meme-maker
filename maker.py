import cv2
import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog

# Initialize default values
video_path = ""
output_path = ""
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.5
font_color = (255, 255, 255)
thickness = 2

# Define the overlay_text function
def overlay_text(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    text_size, _ = cv2.getTextSize(text_entry.get(), font, font_scale, thickness)
    text_x = (frame.shape[1] - text_size[0]) // 2
    text_y = (frame.shape[0] + text_size[1]) // 2
    frame = cv2.putText(frame, text_entry.get(), (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

# Define function to open input video file
def open_video():
    global video_path
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])

# Define function to open output video file
def save_video():
    global output_path
    output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Video Files", "*.mp4")])

# Define function to process video with text overlay
def process_video():
    if video_path != "" and output_path != "":
        video = mp.VideoFileClip(video_path)
        video = video.fl_image(overlay_text)
        video.write_videofile(output_path, codec="libx264")

# Create the GUI
root = tk.Tk()
root.title("Text Overlay")

# Create input video file button
input_button = tk.Button(root, text="Select Input Video", command=open_video)
input_button.pack()

# Create output video file button
output_button = tk.Button(root, text="Save Output Video", command=save_video)
output_button.pack()

# Create text entry field
text_label = tk.Label(root, text="Text:")
text_label.pack()
text_entry = tk.Entry(root)
text_entry.pack()

# Create process button
process_button = tk.Button(root, text="Process Video", command=process_video)
process_button.pack()

root.mainloop()
