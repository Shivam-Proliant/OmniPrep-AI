from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.markov_engine import MarkovProficiencyScale
from src.graph_rag import AdaptiveGraphRAG
from src.llm_agent import AdaptiveLLMAgent

app = FastAPI(title="OmniPrep AI Brain")

# Initialize modules
markov = MarkovProficiencyScale()
# graph_rag = AdaptiveGraphRAG("bolt://neo4j:7687", "neo4j", "secretpassword")
llm_agent = AdaptiveLLMAgent()

class StudentResponse(BaseModel):
    student_id: str
    current_topic: str
    current_domain: str
    current_markov_state: int
    is_correct: bool
    recent_history: list  # e.g., [True, False, False]

@app.post("/next-step")
async def process_next_step(data: StudentResponse):
    # 1. Calculate new Markov State
    new_state = markov.get_next_state(data.current_markov_state, data.is_correct)
    
    # 2. Check if LLM policy dictates a cross-domain switch
    needs_switch = llm_agent.evaluate_domain_switch(data.recent_history)
    
    next_topic = data.current_topic
    next_domain = data.current_domain
    
    # 3. Query GraphRAG for the Adaptive Decision Tree path
    # (Mocking GraphRAG response for boilerplate)
    # graph_node = graph_rag.get_next_node(data.current_topic, new_state)
    graph_node = {"topic": "Cross-Domain Link Topic", "domain": "New Domain"} if needs_switch else None

    if graph_node:
        next_topic = graph_node["topic"]
        next_domain = graph_node["domain"]
    
    # 4. Generate the next Question
    mcq = llm_agent.generate_mcq(next_domain, next_topic, new_state)
    
    return {
        "student_id": data.student_id,
        "new_markov_state": new_state,
        "domain_switched": needs_switch,
        "next_question": mcq
    }
