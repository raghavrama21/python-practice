"""Practice problem to test linting and other code quality tools."""

from tqdm import tqdm


def number_of_ways(start_pos: int, end_pos: int, k: int) -> int:
    """
    Solving Leetcode Problem.
    https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

    Given two positive integers start_pos and end_pos
    Initially, you are standing at position start_pos on an infinite
    number line. With one step, you can move either one position to the left,
    or one position to the right.

    Given a positive integer k, return the number of different ways to
    reach the position end_pos starting from start_pos, such that you
    perform exactly k steps.
    """
    # start with path of length 1
    paths = [[start_pos]]

    # loop k times
    for i in tqdm(range(k)):
        for path in paths.copy():
            new_path = path.copy()
            last_position = new_path[-1]

            # exist fast if not going to make to end
            if end_pos - last_position > (k - i - 1):
                continue
            # path that goes to the left
            new_path_left = new_path + [last_position - 1]

            # path that goes to the right
            new_path_right = new_path + [last_position - 1]

            # add paths to the left and right
            paths.append(new_path_left)
            paths.append(new_path_right)

    num_ways = 0
    for path in paths:
        if path[-1] == end_pos:
            num_ways += 1
    return num_ways


def test_number_of_ways():
    """
    Example 1:

    Input: startPos = 1, endPos = 2, k = 3
    Output: 3
    Explanation: We can reach position 2 from 1 in exactly 3 steps
    in three ways:
    - 1 -> 2 -> 3 -> 2.
    - 1 -> 2 -> 1 -> 2.
    - 1 -> 0 -> 1 -> 2.
    It can be proven that no other way is possible, so we return 3.
    """
    print(number_of_ways(1, 2, 3))


if __name__ == "__main__":
    test_number_of_ways()
