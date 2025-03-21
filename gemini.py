from google import genai

client = genai.Client(api_key="AIzaSyAACWLDDhYPrE5HqeW96JAjtOLDBRF5UtM")

# prompt = input("prompt agent: ")

# messages = [
#     {"role": "system", "content": "You are a nice loan acceptance prediction and assistant for small business enterprises"},
#     {"role": "user", "content": prompt}
# ]

# message = f"""

# "You are a nice loan acceptance prediction and assistant for small business enterprises"
# {prompt}

# """

format = '''
    [
        {
            "Business_Idea": "",
            "sector": "",
            "link": ""
        },
        {
            "Business Idea": "",
            "sector": "",
            "link": ""
        }
    ]
    '''

prompt = "Hi, my country is {}. Kindly create a comprehensive list of places I can look out for to get a good loan for my small business establishment both in my country and other countries. Make sure you give the countries of the other countries! Give the answer strictly in this format: {}. Thanks.".format("south africa", format)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)

print(response.text)