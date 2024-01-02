from Rectangle import Rectangle
from PIL import ImageGrab, Image
from Constants import PLAY_AREA, LEFT_LOG, RIGHT_LOG


# make screenshot
def make_screenshot(x1=None, y1=None, x2=None, y2=None):
    if x1 is None or y1 is None or x2 is None or y2 is None:
        screenshot = ImageGrab.grab()
        screenshot.save('play_area_screenshot.png')
    else:
        screenshot = ImageGrab.grab((x1, y1, x2, y2))
        screenshot.save('play_area_screenshot.png')

def is_left_log():
    photo = Image.open('play_area_screenshot.png')
    pixel_color = photo.getpixel((LEFT_LOG.get_x(), LEFT_LOG.get_y()))
    print(pixel_color)