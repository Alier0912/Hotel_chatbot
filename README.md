*  🏨 Hotel Booking Assistant

A beginner-friendly rule-based chatbot for hotel booking, wrapped in Python and deployed with Streamlit.
The bot helps users check room availability, book rooms, and interact in a conversational way.

-  ✨ Features

💬 Chat Interface built with Streamlit.

🏷️ Rule-based responses (no ML needed).

🛏️ Supports booking requests, availability queries, and basic greetings.

🎭 Friendly chatbot personality for better user experience.

🌐 Deployable locally or on Streamlit Cloud
.

-  📂 Project Structure
hotel_chatbot/
│── app.py               # Main Streamlit app
│── chatbot.py           # Rule-based chatbot logic
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation

⚙️ Tech Stack

Python 3.9+

Streamlit (UI + deployment)

VS Code (development environment)

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/your-username/hotel_chatbot.git
cd hotel_chatbot

2️⃣ Set Up Virtual Environment (Recommended)
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App Locally
streamlit run app.py


Open http://localhost:8501
 in your browser.

Start chatting with your Hotel Assistant Bot 🎉.

---

🌐 Deployment
Deploy to Streamlit Cloud

Push your project to GitHub.

Go to Streamlit Cloud
.

Click New app → Select your repo → Branch → app.py.

Deploy 🚀.

Share your public app link (e.g. https://username-hotel-bot.streamlit.app).

---

🧑‍💻 Example Usage
You: Hello
Bot: Hi there! Welcome to our Hotel Booking Assistant. How can I help you today?

You: I want to book a single room
Bot: Great choice! A Single room costs $100 per night. How many nights would you like to stay?

----

🔑 Notes

If you use multiple widgets with the same label in Streamlit, always add a unique key=.

Example:

user_input = st.text_input("You:", "", key="chat_input")

🛠️ Future Improvements

Add memory so the bot remembers past conversations.

Integrate a real booking API or database.

Add payment gateway simulation.

Switch from rule-based logic → NLP powered chatbot (e.g., spaCy, HuggingFace, LangChain).

----

👨‍💻 Author

Your Name

GitHub: Alier0912

LinkedIn: Awal Alier
