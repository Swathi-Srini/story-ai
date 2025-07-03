from py2neo import Graph, Node, Relationship
from datetime import datetime

graph = Graph("bolt://localhost:7687", auth=("neo4j", "Thatha@123"))

def save_scene(story_name, user_input, chatbot_reply):
    timestamp = str(datetime.now())
    scene = Node("Scene", text=chatbot_reply, user_input=user_input, timestamp=timestamp)

    story = graph.nodes.match("Story", title=story_name).first()
    if not story:
        story = Node("Story", title=story_name, created_at=timestamp)
        graph.create(story)

    rel = Relationship(scene, "PART_OF", story)
    graph.create(scene | rel)
