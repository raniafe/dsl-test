# (a) add a title on a black background at the beginning for 10 seconds stating where they were and when.
# (b) add a first video clip that appears directly after the title screen
# (c) add another video clip that appears directly after the first clip
# (d) add a thanks sentence at the end, lasting for 15 seconds
# (e) export the result as a video file

from moviepy.editor import *
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "C:\Program Files\ImageMagick-7.0.10-Q16-HDRI\magick.exe"})

screensize = (720,460)

composite_durations = []

# Make the text. Many more options are available.
intro = ( TextClip("Nos supers vacances au snowboard",fontsize=20,color='white',bg_color='black')
             .set_position(['center', 'center'])
             .set_duration(10)
             )
composite_durations.append(intro.duration)

video1 = VideoFileClip("./snow.mp4").subclip(20,25).set_position(['center', 'center'])
composite_durations.append(composite_durations[0] + video1.duration)

video2 = VideoFileClip("./snow.mp4").subclip(50,55).set_position(['center', 'center'])
composite_durations.append(composite_durations[1] + video2.duration)

outro = ( TextClip("Merci à tous",fontsize=20,color='white')
             .set_position(['center', 'center'])
             .set_duration(15))
composite_durations.append(composite_durations[2] + outro.duration)

print(composite_durations)
print(video1.duration)


result = CompositeVideoClip([intro, video1.set_start(composite_durations[0]), video2.set_start(composite_durations[1]), outro.set_start(composite_durations[2])], size=screensize) # Overlay text on video
# result = CompositeVideoClip([video1, video2.set_start(10)], size=screensize) # Overlay text on video
result.write_videofile("myHolidays_edited.webm",fps=25) # Many options...