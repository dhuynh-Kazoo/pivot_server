<?php

header('content-type:application/json');

?>

{
    "module": "play",
    "data": {
        "id": "038779773b7d0c556c6790f06f7322a6",
        "terminators": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"],
        "loop_count": 3
    }
    "children" {
        "_": {
            "module": "set_variables",
            "custom_application_vars":
                {
                    "timeout": 10,
                    "actionUrl": "http://localhost:5000/ecallmgr_extention",
                    "billing": "$1000"  
                }
        }
    }
}