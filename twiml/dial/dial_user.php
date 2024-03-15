<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say loop="2"> Going to test dial action! Thank you. With 10 seconds timeout and 60 seconds time Limit</Say>

    <Dial
        action="dial_thanks.php"
        method="GET"
        timeout="10"
        timeLimit="60"
    >
        <User>8851dbe5bdcdd0eb06c29419cc50d9c6</User>
    </Dial>
</Response>
