from moviepy.editor import *
from moviepy.config import change_settings
from moviepy.video.tools.subtitles import SubtitlesClip
change_settings({"IMAGEMAGICK_BINARY": "C:\Program Files\ImageMagick-7.0.10-Q16-HDRI\magick.exe"})
screensize = (720, 460)
composite_durations = []
intro = (TextClip("Nos supers vacances au snowboard", fontsize=20, color='white', bg_color='black')
             .set_position(['center', 'center'])
             .set_duration(10))
composite_durations.append(intro.duration)
subs = [((10, 20), 'sub1'),
        ((50, 60), 'sub2'),
        ((116, 131), 'sub3'),
        ]
subtitles = SubtitlesClip(subs).set_position(['center', 'bottom'])
video1 = VideoFileClip("./snow.mp4").subclip((0, 23), (1, 47)).set_position(['center', 'center'])
composite_durations.append(composite_durations[0] + video1.duration)
video2 = VideoFileClip("./snow.mp4").subclip((2, 1), (2, 21)).set_position(['center', 'center'])
composite_durations.append(composite_durations[1] + video2.duration)
outro = (TextClip("Merci à tous", fontsize=20, color='white')
             .set_position(['center', 'center'])
             .set_duration(15))
composite_durations.append(composite_durations[2] + outro.duration)
result = CompositeVideoClip([intro, video1.set_start(composite_durations[0]),
                             video2.set_start(composite_durations[1]),
                             outro.set_start(composite_durations[2]), subtitles],
                            size=screensize)
result.write_videofile("myHolidays_edited.webm", fps=25)