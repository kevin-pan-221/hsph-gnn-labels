import openai

# Set up your OpenAI API credentials
openai.api_key = ''

def check_relation(str1, str2, relation):
    prompt = f"{str1} {relation} {str2}. Respond with yes, no, or unsure"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt= prompt,
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
str1 = "insulin"
str2 = "type 1 diabetes"
relation = "treats"
answer = check_relation(str1, str2, relation)
#print(f"{answer} {confidence}")
print(answer)
