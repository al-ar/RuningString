from moviepy.editor import *
from transliterate import translit

SCREEN_SIZE = (100, 100)
FONT_SIZE = 50
VIDEO_DURATION = 3
FPS = 25
def create_video(text):


    txtClip = TextClip(text, color='black', font="TimesNewRoman",
                       fontsize=FONT_SIZE)
    txtClip = txtClip.set_pos(lambda t: (FONT_SIZE-len(text)*10*t,'center'))
    clip = ImageClip('../background/background_image.jpg').set_duration(VIDEO_DURATION)

    cvc = CompositeVideoClip([clip, txtClip.set_duration(clip.duration)],
                             size=SCREEN_SIZE)
    text = translit(text, language_code='ru', reversed=True)
    name = '../tempVideo/' + text+'.mp4'
    return cvc.write_videofile(name, fps=FPS)