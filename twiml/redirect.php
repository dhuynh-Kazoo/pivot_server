<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Say>Hello This is a redirect action</Say>
        <Redirect method="GET">http://192.168.1.16:5000/pivot/twiml/redirect_branch.php</Redirect>
    <Say>Checking if completed redirect action back to main flow</Say>    

</Response>