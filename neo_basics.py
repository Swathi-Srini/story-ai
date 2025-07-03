from py2neo import Graph

graph = Graph("bolt://localhost:7687", auth=("neo4j", "Thatha@123"))

try:
    graph.run("RETURN 1")
    print("🔥 CONNECTION SUCCESSFUL 🔥")
except Exception as e:
    print("🚨 Connection failed: ", e)
