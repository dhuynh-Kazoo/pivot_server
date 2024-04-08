<?php

header('content-type:application/json');

?>

{
    "module": "tts",
    "data": {
        "text": "Below are a series of poorly constructed paragraphs and possible solutions.",
        "voice": "male",
        "language": "en-us",
        "terminators": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"],
        "endless_playback": true
    },
    "children": {
        "_": {
            "module": "response",
            "data": {}
        }
    }
}
