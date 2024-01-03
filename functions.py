from Rectangle import Rectangle
from PIL import ImageGrab, Image
from Constants import PLAY_AREA, LEFT_LOG, RIGHT_LOG


# make screenshot
def make_screenshot(x1=None, y1=None, x2=None, y2=None):
    if x1 is None or y1 is None or x2 is None or y2 is None:
        screenshot = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=False, xdisplay=None)
        screenshot.save('play_area_screenshot.png')
    else:
        screenshot = ImageGrab.grab((x1, y1, x2, y2))
        screenshot.save('play_area_screenshot.png')


def is_left_log(pos):
    x, y = pos
    photo = Image.open('play_area_screenshot.png')
    pixel_color = photo.getpixel((x, y))
    r, g, b = pixel_color
    if r == 167 and g == 92 and b == 42:
        return True
    else:
        return False


def is_right_log(pos):
    x, y = pos
    photo = Image.open('play_area_screenshot.png')
    pixel_color = photo.getpixel((x, y))
    r, g, b = pixel_color
    if r == 167 and g == 92 and b == 42:
        return True
    else:
        return False
