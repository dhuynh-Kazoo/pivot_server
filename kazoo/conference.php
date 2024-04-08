<?php

header('content-type:application/json');

?>

{
    "module": "tts",
    "data": {
        "text": "Hi this is a conference test using kazoo pivot format"
    },
    "children":
    {
        "_": {
            "module": "conference",
            "data": {
                "config": {
                        "name": "Dat Test",
                        "member": {
                            "join_muted": true,
                            "join_deaf": false,
                            "pins": ["1234"]
                        },
                        "play_entry_tone": true,
                        "play_exit_tone": true,
                        "max_participants": 3,
                        "require_moderator": true,
                        "wait_for_moderator": true
                    }
                
                }

        }

    }
    
}