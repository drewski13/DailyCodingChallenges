import unittest
import two_nums_in_a_list_add_up_to_k


class MyTestCase(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(two_nums_in_a_list_add_up_to_k.sum_two_nums_from_list_to_k([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -1, 18], 13), [(7,6), (8,5), (9,4), (10,3), (11,2), (12,1), (13,0), (-1,14)])
        self.assertEqual(two_nums_in_a_list_add_up_to_k.sum_two_nums_from_list_to_k(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -1, 18], 36),
                         [])
        self.assertFalse(two_nums_in_a_list_add_up_to_k.sum_two_nums_from_list_to_k(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -1, 18], 36),
            [(17, 18)])
        self.assertTrue(two_nums_in_a_list_add_up_to_k.sum_two_nums_from_list_to_k(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -1, 18], 35),
            [(17, 18)])


if __name__ == '__main__':
    unittest.main()
