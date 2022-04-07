const examples = require('./examples');

const all_subsets = nums => {
    let subsets = [];

    const build_subset = (length, start_index, current_subset) => {
        if (length < 0) return;

        for (let index = start_index; index < nums.length; index++) {
            current_subset.push(nums[index]);
            build_subset(length - 1, index + 1, current_subset);
            current_subset.pop();
        }

        subsets.push([...current_subset]);
    };

    build_subset(nums.length, 0, []);
    return subsets;
};

for (let example of examples) {
    console.log('Set: ', example);
    console.log('Subsets: ', all_subsets(example));
    console.log('-----------------');
}
