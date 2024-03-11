<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say>Please enter your input.</Say>
    <Gather 
        timeout="5" 
        finishOnKey="#" 
        method="GET" 
        numDigits="5"
        action="https://dhuynh147.000webhostapp.com/twiml/gather_thanks.php">
    </Gather>

</Response>