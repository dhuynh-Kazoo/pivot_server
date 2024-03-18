<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say>Hello, we will record your conversation</Say>
    <Record
        timeout="5"
        recordingUrl="http://192.168.1.16:5000/pivot/twiml/record/upload"
        action="http://192.168.1.16:5000/pivot/twiml/record"
        method="POST"
        finishOnKey="1"
        playBeep="true"
	    maxLength="60"
        trim="trim-silence"
        transcribe="true"
    />
    <!-- all actions after Record wont be executed -->
    <Play>https://api.twilio.com/cowbell.mp3</Play>
</Response>