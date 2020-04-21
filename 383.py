import unittest
def repeats(string1):
    counter = 0
    if len(string1) == 0:
        return 1
    refString = string1
    for i in range(len(string1)):
        if string1 == refString:
            counter += 1
        string1 = string1[-1] + string1[:-1]
    return counter

def same_necklace(string1, string2):
    if len(string1) != len(string2):
        return False
    for i in range(len(string1)+1):
        if string1 == string2:
            return True
        string1 = string1[-1] + string1[:-1]
    return False


class Test383(unittest.TestCase):
    """
    Test class for 383
    """

    def test_383(self):
        """
        Actual testing
        """
        self.assertTrue(same_necklace("nicole", "icolen"))
        self.assertTrue(same_necklace("nicole", "lenico"))
        self.assertFalse(same_necklace("nicole", "coneli"))
        self.assertTrue(same_necklace("aabaaaaabaab", "aabaabaabaaa"))
        self.assertFalse(same_necklace("abc", "cba"))
        self.assertFalse(same_necklace("xxyyy", "xxxyy"))
        self.assertFalse(same_necklace("xyxxz", "xxyxz"))
        self.assertTrue(same_necklace("x", "x"))
        self.assertFalse(same_necklace("x", "xx"))
        self.assertFalse(same_necklace("x", ""))
        self.assertTrue(same_necklace("", ""))

    def test_383_optional1(self):
        """
        First Optional Point
        """
        self.assertEqual(repeats("abc"), 1)
        self.assertEqual(repeats("abcabcabc"), 3)
        self.assertEqual(repeats("abcabcabcx"), 1)
        self.assertEqual(repeats("aaaaaa"), 6)
        self.assertEqual(repeats("a"), 1)
        self.assertEqual(repeats(""), 1)

    def test_383_optional2(self):
        """
        Second Optional Point
        """
        with open("enable1.txt") as F:
            words = F.readlines()
            for i in range(len(words)):
                words[i] = words[i].strip("\n")

        for i in range(len(words)):
            indices = [i]
            for j in range(i+1, len(words)):
                if same_necklace(words[i], words[j]) == True:
                    indices.append(j)
            if len(indices) > 1:
                print(indices)
                for j in range(len(indices)):
                    print(words[indices[j]])
            if len(indices) == 4:
                print("AHA! I've found the 4 words")
                break





if __name__ == '__main__':
    unittest.main()