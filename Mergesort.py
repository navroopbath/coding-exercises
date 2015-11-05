import unittest

class Mergesort:
    '''
    Given an array of ints arr as input, return arr in ascending sorted order.
    '''
    @staticmethod
    def mergesort(arr):
        if (arr != None):
            return Mergesort.recursive_mergesort(arr)
        else:
            return None

    '''
    Starts the mergesort in a recursive manner.
    '''
    @staticmethod
    def recursive_mergesort(arr):
        if len(arr) == 0: # an empty array is already 'sorted' so return it
            return []
        if len(arr) == 1: # an array with one element is sorted so return it
            return arr

        mid = len(arr)/2
        # recursively sort both the left and right halves of the array
        left_merge = Mergesort.recursive_mergesort(arr[0:mid])
        right_merge = Mergesort.recursive_mergesort(arr[mid:len(arr)])
        sorted_arr = []

        # grab the first element from left_merge, right_merge, compare them,
        # and insert the smaller element into sorted_arr, and pop the smaller element
        while len(left_merge) > 0 and len(right_merge) > 0:
            left_item = left_merge[0]
            right_item = right_merge[0]
            if left_item <= right_item:
                sorted_arr.append(left_item)
                left_merge.pop(0)
            else:
                sorted_arr.append(right_item)
                right_merge.pop(0)

        if len(left_merge) > 0:
            sorted_arr += left_merge
        if len(right_merge) > 0:
            sorted_arr += right_merge

        return sorted_arr

class TestMergeSortMethods(unittest.TestCase):

  def test_edge_case_empty_array(self):
      test_arr = []
      self.assertEqual(Mergesort.mergesort(test_arr), [])

  def test_edge_case_null_array(self):
      self.assertEqual(Mergesort.mergesort(None), None)

  def test_length_ten_array(self):
      test_arr = [5, 1, 4, 3, 10, 17, 18, 6, 20, 9]
      self.assertEqual(Mergesort.mergesort(test_arr), [1, 3, 4, 5, 6, 9, 10, 17, 18, 20])

if __name__ == '__main__':
    unittest.main()
