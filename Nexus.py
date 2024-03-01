import sys
import os
import customtkinter
from tkinter import filedialog, END
import csv
from PyPDF2 import PdfReader
import warnings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

key = "REPLACE WITH YOUR OWN API KEY"
model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True,
                               google_api_key=key, temperature=0.5)

warnings.filterwarnings("ignore")

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class GUI:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.MainWindow = customtkinter.CTk()
        self.MainWindow.geometry("750x550")
        self.MainWindow.title("Nexus")

        # Title Label
        title = customtkinter.CTkLabel(
            self.MainWindow, text="Chat With Nexus", font=customtkinter.CTkFont(size=30, weight="bold")
        )
        title.pack(padx=10, pady=(40, 20))

        # Main Frame (Chat)
        self.chat_frame = customtkinter.CTkFrame(master=self.MainWindow)
        self.chat_frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Scrollbar (for automatic scrolling)
        self.chat_scrollbar = customtkinter.CTkScrollbar(self.chat_frame)
        self.chat_scrollbar.pack(side="right", fill="y")

        # Chat Display (text box with scrollbar)
        self.chat_text = customtkinter.CTkTextbox(
            self.chat_frame, height=10, width=60, wrap="word", state="disabled",
            yscrollcommand=self.chat_scrollbar.set
        )
        self.chat_text.pack(pady=12, padx=10, fill="both", expand=True)
        # Corrected line
        self.chat_scrollbar.configure(command=self.chat_text.yview)

        # Chat Entry
        self.query = customtkinter.CTkEntry(self.chat_frame, placeholder_text="Ask question here")
        self.query.pack(pady=12, padx=10, fill="x", expand=True)

        # Ask Button
        ask_button = customtkinter.CTkButton(master=self.chat_frame, text="Ask", command=self.ask)
        ask_button.pack(pady=12, padx=10)

        # Dedicated Area (Upload)
        upload_frame = customtkinter.CTkFrame(master=self.MainWindow)
        upload_frame.pack(pady=10, padx=60, fill="x")

        # Upload Button
        upload_button = customtkinter.CTkButton(master=upload_frame, text="Upload Document",
                                               command=self.upload_and_read_file)
        upload_button.pack(pady=12, padx=10)

        self.content = ""

        self.MainWindow.mainloop()

    def ask(self):
        user_query = self.query.get()
        response = model(
            [
                SystemMessage(
                    content=f"This is the content of the file you have a job to complete the given task related to"
                            f"this content: {self.content}"
                ),
                HumanMessage(content=user_query),
            ]
        )

        self.display_message(f"Nexus: {response.content}\n\n")

    def upload_and_read_file(self):
        file_types = [("Text files", "*.txt"), ("CSV files", "*.csv"), ("PDF files", "*.pdf")]
        file_path = filedialog.askopenfilename(filetypes=file_types)

        if file_path:
            try:
                if file_path.endswith(".csv"):
                    with open(file_path, "r") as file:
                        data = csv.reader(file)
                        self.content = "\n".join([", ".join(row) for row in data])
                elif file_path.endswith(".pdf"):
                    with open(file_path, "rb") as file:
                        reader = PdfReader(file)
                        self.content = "\n".join(page.extract_text() for page in reader.pages)
                else:
                    with open(file_path, "r") as file:
                        self.content = file.read()

            except Exception as e:
                self.display_message("Please choose appropriate file!")

    def display_message(self, message):
        self.chat_text.configure(state="normal")
        self.chat_text.insert(END, message)
        # Automatically scroll to the bottom after inserting new message
        self.chat_text.see(END)
        self.chat_text.configure(state="disabled")


Nexus = GUI()
