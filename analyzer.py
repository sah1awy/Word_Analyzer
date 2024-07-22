import customtkinter
from app2 import *

# Set appearance mode and color theme
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Initialize the main application window
root = customtkinter.CTk()
root.geometry("500x350")
root.title("Word Analyzer")

# Function to handle the login action
def analyze():
    w = entry1.get()
    
    # Checking if the word is valid or not
    if w.isalpha():
        # You can uncomment glove but it will take sometime
        # g = Glove()

        # arr = g.nearest_neighbors(w)

        s = Synset(w)
        defi = s.definition()
        x = s.syn_ant()

        # Hide The Main Application
        root.withdraw()
        # Create a new Toplevel window for the output
        output_window = customtkinter.CTkToplevel()
        output_window.title(f"{w.capitalize()} Analysis")
        output_window.geometry("500x250")
        
        # Schedule the output window to close after 60 seconds
        output_window.after(6000000 , output_window.destroy)
        
        # Create a label in the new window to display the output
        word_label = customtkinter.CTkLabel(master=output_window, text=f"Word: {w}", font=("Roboto", 20))
        word_label.pack(pady=5, padx=0)
        def_label = customtkinter.CTkLabel(master=output_window, text=f"Definition: {defi}", font=("Roboto", 20),anchor='w',text_color='gray',justify='left')
        def_label.pack(pady=5, padx=2,anchor='w')
        syn_label = customtkinter.CTkLabel(master=output_window, text="Synonyms: " + " , ".join(list(set(x[0]))), font=("Roboto", 16),anchor='w',text_color='gray',justify='left')
        syn_label.pack(pady=5,padx=2, anchor='w')
        ant_label = customtkinter.CTkLabel(master=output_window, text="Antonyms: " + ' , '.join(list(set(x[1]))), font=("Roboto", 16),anchor='w',text_color='gray',justify='left')
        ant_label.pack(pady=5,padx=2, anchor='w')
        # neighhbor_label = customtkinter.CTkLabel(master=output_window,text='Nearest Neighbors: '+' - '.join(arr))
        # neighhbor_label.pack(pady=5,padx=2, anchor='w')
        # Close the main application window
        output_window.protocol("WM_DELETE_WINDOW", lambda: [output_window.destroy(), root.destroy()])

    else:
        error_label.configure(text="Invalid Word")
        error_label.pack(pady=5)

# Create a frame to contain the login widgets
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

# Create and pack the login label
label = customtkinter.CTkLabel(master=frame, text="Word Analyzer", font=("Roboto", 24))
label.pack(pady=12, padx=10)

# Create and pack the username entry widget
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Enter The Word')
entry1.pack(pady=12, padx=10)

# Create and pack the login button
button = customtkinter.CTkButton(master=frame, text="Analyze", command=analyze)
button.pack(pady=12, padx=10)

# Create an error label for invalid login attempts
error_label = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 12), text_color="red")

# Run the application's main loop
root.mainloop()
