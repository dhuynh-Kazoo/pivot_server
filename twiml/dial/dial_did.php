<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Dial
        recordingUrl="http://192.168.1.16:5000/pivot/twiml/record/upload"
        record="true">
        +14157365123
    </Dial>
    <Say> You complete your Dial to offnet number. Thank you, we will reach to you soon </Say>
    <Play>https://api.twilio.com/cowbell.mp3</Play>

</Response>
