<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say>Hello This is a call will recording you</Say>
    <Record
        timeout="10"
        recordingUrl="http://localhost:5000/upload"
        finishOnKey="#"
        action="https://dhuynh147.000webhostapp.com/twiml/record_thanks.php"
        method="GET"
    />

</Response>