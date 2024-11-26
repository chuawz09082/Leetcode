class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Find the k closest elements to a given value x from an array.
        The result should be sorted in ascending order.

        Args:
        arr (List[int]): Input array of integers.
        k (int): Number of closest elements to find.
        x (int): Target value to find closest elements to.

        Returns:
        List[int]: A list of k closest elements, sorted in ascending order.
        """

        # Step 1: Initialize a min-heap
        # The heap stores tuples in the form (distance, element), where:
        # - 'distance' is the absolute difference between the element and x
        # - 'element' is the value of the element itself
        heap = []

        # Step 2: Populate the heap with all elements from the array
        for element in arr:
            # Push the tuple (absolute difference, element) onto the heap
            heapq.heappush(heap, (abs(element - x), element))

        # Step 3: Extract the k smallest elements based on distance
        result = []  # List to store the k closest elements
        while len(result) < k:
            # Pop the smallest element from the heap
            dist, element = heapq.heappop(heap)
            # Append the element to the result list
            result.append(element)

        # Step 4: Sort the result list in ascending order before returning
        result = sorted(result)
        return result
        

        