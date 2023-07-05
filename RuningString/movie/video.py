from moviepy.editor import *

SCREEN_SIZE = (100, 100)
FONT_SIZE = 50
VIDEO_DURATION = 3
FPS = 25
def create_video(text):


    txtClip = TextClip(text, color='black', font="Amiri-Bold",
                       fontsize=FONT_SIZE)
    txtClip = txtClip.set_pos(lambda t: (FONT_SIZE-len(text)*10*t,'center'))
    clip = ImageClip('../background/background_image.jpg').set_duration(VIDEO_DURATION)

    cvc = CompositeVideoClip([clip, txtClip.set_duration(clip.duration)],
                             size=SCREEN_SIZE)

    name = '../tempVideo/' + text+'.mp4'
    return cvc.write_videofile(name, fps=FPS)