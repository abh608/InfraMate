import google.generativeai as genai
import json
from mock_system_stats import get_mock_stats

# Your Gemini API key
genai.configure(api_key="YOUR_API_KEY")  # Replace with your real key

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_infraMate(question):
    stats = get_mock_stats()
    system_context = (
        f"System as of {stats['timestamp']}:\n"
        f"- CPU: {stats['cpu_percent']}%\n"
        f"- RAM: {stats['ram_percent']}%\n"
        f"- Disk: {stats['disk_storage_percent']}%\n"
    )
    full_prompt = f"{system_context}\nUser asked: {question}"
    response = model.generate_content(full_prompt)
    print("🧠", response.text)

if __name__ == "__main__":
    while True:
        q = input("❓ Ask InfraMate: ")
        if q.lower() in ["exit", "quit"]:
            break
        ask_infraMate(q)
