import yaml
from crewai import Agent, Task, Crew, LLM

class MbtiLoopCrew:
    def __init__(self):
        with open('agents.yaml', 'r') as f:
            self.agents_config = yaml.safe_load(f)
        with open('tasks.yaml', 'r') as f:
            self.tasks_config = yaml.safe_load(f)
        
        self.ollama_llm = LLM(
            model="ollama/llama3.2:1b", 
            base_url="http://localhost:11434",
            temperature=0.4
        )

    def run(self, mbti_type):
        lister = Agent(config=self.agents_config['gift_lister'], llm=self.ollama_llm)
        picker = Agent(config=self.agents_config['gift_picker'], llm=self.ollama_llm)

        t1 = Task(config=self.tasks_config['brainstorm_task'], agent=lister)
        t2 = Task(config=self.tasks_config['critique_task'], agent=picker)
        t3 = Task(
            config=self.tasks_config['refinement_task'], 
            agent=lister,
            output_file='final_gifts.md'
        )

        crew = Crew(
            agents=[lister, picker],
            tasks=[t1, t2, t3],
            verbose=True
        )
        return crew.kickoff(inputs={'mbti': mbti_type})