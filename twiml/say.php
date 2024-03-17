<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say loop='10' terminators='#' voice='female'>This is a say action, going to share something with you!!!!!</Say>
</Response>