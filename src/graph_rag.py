from neo4j import GraphDatabase

class AdaptiveGraphRAG:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def get_next_node(self, current_topic: str, target_difficulty: int):
        """
        Traverses the Neo4j Graph to find the next logical topic or cross-domain link
        based on the student's new Markov state.
        """
        query = """
        MATCH (current:Topic {name: $topic})-[r:LEADS_TO|CROSS_DOMAIN_LINK]->(next:Topic)
        WHERE next.difficulty_level = $diff
        RETURN next.name AS next_topic, next.domain AS domain, type(r) AS relation
        ORDER BY rand() LIMIT 1
        """
        with self.driver.session() as session:
            result = session.run(query, topic=current_topic, diff=target_difficulty)
            record = result.single()
            if record:
                return {"topic": record["next_topic"], "domain": record["domain"], "relation": record["relation"]}
            return None
