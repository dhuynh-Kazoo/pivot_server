<?php

header('content-type:application/json');

?>
{
    "module":"tts",
    "data":{
        "text": "This is a test for kazoo collecting DTMF. Please enter up to five digits."
    },
    "children": {
        "_": {
            "module": "collect_dtmf",
            "data": {
                "max_digits": 5,
                "timeout": 10000,
                "terminators": ["*", "#"],
                "collection_name": "custom_name"
            }
        }
    }
}