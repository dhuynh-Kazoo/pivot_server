<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say>Please enter your input.</Say>
    <Gather 
        timeout="10"
        finishOnKey="#"
        method="POST"
        numDigits="5"
        action="http://192.168.1.16:5000/pivot/gather"
    >

    </Gather>
    <Say>Collect completed. Thank you</Say>
    
</Response>