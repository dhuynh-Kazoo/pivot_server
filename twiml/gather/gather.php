<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Gather 
        timeout="20"
        finishOnKey="*"
        method="POST"
        numDigits="3"
        action="http://192.168.1.16:5000/pivot/gather"
    >
        <Play>https://api.twilio.com/cowbell.mp3</Play>


    </Gather>
    
</Response>