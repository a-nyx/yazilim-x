<?php

include 'examples.php';

function two_sum($nums, $target)
{
    asort($nums);

    $left = 0;
    $right = count($nums) - 1;
    while ($left < $right) {
        $sum = $nums[$left] + $nums[$right];

        if ($sum == $target) {
            return [$left, $right];
        } elseif ($sum < $target) {
            $left++;
        } else {
            $right--;
        }
    }
}


foreach ($examples as $target => $nums) {
    echo "input: [" . implode(',', $nums) . "] & " . $target . PHP_EOL
        . "answer: [" . implode(',', two_sum($nums, $target)) . "]" . PHP_EOL
        . '---------------' . PHP_EOL;
}
