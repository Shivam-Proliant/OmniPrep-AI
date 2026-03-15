 OmniPrep: Neuro-Symbolic Adaptive Assessment Engine
![alt text](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)

![alt text](https://img.shields.io/badge/Neo4j-Graph_RAG-008CC1?style=for-the-badge&logo=neo4j)

![alt text](https://img.shields.io/badge/FastAPI-Microservice-009688?style=for-the-badge&logo=fastapi)

![alt text](https://img.shields.io/badge/LangChain-LLM_Agent-black?style=for-the-badge)
 Overview
OmniPrep is the "AI Brain" microservice for an adaptive, cross-domain learning platform (integrated with a Node.js/Moodle frontend). Standard testing platforms use static, linear progression. This project implements a Neuro-Symbolic architecture, merging probabilistic mathematics with graph theory and Generative AI to create a truly adaptive Intelligent Tutoring System (ITS).
 Architectural Components
Probabilistic State Tracking (Markov Chains):
Student proficiency and question difficulty are not arbitrarily assigned. They are tracked via a Markov Decision Process (MDP). A transition matrix calculates the mathematical probability of a student advancing or regressing based on real-time answer correctness.
Adaptive Decision Tree (Neo4j Graph RAG):
Questions and concepts are stored as nodes in a Neo4j Knowledge Graph. The system traverses multi-dimensional edges (LEADS_TO, PREREQUISITE_OF, CROSS_DOMAIN_LINK) to seamlessly transition a student from one subject to another based on cognitive links (e.g., bridging Physics to Calculus).
Generative Policy Agent (LLM):
A LangChain-powered LLM acts as the policy orchestrator. It monitors student fatigue and failure rates to dynamically suggest cross-domain pivots, and generates highly specialized MCQs on the fly if the static SQL database runs out of graph nodes.
MLOps & Deployment
This microservice is designed to run asynchronously behind a Node.js backend. It is fully containerized using Docker Compose, orchestrating the Python AI API alongside the Neo4j Graph Database.
```bash
# Spin up the AI microservice and Graph Database
docker-compose up -d --build
```
