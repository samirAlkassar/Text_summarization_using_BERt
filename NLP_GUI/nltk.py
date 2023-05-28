from tkinter import filedialog
import sys
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import customtkinter
from BERT import summarize

# Create the main window
root = tk.Tk()
root.title("KDD project")
root.geometry("1500x800")
root.configure(bg="#1c1c1c")

# Create the left sidebar
sidebar = tk.Frame(root, width=200, bg="orange")
sidebar.pack(side="left", fill="y")

# Add the logo to the sidebar
logos = Image.open(r"C:\\Users\\East-Sound\Desktop\\NLP_GUI\\logos.jpg")
width, hight = logos.size
new_width = int(width * 0.15)  # reduce the width by 50%
new_height = int(hight * 0.15)  # reduce the height by 50%
logos = logos.resize((new_width, new_height), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(logos)

logo = tk.Label(sidebar, image=logo_image, bg="black")
logo.pack(pady=20, padx=10)

# Add the pages to the sidebar
pages = ["Home Page", "Summarize", "About Team"]
page_frames = {}
for page in pages:
    frame = tk.Frame(root, bg="black")
    frame.pack(side="right", fill="both", expand=True)
    page_frames[page] = frame

# Define the styles for the buttons in the sidebar
style = ttk.Style()
# style.configure("Sidebar.TButton", fg="red",
#                 bg="red", font=("Helvetica", 14), width=25)


home_content = tk.Frame(page_frames["Home Page"], bg="#1c1c1c")  # bg Color
home_content.pack(fill="both", expand=True)

# =========================background===========================
background = Image.open(
    r"C:\\Users\\East-Sound\Desktop\\KDD_project\\325463.png")
# load the images
width, hight = background.size
new_width = int(width * 0.70)  # reduce the width by 50%
new_height = int(hight * 0.70)  # reduce the height by 50%
background = background.resize((new_width, new_height), Image.ANTIALIAS)
image4 = ImageTk.PhotoImage(background)

# =========================Homecontent===========================
# ================================photos import================================
image_1 = Image.open(r"C:\\Users\\East-Sound\Desktop\sideBar\samir.jpeg")
# load the images
width, hight = image_1.size
new_width = int(width * 0.2)  # reduce the width by 50%
new_height = int(hight * 0.2)  # reduce the height by 50%
image_1 = image_1.resize((new_width, new_height), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(image_1)


image_3 = Image.open(r"C:\\Users\\East-Sound\Desktop\\NLP_GUI\\abdo.png")
# ==================================load the images===============================
width, hight = image_3.size
new_width = int(width * 0.45)  # reduce the width by 50%
new_height = int(hight * 0.45)  # reduce the height by 50%
image_3 = image_3.resize((new_width, new_height), Image.ANTIALIAS)
image3 = ImageTk.PhotoImage(image_3)
# ==================================images captions==================================
home_picture_3 = tk.Label(home_content, image=image4)
home_picture_3.place(x=-10, y=-10)

home_title = tk.Label(home_content, text="Home Page", font=(
    "Helvetica", 25), fg="white", bg="#1c1c1c")
home_title.pack(pady=20)

cap2 = tk.Label(home_content, text="Dr. Aya El-Zoghby", font=(
    "Arial", 20, 'bold'), fg="black", bg="orange", bd=2, padx=10, pady=5, width=20)
cap2.place(x=450, y=140)
# create labels with the images

home_picture_1 = tk.Label(home_content, image=image1)
home_picture_1.place(x=250, y=250)

home_picture_3 = tk.Label(home_content, image=image3)
home_picture_3.place(x=750, y=250)

samir = tk.Label(home_content, text="Samir Elsaed Elkassar", font=(
    "Helvetica", 16, 'bold'), fg="black", bg="orange")
samir.place(x=245, y=480)

ziad = tk.Label(home_content, text="abd Elhamed abdo ashry", font=(
    "Helvetica", 16, 'bold'), fg="black", bg="orange")
ziad.place(x=730, y=480)

cap1 = tk.Label(home_content, text="Computer Science", font=(
    "Arial", 12), fg="#c5cadb", bg="black")
cap1.place(x=270, y=540)

cap3 = tk.Label(home_content, text="Information technology", font=(
    "Arial", 12), fg="#c5cadb", bg="black")
cap3.place(x=770, y=540)
# ================================================================================
# ================================[ kmeaans content ]===========================================

kmeans_content = tk.Frame(page_frames["Summarize"], bg="#1c1c1c")
kmeans_content.pack(fill="both", expand=True)

frame = tk.Frame(kmeans_content, bg="gray", width=700, height=720)
frame.place(x=300, y=20)


kmeans_title = tk.Label(kmeans_content, text="Summarization", width=15,
                        font=("Helvetica", 20, 'bold'), fg="black", bg="orange")
kmeans_title.place(x=535, y=40)


kmeans_button_1 = customtkinter.CTkButton(width=150, text_color='black', font=('Helvetica', 14, 'bold'),
                                          master=kmeans_content, text="BERT", fg_color=('#a3e4d7'))

kmeans_button_1.place(x=400, y=150)

text_widget_bert = tk.Label(kmeans_content, text="you can chose BERT to \n summarize your input text using \n Pre-trained BERT model",
                            bg='gray', font=('Helvetica', 13))
text_widget_bert.place(x=350, y=190)

kmeans_button_1 = customtkinter.CTkButton(width=150, text_color='black', font=('Helvetica', 14, 'bold'),
                                          master=kmeans_content, text="Sequence-to-sequence", fg_color=('#a3e4d7'))

kmeans_button_1.place(x=760, y=150)

text_widget_seq = tk.Label(kmeans_content, text="you can chose seq2seq to \n summarize your input text using \n sequence-To-sequence model",
                           bg='gray', font=('Helvetica', 13))
text_widget_seq.place(x=720, y=190)
# =============[ comands ]===========================================
input_var3 = tk.StringVar()


input_field = customtkinter.CTkEntry(
    kmeans_content, textvariable=input_var3, width=500, height=50, bg_color='black', fg_color='white', text_color='black')
input_field.place(x=400, y=320)


def get_text():
    text = input_var3.get()
    summary = summarize(text)
    output_text.insert(tk.END, summary + "\n")
# ====================================================================


kmeans_button_1 = customtkinter.CTkButton(text_color='black', font=('Helvetica', 16, 'bold'), width=240, height=40,
                                          master=kmeans_content, text="Summarize", fg_color=('orange', 'orange'), command=get_text)
kmeans_button_1.place(x=540, y=385)


# ============================K-means input===============

apriori_result = tk.Label(kmeans_content, text="Input Your Text Here", font=(
    "Helvetica", 15, 'bold'), fg="black", bg="gray")
apriori_result.place(x=550, y=280)


# =======================================================
# result label (show restuls)


# create a Text widget with a larger size
output_text = tk.Text(kmeans_content, height=11, width=50)
output_text.place(x=372, y=440)

# change the size of the Text widget dynamically
output_text.config(font=("Helvetica", 14))

# define a function to redirect the program output to the Text widget


def redirect_output():
    sys.stdout = OutputRedirector(output_text)

# define a class to redirect the output to the Text widget


class OutputRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert("end", text)
        self.text_widget.see("end")


# call the redirect_output function to redirect the output


# run your program

# ================================[ aprior content ]===========================================

# ================================[ about us content ]===========================================
about_content = tk.Frame(page_frames["About Team"], bg="#1c1c1c")
about_content.pack(fill="both", expand=True)
about_title = tk.Label(about_content, text="About Us Page", font=(
    "Helvetica", 20), fg="white", bg="#1c1c1c")
about_title.pack(pady=20)
about_us = """
Welcome to our team! We are a group of computer science college students passionate about using technology 
to solve real-world problems. Our project focuses on text summarization using BERT and Seq2seq models, which 
are cutting-edge approaches to natural language processing.

Our team consists of Samir Elkassar and Abdo Ashry, two computer science students with a strong background in 
machine learning and natural language processing. Samir is a skilled programmer who has worked on several projects related to 
natural language processing, while Abdo has experience in data analysis and machine learning.

We are fortunate to have the guidance of Dr. Aya Elzoghby, a respected professor in the computer science 
department with extensive expertise in natural language processing. Dr. Elzoghby provides valuable insights and feedback on our project, 
and helps us stay up-to-date with the latest research in the field.

Our project on text summarization using BERT and Seq2seq models is an exciting opportunity to apply our skills 
and knowledge to a real-world problem. Text summarization is a challenging task that has many practical applications, 
such as summarizing news articles or scientific papers for quick reference.

We are committed to delivering a high-quality project that showcases the potential of BERT and Seq2seq models for text summarization. 
We believe thatour work can contribute to advancing the field of natural language processing and help improve the efficiency and accuracy 
of text summarization techniques.

At our core, we believe in the power of technology to make a positive impact on society. We are driven by a 
desire to apply our skills and knowledge to solve real-world problems and make a meaningful difference in the world.

Thank you for considering our team and our project. We are excited about the potential of our work and look 
forward to sharing our results with the wider community.
"""
about_text = tk.Label(about_content, text=about_us, font=(
    "Helvetica", 14), fg="white", bg="#1c1c1c")
about_text.pack(pady=20)


# Define a function to switch between pages


def show_page(page):
    for p in pages:
        if p == page:
            page_frames[p].pack(fill="both", expand=True)
        else:
            page_frames[p].pack_forget()


# Add the sidebar buttons
home_button = customtkinter.CTkButton(command=lambda: show_page("Home Page"), width=240, height=40, font=("Arial", 16, 'bold'),
                                      master=sidebar, text="Home Page", fg_color=('dodger blue', 'dodger blue'))
home_button.pack(pady=9)

kmeans_button = customtkinter.CTkButton(command=lambda: show_page("Summarize"), width=240, height=40, font=("Arial", 16, 'bold'),
                                        master=sidebar, text="Summarize", fg_color=('dodger blue', 'dodger blue'))
kmeans_button.pack(pady=9)


about_button = customtkinter.CTkButton(command=lambda: show_page("About Team"), width=240, height=40, font=("Arial", 16, 'bold'),
                                       master=sidebar, text="About Team", fg_color=('red', 'dodger blue'))
about_button.pack(pady=9)
about_button = customtkinter.CTkButton(width=250,
                                       master=sidebar, text="", fg_color=('orange', 'orange'))
about_button.pack(pady=10)


# Set the style for the sidebar buttons


# Show the home page initially
show_page("Home Page")


# Run the app
root.mainloop()
