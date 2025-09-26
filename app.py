# app.py

# A simple function to handle conversation
def hotel_bot(user_input, state):
    """
    Rule-based chatbot for hotel booking.
    - user_input: what the user typed
    - state: current step in the conversation
    """

    user_input = user_input.lower()  # make input lowercase for easier matching

    if state == "start":
        return "Hello! Welcome to Sunshine Hotel 🏨. Would you like to book a room, check availability, or cancel a booking?", "main_menu"

    # Main Menu
    elif state == "main_menu":
        if "book" in user_input:
            return "Great! What date would you like to check in? (YYYY-MM-DD)", "ask_checkin"
        elif "availability" in user_input:
            return "Sure 😊 For which date would you like to check availability?", "ask_checkin"
        elif "cancel" in user_input:
            return "Please provide your booking ID to cancel.", "cancel_booking"
        else:
            return "I didn’t understand that ❌. Please type: book, availability, or cancel.", "main_menu"

    # Ask check-in date
    elif state == "ask_checkin":
        return f"Got it! You want to check in on {user_input}. What date will you check out?", "ask_checkout"

    # Ask check-out date
    elif state == "ask_checkout":
        return f"Okay, check-out on {user_input}. How many guests will be staying?", "ask_guests"

    # Ask number of guests
    elif state == "ask_guests":
        return f"Perfect! ✅ I’ll reserve a room for {user_input} guests. Booking confirmed!", "end"

    # Cancel booking
    elif state == "cancel_booking":
        return f"Booking with ID {user_input} has been cancelled. ✅", "end"

    # Default fallback
    else:
        return "Sorry, I didn’t understand that 😕.", "main_menu"

import streamlit as st

# Import the chatbot function
from app import hotel_bot   # if you keep hotel_bot in a separate file
# but if it's in the same file, no need to import

# Initialize session state (to remember the conversation)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "state" not in st.session_state:
    st.session_state.state = "start"

st.title("🏨 Sunshine Hotel Booking Assistant")

# User input
user_input = st.text_input("You:", "")

# Process input when entered
if user_input:
    # Get bot reply
    bot_reply, new_state = hotel_bot(user_input, st.session_state.state)

    # Save chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_reply))

    # Update state
    st.session_state.state = new_state

# Display chat history nicely
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")
