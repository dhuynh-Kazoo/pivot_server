<?php

header('content-type:application/json');

?>

{
    "module": "tts",
    "data": {
        "text": "Thank you for reaching out. We will reocord your call. Please leave your message after the beep",
        "voice": "male",
        "language": "en-us",
        "terminators": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"],
        "endless_playback": true
    },
    "children": {
        "_": {
            "module": "record_caller",
            "data": {
                "action": "start",
                "time_limit": 10,
                "format": "mp3",
                "url": "http://192.168.1.16:5000/pivot/kazoo/record/upload"

            }
        }
    }
}