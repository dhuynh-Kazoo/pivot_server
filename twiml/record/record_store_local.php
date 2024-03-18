<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<!-- 
without recordingUrl
recorded file will be sent to action urldecode
the format is: http://192.168.1.16:5000/pivot/twiml/record/record_thanks.php/call_recording_{call_id}.mp3 
-->

<Response>
    <Say>Hello, we will record your conversation</Say>
    <Record
        timeout="5"
        finishOnKey="1"
        action="http://192.168.1.16:5000/pivot/twiml/record/record_thanks.php"
        recordingUrl=""
        method="GET"
        playBeep="true"
	    maxLength="60"
        trim="trim-silence"
        transcribe="true"
    />
</Response>