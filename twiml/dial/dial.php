<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say> Going to test dial action! Thank you</Say>
    <Dial continueOnFail="false">1000</Dial>
</Response>
