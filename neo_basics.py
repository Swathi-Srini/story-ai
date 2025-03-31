# basic query and reply in neo4j database
from py2neo import Graph

# Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Create nodes for Nico and his legal case
nico = graph.nodes.create(name="Nico", role="lawyer")
case_1 = graph.nodes.create(name="Case 1", type="Legal Case")

# Add relationships (edges)
nico_works_on_case = nico.relationships.create("WORKS_ON", case_1)
