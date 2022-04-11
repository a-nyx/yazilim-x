<?php

include 'examples.php';

function three_sum($nums, $target)
{
    return null;
}


foreach ($examples as $target => $nums) {
    echo "input: [" . implode(',', $nums) . "] & " . $target . PHP_EOL
        . "answer: [" . implode(',', three_sum($nums, $target)) . "]" . PHP_EOL
        . '---------------' . PHP_EOL;
}
