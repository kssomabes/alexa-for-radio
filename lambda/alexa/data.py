# -*- coding: utf-8 -*-
import gettext

_ = gettext.gettext

WELCOME_MSG = _("Welcome to {}. You can listen to your 22 favorite stations with this skill.")
NOW_PLAYING = _("Now playing: {}")
HELP_MSG = _("Welcome to {}. You can listen to your 22 favorite stations with this skill.")
UNHANDLED_MSG = _("Sorry, I could not understand what you've just said. You must be saying a radio station or a feature that is not supported.")
CANNOT_SKIP_MSG = _("This is radio, you have to wait for previous or next track to play.")
RESUME_MSG = _("Resuming {}")
NOT_POSSIBLE_MSG = _("This is radio, you can not do that.  You can ask me to stop or pause to stop listening.")
STOP_MSG = _("Goodbye.")
DEVICE_NOT_SUPPORTED = _("Sorry, this skill is not supported on this device")

TEST = _("test english")
TEST_PARAMS = _("test with parameters {} and {}")

jingle = {
    "db_table": "my_radio",
    "play_once_every": 1000*60*60*24  # 24 hours
}

home = {
    "card": {
        "title": 'Daily Listen',
        "text": 'This is the demo skill for Mark Pateman',
        "large_image_url": 'https://alexademo.ninja/skills/logo-512.png',
        "small_image_url": 'https://alexademo.ninja/skills/logo-108.png'
    },
}

# TODO: To add more radio stations, follow the format
stations = {
    "dreamboats and petticoats": {
        "url": "https://ssl.shoutcaststreaming.us:8036/",
        "card": {
            "title": "Dreamboats and Petticoats",
            "text": "Dreamboats and Petticoats station",
            "large_image_url": "https://alexademo.ninja/skills/logo-512.png",
            "small_image_url": "https://alexademo.ninja/skills/logo-108.png"
        }},
}


 