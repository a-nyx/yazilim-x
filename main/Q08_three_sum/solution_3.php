<?php

include 'examples.php';

function three_sum($nums)
{
    return null;
}

function two_sum($nums, $start_index, $target)
{
    return null;
}


foreach ($examples as $example) {
    $results = three_sum($example);
    $answers = "";
    foreach ($results as $answer) {
        $answers .= PHP_EOL . implode(",", $answer);
    }
    $output = "input: [" . implode(',', $example) . "]" . PHP_EOL
        . "answers: " . $answers . PHP_EOL
        . '---------------';

    echo $output;
}
