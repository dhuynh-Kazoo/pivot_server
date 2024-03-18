<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say> Going to test dial action! Thank you. Testing outbound DID number</Say>
    <Dial callerId="DatHuynhPivotTest" record="true">
        +14157365123
    </Dial>
</Response>
