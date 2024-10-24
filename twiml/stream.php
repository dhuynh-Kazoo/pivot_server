<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Start>
        <Stream name="Example Audio Stream" url="ws://192.168.1.16:8080" />
    </Start>
    <Say>The stream has started.</Say>
</Response>