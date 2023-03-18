import math


class Solution:

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def minimum_squares(self) -> list:
        """
        Given a rectangle of dimensions L x W find the minimum number (N) of
        identical squares of maximum side that can be cut out from that
        rectangle so that no residue remains in the rectangle. Also find the
        dimension K of that square.
        :return: list [N, D].
        """
        gcd = math.gcd(self.length, self.width)
        return [int(self.length / gcd) * int(self.width / gcd), gcd]


if __name__ == '__main__':
    sol = Solution(7, 5)
    squ = sol.minimum_squares()
    print(squ)
