<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<!-- startConferenceOnEnter=true for moderator -->
<Response>
    <Dial>
        <Conference
            startConferenceOnEnter="true"
            beep="true"
            recordingUrl="http://192.168.1.16:5000/pivot/twiml/record/upload"
            record="true"
        >
            96e22ad7f354ef2d84884c82fb9a5796
        </Conference>
    </Dial>
</Response>
