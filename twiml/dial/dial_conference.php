<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<!-- startConferenceOnEnter=true for moderator -->
<Response>
    <Say> Going to test dial action! Thank you. We are routing you to a conference</Say>
    <Dial>
        <Conference
            waitUrl="https://api.twilio.com/cowbell.mp3"           
            voice="male"
            startConferenceOnEnter="false"
            announceCount="false"
            muted="true"
            beep="true"
            deaf="true"
            play_name="true"
            play_entry_prompt="true"
        >
            96e22ad7f354ef2d84884c82fb9a5796
        </Conference>
    </Dial>
</Response>
