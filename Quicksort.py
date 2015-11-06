import random
import unittest

class Quicksort():
    @staticmethod
    def quicksort(arr):

        if (arr != None):
            # recursively sorts the array in place
            Quicksort.quicksort_in_place(arr, 0, len(arr)-1)
        else:
            return None

    @staticmethod
    def quicksort_in_place(arr, first, last):

        # if there's fewer than 2 items in the array, array is sorted so
        # don't modify it
        if last - first < 1:
            return

        # choose a random pivot for O(n log n) average time complexity
        pivot_index = random.randint(first, last)

        # move the pivot out of the way temporarily by placing it at
        # the end of the array
        pivot = arr[pivot_index]
        arr[pivot_index] = arr[last]
        arr[last] = pivot

        # define two indices i, j such that array elements at index <= i
        # are <= pivot and array elements at index >= j are  >= pivot
        i, j = first-1, last
        while i < j:

            i += 1
            while arr[i] < pivot:
                i += 1

            j -= 1
            while arr[j] > pivot and j > first:
                j -= 1

            if i < j:
                # swap arr[i] and arr[j]
                arr[i], arr[j] = arr[j], arr[i]

        # swap the pivot with item at index i
        arr[i], arr[last] = arr[last], arr[i]
        # recursively sort the left and right halves of the array
        Quicksort.quicksort_in_place(arr, 0, i-1)
        Quicksort.quicksort_in_place(arr, i+1, last)

class TestQuicksortMethods(unittest.TestCase):

  def test_edge_case_empty_array(self):
      test_arr = []
      Quicksort.quicksort(test_arr)
      self.assertEqual(test_arr, [])

  def test_edge_case_null_array(self):
      self.assertEqual(Quicksort.quicksort(None), None)

  def test_length_ten_array(self):
      test_arr = [5, 1, 4, 3, 10, 17, 18, 6, 20, 9]
      Quicksort.quicksort(test_arr)
      self.assertEqual(test_arr, [1, 3, 4, 5, 6, 9, 10, 17, 18, 20])

if __name__ == '__main__':
    unittest.main()
