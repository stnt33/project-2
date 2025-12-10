#I used AI for a few lines here, but i made changes and learned the code.
from tkinter import *
import logic


class GUI:
    def __init__(self, window):
        self.window = window
        self.window.title("VOTING APPLICATION")

        #ID frame
        self.frame_id = Frame(self.window)
        self.label_id = Label(self.frame_id, text="ID")
        self.entry_id = Entry(self.frame_id, width=20)
        self.label_id.pack(side='left', padx=5)
        self.entry_id.pack(side='left', padx=5)
        self.frame_id.pack(pady=10)

        # Candidate row
        self.frame_candidate = Frame(self.window)
        self.label_candidate = Label(self.frame_candidate, text='CANDIDATES')
        self.radio_choice = StringVar()
        self.radio_choice.set("__none__")
        self.radio_john = Radiobutton(self.frame_candidate, text='John', variable=self.radio_choice, value='John')
        self.radio_jane = Radiobutton(self.frame_candidate, text='Jane', variable=self.radio_choice, value='Jane')
        self.label_candidate.pack(pady=5)
        self.radio_john.pack(pady=5)
        self.radio_jane.pack(pady=5)

        self.frame_candidate.pack(pady=10)


        # Buttons
        self.frame_button = Frame(self.window)

        self.button_vote = Button(self.frame_button, text='SUBMIT VOTE', width=18, command=self.vote)
        self.button_vote.pack(pady=10)



        self.frame_button.pack()

        self.frame_message = Frame(self.window)
        self.label_message = Label(self.frame_message, text='Enter ID and choose a candidate')
        self.label_message.pack(pady=10)
        self.frame_message.pack()

        self.entry_id.focus()

    def show_message(self, text, color='red'):
        """AI helped me with this function"""
        self.label_message.config(text=text, fg=color)

    def vote(self):
        try:
            voter_id = self.entry_id.get().strip()
            candidate = self.radio_choice.get()

            # check ID
            if voter_id == "":
                self.show_message("Please enter your ID.", "red")
                return

            if not voter_id.isdigit():
                self.show_message("ID must be a number.", "red")
                return

            if int(voter_id) == 0:
                self.show_message("ID cannot be 0.", "red")
                return

            # check candidate
            if candidate not in ("John", "Jane"):
                self.show_message("Please select a candidate.", "red")
                return

            # add vote using logic file
            added = logic.add_vote(voter_id, candidate)
            if not added:
                self.show_message("Already Voted", "red")
                return

            # after vote
            self.show_message("You voted.", "green")

            # clear any inputs
            self.entry_id.delete(0, END)
            self.radio_choice.set("__none__")
            self.entry_id.focus()

        except Exception:
            self.show_message("Something went wrong.", "red")


