# from moviepy.editor import VideoFileClip
# from moviepy.editor import TextClip
# from moviepy.editor import CompositeVideoClip
from moviepy.editor import *
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "C:\Program Files\ImageMagick-7.0.10-Q16-HDRI\magick.exe"})

video = VideoFileClip("./snow.mp4").subclip(50,60).crossfadeout(2)

composite_videos = []

# Make the text. Many more options are available.
subtitle_clip = ( TextClip("Pour le mini shred, et faire des trics flat très facilement",fontsize=20,color='white')
             .set_position(['center', 'bottom'])
             .set_start(0)
             .set_duration(3))

subtitle_clip2 = ( TextClip("je vous conseille de prendre une petite board souple, type cimemac ",fontsize=20,color='white')
             .set_position(['center', 'bottom'])
             .set_start(3)
             .set_duration(4))

subtitle_clip3 = ( TextClip("grace à son camble en double grille, vous ferrez des tricks tres facilement",fontsize=20,color='white')
             .set_position(['center', 'bottom'])
             .set_start(7)
             .set_duration(3))

result = CompositeVideoClip([video, subtitle_clip, subtitle_clip2, subtitle_clip3]) # Overlay text on video
result.write_videofile("myHolidays_edited.webm",fps=25) # Many options...