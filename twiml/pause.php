<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say>I will pause 10 seconds starting now!</Say>
    <Pause length="10"/>
    <Say>I just paused 10 seconds</Say>
</Response>