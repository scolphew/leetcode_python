#!/usr/bin/env python

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = {j: i for i, j in enumerate(list1)}
        d2 = {j: i for i, j in enumerate(list2)}

        d3 = {i: d1[i] + d2[i] for i in d1 if i in d2}
        minSum = min(d3.values())
        return [k for k in d3 if d3[k] == minSum]


if __name__ == "__main__":
    s = Solution()
    x = s.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Burger King", "Tapioca Express", "Shogun"],
    )
    print(x)
