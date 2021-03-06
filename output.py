# Wiring code generated from an CinEditorML model
# Video name: mavideo
from moviepy.editor import *
from moviepy.config import change_settings
from moviepy.video.tools.subtitles import SubtitlesClip
change_settings({"IMAGEMAGICK_BINARY": "C:\Program Files\ImageMagick-7.0.10-Q16-HDRI\magick.exe"})
screensize = (720, 460)
composite_durations = [0]
miniature_durations = []

clip1a = VideoFileClip("./snow.mp4").subclip(23,43).set_position(['center','center']).fx(transfx.slide_in, 1, 'bottom')

clip1b = VideoFileClip("./snow.mp4").subclip(121,141).set_position(['center','center']).fx(transfx.crossfadein, 1)

comment_clip = VideoFileClip("./comment.mp4").subclip(0,60).set_position(['right','bottom']).fx(vfx.resize, width=50, height=50)

intro = TextClip("Cet element dure 10 secondes",
bg_color='black',
fontsize=20,
color='white',
).set_position(['center','center']).set_duration(10)
outro = TextClip("Cet element dure 15 secondes",
bg_color='black',
fontsize=20,
color='white',
).set_position(['center','center']).set_duration(15)

composite_durations.append(intro.duration + composite_durations[0])
composite_durations.append(clip1a.duration + composite_durations[1])
composite_durations.append(clip1b.duration + composite_durations[2])
composite_durations.append(outro.duration + composite_durations[3])
clip_list = {}
clip_list['intro'] = [composite_durations[0], composite_durations[1], 0]
clip_list['clip1a'] = [composite_durations[1], composite_durations[2], 1]
clip_list['clip1b'] = [composite_durations[2], composite_durations[3], 2]
clip_list['outro'] = [composite_durations[3], composite_durations[4], 3]
miniature_durations.append((clip_list['clip1a'][0]  - 0 , clip_list['clip1a'][0] - 0 +0
))

subs = []
subs.append(((clip_list['clip1a'][0]  - 0 , clip_list['clip1a'][0] - 0 +10
), 'Sous titre du debut de clip1a pour 10s', 'sub_clip1'))
subs.append(((list(filter(lambda sub: sub[2] == 'sub_clip1', subs))[0][0][1]  + 30 ,list(filter(lambda sub: sub[2] == 'sub_clip1', subs))[0][0][1]  + 30 +10
), 'Sous titre de la fin de subclip2+30 pour 10s', 'sub_clip2'))
subs.append(((clip_list['clip1b'][0]  - 5 , clip_list['clip1b'][0] - 5 +15
), 'Sous titre du debut de clip1b-5 pour 15s', 'sub_clip3'))
subs2 = [((ta,tb), txt) for ((ta,tb), txt, name) in subs]
subtitles = SubtitlesClip(subs2).set_position(['center', 'bottom'])

result = CompositeVideoClip([
intro.set_start(composite_durations[0]),
clip1a.set_start(composite_durations[1]),
clip1b.set_start(composite_durations[2]),
outro.set_start(composite_durations[3]),
comment_clip.set_start(miniature_durations[0][0]),

		
subtitles
], size=screensize)

result.write_videofile("mavideo.webm",fps=25)
