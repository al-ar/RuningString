from moviepy.editor import *
from transliterate import translit


W = 100
H = 100
SCREEN_SIZE = (W, H)
FONT_SIZE = 30
VIDEO_DURATION = 3
FPS = 25
def create_video(text):
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    alpha = sum(1 for c in text if not c.isalnum())
    digit = sum(1 for c in text if c.isdigit())
    coef_len = (upper*1.5+lower*1.1+alpha*0.6 + digit*1.2)/len(text)
    speed = coef_len * len(text) /VIDEO_DURATION
    symbol = W - FONT_SIZE
    txtClip = TextClip(text, color='black', font="TimesNewRoman",
                       fontsize=FONT_SIZE).set_pos(
        lambda t: (symbol-(t*FONT_SIZE*0.5*speed), 'center')).set_duration(VIDEO_DURATION)
    clip = ImageClip('../background/background_image.jpg').set_duration(VIDEO_DURATION)

    cvc = CompositeVideoClip([clip, txtClip],
                             size=SCREEN_SIZE)
    text = translit(text, language_code='ru', reversed=True)
    name = '../tempVideo/' + text+'.mp4'
    return cvc.write_videofile(name, fps=FPS)