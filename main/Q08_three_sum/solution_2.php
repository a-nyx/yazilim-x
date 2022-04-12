<?php

include 'examples.php';

function three_sum($nums)
{
    sort($nums);
    $answers = [];

    for($i = 0; $i < count($nums)-2; $i++) {
        if($i > 0 && $nums[$i] == $nums[$i-1]) {
            continue;
        }

        $subtotal = 0 - $nums[$i];
        $left = $i + 1;
        $right = count($nums) - 1;

        while($left < $right) {
            if($nums[$left] + $nums[$right] == $subtotal) {
                $answers[] = [$nums[$i], $nums[$left], $nums[$right]];
                $left++;
                $right--;
                while($left < $right && $nums[$left] == $nums[$left-1]) {
                    $left++;
                }
            } else if($nums[$left] + $nums[$right] < $subtotal) {
                $left++;
            } else {
                $right--;
            }
        }
    }

    return $answers;
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
