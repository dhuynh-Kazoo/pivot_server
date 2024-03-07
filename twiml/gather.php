<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say>Please enter your input.</Say>
    <Gather timeout="5" finishOnKey="#">
    </Gather>
    <Say>Collect completed. Thank you</Say>
    
</Response>