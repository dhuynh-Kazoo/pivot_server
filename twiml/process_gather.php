<?php
header("content-type: text/xml");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";

$digits = $_REQUEST['Digits'];
$separated_digits = '';
foreach (str_split($digits) as $digit) {
    $separated_digits = $separated_digits . " " . $digit;
}

if($_REQUEST['Digits'] == "123") {
    echo "<Response><Say>Good job! This was just a test, the call will end now</Say></Response>";
} else {
    echo "<Response><Say>Wrong, you entered " . trim($separated_digits) .  ". Bye!</Say></Response>";
}
?>