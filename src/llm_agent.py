from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
import psycopg2

class AdaptiveLLMAgent:
    def __init__(self):
        # In production, ensure OPENAI_API_KEY is in env vars
        self.llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")
        
        # PostgreSQL Connection Config
        self.pg_host = os.getenv("POSTGRES_HOST", "localhost")
        self.pg_port = os.getenv("POSTGRES_PORT", "5432")
        self.pg_user = os.getenv("POSTGRES_USER", "omniprep")
        self.pg_password = os.getenv("POSTGRES_PASSWORD", "omniprep_pass")
        self.pg_db = os.getenv("POSTGRES_DB", "omniprep_db")

    def evaluate_domain_switch(self, student_history: list) -> bool:
        """LLM decides if the student is stuck and needs a cross-domain pivot."""
        prompt = f"""
        Analyze the student's recent performance: {student_history}.
        If they are failing repeatedly in the current domain, return 'SWITCH'. 
        Otherwise, return 'STAY'. Reply with exactly one word.
        """
        # Logic to call LLM (Mocked for boilerplate simplicity)
        # response = self.llm.predict(prompt)
        response = "STAY" # Mock logic
        return response.strip() == "SWITCH"

    def _fetch_context_from_sql(self, domain: str, topic: str):
        """Fetches textbook context from PostgreSQL for RAG."""
        try:
            conn = psycopg2.connect(
                host=self.pg_host,
                port=self.pg_port,
                user=self.pg_user,
                password=self.pg_password,
                database=self.pg_db
            )
            cursor = conn.cursor()
            cursor.execute(
                "SELECT content FROM textbook_context WHERE domain = %s AND topic = %s LIMIT 1",
                (domain, topic)
            )
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            return result[0] if result else "No specific textbook context found."
        except Exception as e:
            print(f"Error fetching from SQL: {e}")
            return "Context unavailable."

    def generate_mcq(self, domain: str, topic: str, difficulty: int):
        """Generates a dynamic MCQ if the static SQL DB runs out of questions."""
        
        # 1. Fetch factual context from PostgreSQL (SQL RAG)
        context = self._fetch_context_from_sql(domain, topic)
        
        prompt = f"""
        Generate a highly complex multiple-choice question for Domain: {domain}, 
        Topic: {topic}, Markov Difficulty Scale: {difficulty}/3.
        
        Base the question STRICTLY on the following textbook context:
        "{context}"
        
        Provide 4 options and the correct answer in strict JSON format.
        """
        # response = self.llm.predict(prompt)
        # Mocking the JSON response
        return {
            "question": f"Based on the context '{context[:30]}...', what is true about {topic} at level {difficulty}?",
            "options": ["A", "B", "C", "D"],
            "correct_answer": "A"
        }
