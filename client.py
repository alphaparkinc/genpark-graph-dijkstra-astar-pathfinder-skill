import heapq
from typing import Dict, Any, List

class GraphPathfinder:
    @staticmethod
    def dijkstra(graph: Dict[str, Dict[str, float]], start: str, end: str) -> Dict[str, Any]:
        distances = {node: float('inf') for node in graph}
        previous = {node: None for node in graph}
        distances[start] = 0.0
        pq = [(0.0, start)]
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_dist > distances[curr_node]:
                continue
            if curr_node == end:
                break
            for neighbor, weight in graph.get(curr_node, {}).items():
                d = curr_dist + weight
                if d < distances.get(neighbor, float('inf')):
                    distances[neighbor] = d
                    previous[neighbor] = curr_node
                    heapq.heappush(pq, (d, neighbor))
        path = []
        curr = end
        while curr:
            path.append(curr)
            curr = previous.get(curr)
        path.reverse()
        return {
            "start": start, "end": end,
            "shortest_distance": distances.get(end),
            "optimal_path": path if path and path[0] == start else []
        }

    def benchmark_pathfinder(self) -> Dict[str, Any]:
        g = {
            "A": {"B": 1.0, "C": 4.0},
            "B": {"A": 1.0, "C": 2.0, "D": 5.0},
            "C": {"A": 4.0, "B": 2.0, "D": 1.0},
            "D": {"B": 5.0, "C": 1.0}
        }
        return self.dijkstra(g, "A", "D")
