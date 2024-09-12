import openai

# Set up your OpenAI API credentials
openai.api_key = ''

def check_relation():
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt= "Insulin treats type 1 diabetes. Respond with yes or no",
        max_tokens=3,
        n=1,
        stop=None,
        temperature=0,
        logprobs=0
    )
    answer = response.choices[0].text.strip().lower()
    #confidence = round(response.choices[0].logprobs.token_logprobs[0], 2) * 100
    #return answer, confidence
    return answer


# Example usage
answer = check_relation()
#print(f"{answer} {confidence}")
print(answer)
