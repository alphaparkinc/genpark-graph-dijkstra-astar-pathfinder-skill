from client import GraphPathfinder

def run_example():
    print("=== GenPark Graph Pathfinder Example ===")
    finder = GraphPathfinder()
    print("Optimal Path:", finder.benchmark_pathfinder())

if __name__ == "__main__":
    run_example()
