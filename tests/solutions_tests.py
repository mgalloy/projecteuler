import unittest
import time
import solutions.euler_1
import solutions.euler_2
import solutions.euler_3
import solutions.euler_4
import solutions.euler_5
import solutions.euler_6
import solutions.euler_7
import solutions.euler_8
import solutions.euler_9
import solutions.euler_10
import solutions.euler_11
import solutions.euler_12
import solutions.euler_13
import solutions.euler_14
import solutions.euler_15
import solutions.euler_16
import solutions.euler_17
import solutions.euler_20


class SolutionsTestCase(unittest.TestCase):
    '''
    Unit tests for Project Euler solutions.
    '''

    test_time = 0.0

    def setUp(self):
      self.test_time = time.time()

    def tearDown(self):
      self.test_time = time.time() - self.test_time
      self.assertTrue(self.test_time < 60.0, msg='too slow: %f seconds' % self.test_time)

    def test_001(self):
        result = solutions.euler_1.euler_1(1000)
        self.assertTrue(result == 233168, msg='incorrect result: %d' % result)

    def test_002(self):
        result = solutions.euler_2.euler_2(4000000)
        self.assertTrue(result == 4613732, msg='incorrect result: %d' % result)

    def test_003(self):
        result = solutions.euler_3.euler_3(600851475143)
        self.assertTrue(result == 6857, msg='incorrect result: %d' % result)

    def test_004(self):
        result = solutions.euler_4.euler_4()
        self.assertTrue(result == 906609, msg='incorrect result: %d' % result)

    def test_005(self):
        result = solutions.euler_5.euler_5(20)
        self.assertTrue(result == 232792560, msg='incorrect result: %d' % result)

    def test_006(self):
        result = solutions.euler_6.euler_6(100)
        self.assertTrue(result == 25164150, msg='incorrect result: %d' % result)

    def test_007(self):
        result = solutions.euler_7.euler_7(10001)
        self.assertTrue(result == 104743, msg='incorrect result: %d' % result)

    def test_008(self):
        result, start_index = solutions.euler_8.euler_8(1000, 13)
        self.assertTrue(result == 23514624000, msg='incorrect result: %d' % result)

    def test_009(self):
        result, a, b, c = solutions.euler_9.euler_9(1000)
        self.assertTrue(result == 31875000, msg='incorrect result: %d' % result)

    def test_010(self):
        result = solutions.euler_10.euler_10(2000000)
        self.assertTrue(result == 142913828922, msg='incorrect result: %d' % result)

    def test_011(self):
        result = solutions.euler_11.euler_11()
        self.assertTrue(result == 70600674, msg='incorrect result: %d' % result)

    # def test_012(self):
    #     result = solutions.euler_12.euler_12()
    #     self.assertTrue(result == , msg='incorrect result: %d' % result)

    def test_013(self):
        result = solutions.euler_13.euler_13(10)
        self.assertTrue(result == '5537376230', msg='incorrect result: %s' % result)

    def test_014(self):
        result, max_len = solutions.euler_14.euler_14(1000000)
        self.assertTrue(result == 837799, msg='incorrect result: %d' % result)

    def test_015(self):
        result = solutions.euler_15.euler_15(20, 20)
        self.assertTrue(result == 137846528820, msg='incorrect result: %d' % result)

    def test_016(self):
        result = solutions.euler_16.euler_16(1000)
        self.assertTrue(result == 1366, msg='incorrect result: %d' % result)

    def test_017(self):
        result = solutions.euler_17.euler_17(1000)
        self.assertTrue(result == 21124, msg='incorrect result: %d' % result)

    def test_020(self):
        result = solutions.euler_20.euler_20(100)
        self.assertTrue(result == 648, msg='incorrect result: %d' % result)


if __name__ == '__main__':
    unittest.main()