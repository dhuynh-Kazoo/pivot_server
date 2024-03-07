<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
?>

<Response>
    <Set>
        <Variable
            timeout="10"
            actionUrl="http://localhost:5000/ecallmgr_extention"
            billing="$1000"    
        /> 
    </Set>
</Response>