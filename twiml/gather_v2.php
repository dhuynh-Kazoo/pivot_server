<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>

<Response>
    <Gather action="process_gather.php" method="GET">
        <Say>
            Hello there. Please enter, 1 2 3, followed by the pound sign
        </Say>
    </Gather>
    <Say>We didn't receive any input. Bye!</Say>
</Response>