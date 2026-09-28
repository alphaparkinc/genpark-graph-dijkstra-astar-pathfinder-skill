import sys, json
from client import GraphPathfinder

finder = GraphPathfinder()

def handle_jsonrpc(line):
    global finder
    try:
        req = json.loads(line)
        req_id = req.get("id")
        method = req.get("method")
        if method == "initialize":
            return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "genpark-graph-dijkstra-astar-pathfinder-skill", "version": "1.0.0"}, "capabilities": {"tools": {}}}}
        elif method == "tools/list":
            return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [
                {"name": "find_shortest_path", "description": "Run Dijkstra shortest path.", "inputSchema": {"type": "object", "properties": {"graph": {"type": "object"}, "start": {"type": "string"}, "end": {"type": "string"}}, "required": ["graph", "start", "end"]}},
                {"name": "benchmark_pathfinder", "description": "Run pathfinder benchmark.", "inputSchema": {"type": "object", "properties": {}}}
            ]}}
        elif method == "tools/call":
            params = req.get("params", {})
            tool = params.get("name")
            args = params.get("arguments", {})
            if tool == "find_shortest_path":
                res = finder.dijkstra(args.get("graph", {}), args.get("start"), args.get("end"))
            elif tool == "benchmark_pathfinder":
                res = finder.benchmark_pathfinder()
            else:
                return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}
    except Exception as e:
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}

def main():
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_jsonrpc(line.strip())), flush=True)

if __name__ == "__main__":
    main()
