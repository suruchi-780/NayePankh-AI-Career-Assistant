from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6L0XTacQTvfuJS6txgUo3J5kNA7Vbrq2BIP74lGkli1Aw"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello"
)

print(response.text)