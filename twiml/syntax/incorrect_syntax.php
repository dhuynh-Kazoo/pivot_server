<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<!-- test with user id -->
<!-- kazoo parse it as <<"\"8851dbe5bdcdd0eb06c29419cc50d9c6\"">> -->
<!-- so it could not find the endpoint associated with this id -->
<Response>
    <Say loop="1"> Going to test dial action! Thank you. This test has double quote for the text content</Say>

    <Dial>
        <User>"8851dbe5bdcdd0eb06c29419cc50d9c6"</User>
    </Dial>
</Response>

