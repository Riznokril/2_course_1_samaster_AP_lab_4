from queue import PriorityQueue
import queue
from sys import maxsize
from collections import defaultdict


class Graph:
    
    def __init__(self, name_in_file):
        self.visited = []
        number_of_vertices = Graph.create_dict_of_file_data(name_in_file).get("number_of_vertices")
        self.number_of_vertices = number_of_vertices
        self.edges = Graph.create_dict_of_file_data(name_in_file).get("edges")
        self.start_vertex = Graph.create_dict_of_file_data(name_in_file).get("start_vertex")

    def create_dict_of_file_data(name_in_file):
        with open(name_in_file, 'r') as dijkstra_in_file:
            number_of_edges, start_vertex, number_of_vertices = map(int, dijkstra_in_file.readline().split(" "))
            
            edges = [[-1 for i in range(number_of_vertices)] for j in range(number_of_vertices)]
            for i in range(number_of_edges):
                list_data = list(map(int, dijkstra_in_file.readline().split(" ")))
                edges[list_data[0]][list_data[1]] = list_data[2]

        return {"start_vertex": start_vertex, "number_of_vertices": number_of_vertices, "edges": edges}
    
    def dijkstra(self):
        distances = {i:float('inf') for i in range(self.number_of_vertices)}
        distances[self.start_vertex] = 0

        not_visited_verteces = PriorityQueue()
        not_visited_verteces.put((0, self.start_vertex))

        while not not_visited_verteces.empty():
            (dist, current_vertex) = not_visited_verteces.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.number_of_vertices):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = distances[neighbor]
                        new_cost = distances[current_vertex] + distance
                        if new_cost < old_cost:
                            not_visited_verteces.put((new_cost, neighbor))
                            distances[neighbor] = new_cost
        return distances

