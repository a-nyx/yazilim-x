<?php

include 'examples.php';

function three_sum($nums)
{
    // find all triplets
    $answers = [];
    for ($x = 0; $x < count($nums); $x++) {
        for ($y = $x + 1; $y < count($nums); $y++) {
            for ($z = $y + 1; $z < count($nums); $z++) {
                if ($nums[$x] + $nums[$y] + $nums[$z] == 0) {
                    $answer = [$nums[$x], $nums[$y], $nums[$z]];
                    sort($answer);
                    $answers[] = $answer;
                }
            }
        }
    }

    // remove duplicates
    for ($i = 0; $i < count($answers); $i++) {
        for ($k = $i + 1; $k < count($answers); $k++) {
            if ($answers[$i] == $answers[$k]) {
                array_splice($answers, $k, 1);
                $k--;
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
