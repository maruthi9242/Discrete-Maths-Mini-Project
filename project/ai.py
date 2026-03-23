
from openai import OpenAI
class Ai:
    def createExpression(self):
        client = OpenAI(
            api_key="Groq_Api_Key",
            base_url="https://api.groq.com/openai/v1",
            )
        inp=input("Enter sentence:\n")
        response1 = client.responses.create(

            input=f"""Convert the given sentence into propositional logic components.
            Rules:
            - Use ONLY variables: P, Q, R
            - Assign each variable to a clear statement from the sentence
            - Output ONLY in this exact format:

            P: ...
            Q: ...
            R: ...
            Expression: ...

        - The LAST line must be ONLY the logical expression
        
        - Do NOT include explanations or extra text Sentence: {inp}
        """,
            model="openai/gpt-oss-20b",
        )
        response = client.responses.create(

                input=inp+" Convert the given sentence into a propositional logic expression."
                    " Output only the logical expression. Do not include explanations, "
                    "steps, or extra text Use only uppercase variables (P, Q, R)"
                          ".Use only ~, &, |, >> operators.Do not use Implies().",
                model="openai/gpt-oss-20b",
        )
        print(response1.output_text+"\n")

        return response.output_text

