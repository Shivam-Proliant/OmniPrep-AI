CREATE TABLE IF NOT EXISTS textbook_context (
    id SERIAL PRIMARY KEY,
    domain VARCHAR(100) NOT NULL,
    topic VARCHAR(100) NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO textbook_context (domain, topic, content) VALUES
('Physics', 'Thermodynamics', 'Thermodynamics is the branch of physics that deals with the relationships between heat and other forms of energy. The first law states that energy cannot be created or destroyed.'),
('Chemistry', 'Chemical Kinetics', 'Chemical kinetics is the study of reaction rates and how they are affected by variables such as concentration, temperature, and catalysts.'),
('Mathematics', 'Calculus', 'Calculus is the mathematical study of continuous change. Differential calculus concerns instantaneous rates of change and slopes of curves.');
