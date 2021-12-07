import unittest
from dijkstra import Graph

class TestHamster(unittest.TestCase):

    def test_case_1(self):
        graph_test_1 = Graph("dijkstra_in_test_1.txt")
        result = graph_test_1.dijkstra()
        sum_distances = 0
        num_distances = len(result)

        for i in range(num_distances):
            sum_distances += result.get(i)
        self.assertEqual(sum_distances/num_distances, 19/6)

if __name__ == '__main__':
    unittest.main()
