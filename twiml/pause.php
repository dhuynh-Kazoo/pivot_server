<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say>I will pause 10 seconds starting now!</Say>
    <Pause length="10"/>
    <Say>Resume the call, thank you for waiting</Say>
</Response>
