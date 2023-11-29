# Prompt

A prompt is an instruction to an LLM.

Prompting is about packaging your intent in a natural-language query that will cause the model to return the desired response. A prompt must be clear and specific. The expected result can be requested by breaking the prompt into several instructions to proceed step-by-step.

A good prompt allows the model to work better and give better responses including preventing hallucinations. Prompting is not a science, but *tips & tricks* have been discovered that give better performance.

* Use delimiters to clearly indicate distinct parts of the input
* Ask for a structured output
* Ask the model to check whether conditions are satisfied
* "Few-shot" prompting
* Specify the steps required to complete a task
* Instruct the model to work out its own solution before rushing to a conclusion

Examples of Prompts:

* *"Generate a list of three made-up book titles along with their authors and genres. Provide them in JSON format with the following keys: book_id, title, author, genre."*

* *"Your task is to answer in a consistent style.*

    *< child>: Teach me about patience.*

    *< grandparent>: The river that carves the deepest* valley flows from a modest spring; the grandest symphony originates from a single note; the most intricate 
    tapestry begins with a solitary thread.*
    
    *< child>: Teach me about resilience."*