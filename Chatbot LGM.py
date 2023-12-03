from tkinter import *

# Create the main window
window = Tk()
window.title("Chat Box")

# Create a Text widget for chat history
chat_history = Text(window, height=10, width=50)
chat_history.pack()

# Create an Entry widget for user input
user_input = Entry(window, width=50)
user_input.pack()

# Define a function to handle user messages
def send_message():
  message = user_input.get()
  chat_history.insert(END, "User: " + message + "\n")
  user_input.delete(0, END)

# Create a Button for sending messages
send_button = Button(window, text="Send", command=send_message)
send_button.pack()

# Run the main loop
window.mainloop()
