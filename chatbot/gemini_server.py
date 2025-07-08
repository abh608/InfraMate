# chatbot/gemini_server.py

import google.generativeai as genai
from monitor.mock_system_stats import get_mock_stats  # fixed path if used as module
import datetime

# 🔐 Configure Gemini with your API key (replace below or use environment variable)
genai.configure(api_key="AIzaSyCiPPM3_mSmUc5OETUURFaC8C_f1btRmo0")  # ⛔️ Replace this before pushing

# 🔄 Load the Gemini 2.5 Flash model
model = genai.GenerativeModel("gemini-2.5-flash")

def ask_infraMate(question: str) -> str:
    """
    Fetches mock system stats and sends them along with the user's question
    to Gemini for a smart response.
    """
    stats = get_mock_stats()

    system_context = (
        f"System Snapshot ({stats['timestamp']}):\n"
        f"- CPU Usage: {stats['cpu_percent']}%\n"
        f"- RAM Usage: {stats['ram_percent']}%\n"
        f"- Disk Usage: {stats['disk_storage_percent']}%\n"
        f"- Disk Read Speed: {stats['read_speed']} MB/s\n"
        f"- Disk Write Speed: {stats['write_speed']} MB/s\n"
    )

    full_prompt = (
        f"{system_context}\n"
        f"User Question: {question}\n"
        f"Respond with actionable system health suggestions."
    )

    try:
        response = model.generate_content(full_prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Gemini API Error: {e}"

if __name__ == "__main__":
    print("🧠 InfraMate CLI Chat – Type 'exit' to quit\n")
    while True:
        q = input("❓ Ask InfraMate: ")
        if q.strip().lower() in ["exit", "quit"]:
            break
        answer = ask_infraMate(q)
        print("🤖", answer, "\n")
