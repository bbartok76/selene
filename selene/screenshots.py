import os
import selene.config
import logging

all_screenshots = []


def last_screenshot():
    if all_screenshots:
        return all_screenshots[-1]
    else:
        return ''


def take_screenshot(webdriver, path=None, filename=None):
    if not path:
        path = selene.config.reports_folder
    if not filename:
        filename = "screen_{id}".format(id=next(selene.config.counter))

    screenshot_path = os.path.join(path,
                                   "{}.png".format(filename))

    folder = os.path.dirname(screenshot_path)
    if not os.path.exists(folder):
        os.makedirs(folder)

    if webdriver.get_screenshot_as_file(screenshot_path):
        all_screenshots.append(screenshot_path)
        return screenshot_path
    else:
        return ''
