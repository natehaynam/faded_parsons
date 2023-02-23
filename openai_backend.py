# FINETUNING CMD
# set OPENAI_API_KEY="key"
# openai tools fine_tunes.prepare_data -f fine_tuning.jsonl
# openai api fine_tunes.create -t fine_tuning.jsonl -m davinci

import openai

class ml_backend:
    openai.api_key = "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"
    def generate_caption(self, text):
        model = "text-davinci-003"
        text =   "Write a faded parson's problem where inputted code is deleted to create a fill in the blank question for " \
                 "student testing. Example: describe HelloWorld do context \"When testing the HelloWorld class\" do \n it " \
                 "\"The say_hello method should return \'Hello World\'\" do \n hw = HelloWorld.new  \n" \
                 "message = hw.say_hello expect(message).to eq \"Hello World!\" end end end \n ""\n Returns: \n context " \
                 "\“When testing the HelloWorld class\” describe HelloWorld do \n context \“When testing the HelloWorld " \
                 "class\” do \n it \"The say_hello method should return \'Hello World\'\" do \n hw = HelloWorld.new \n " \
                 "message = hw.say_hello \n expect(message).to eq \"Hello World!\" end end enddo \n it \"The say_hello " \
                 "method should return \'Hello World\'\" do  \n hw = ___________  \n message = hw._________________ " \
                 "\n expect(message).to eq \"Hello World!\" end end end Example: "+ text + "\n Return: "
        return ml_backend().model(text, model)
    def model(self, prompt, model):
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=0.71,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0.5
        )
        return response.get("choices")[0]['text']