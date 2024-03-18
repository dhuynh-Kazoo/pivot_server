<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<!-- 
without recordingUrl
without action
recorded file will be sent to currentUrl(pivot get URL)
the format is: http://192.168.1.16:5000/pivot/twiml/record/record.php/call_recording_{call_id}.mp3 
-->

<Response>
    <Say>Hello, we will record your conversation</Say>
    <Record
        timeout="5"
        finishOnKey="1"
        method="GET"
        playBeep="true"
	    maxLength="60"
        trim="trim-silence"
        transcribe="true"
    />
</Response>