from dijkstra import Graph

if __name__ == '__main__':
    graph = Graph("dijkstra_in_test_1.txt")
    result = graph.dijkstra()
    print(result)
    
    sum_distances = 0
    num_distances = len(result)

    for i in range(num_distances):
        sum_distances += result.get(i)
    print(sum_distances/num_distances)
