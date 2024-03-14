<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say>Hello, we will record your conversation</Say>
    <Record
        timeout="5"
        recordingUrl="http://192.168.1.16:5000/pivot/record/upload"
        finishOnKey="1"
        action="http://192.168.1.16:5000/pivot/twiml/record_thanks.php"
        method="GET"
        playBeep="true"
	    maxLength="60"
        trim="trim-silence"
        transcribe="true"
    />
</Response>
