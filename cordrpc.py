import json
import pypresence
import time
import customtkinter as ctk
from tkinter import messagebox
def poll():
    try:
        RPC = pypresence.Presence(client_id.get())
        RPC.connect()
        start = int(time.time())

        while True:
            btns = [
                {
                    "label": btn1_label.get(),
                    "url": btn1_url.get()
                },
                {
                    "label": btn2_label.get(),
                    "url": btn2_url.get()
                }
            ]
            RPC.update(
            large_image=large_image.get(),
            large_text=large_text.get(),
            details=details.get(),
            state=state.get(),
            start=start,
            buttons=btns
            )
            time.sleep(int(update_time.get()))
    except Exception as e:
        messagebox.showerror("An error occued", message=f"An error occued: {str(e)}")
root = ctk.CTk()
root.title("CordRPC")
l = ctk.CTkLabel(root, text="Welcome to CordRPC!")
client_id = ctk.CTkEntry(root, width=250, placeholder_text="Client ID")
large_image = ctk.CTkEntry(root, width=250, placeholder_text="Large Image")
large_text = ctk.CTkEntry(root, width=250, placeholder_text="Large text")
details = ctk.CTkEntry(root, width=250, placeholder_text="Details")
state = ctk.CTkEntry(root, width=250, placeholder_text="State")
update_time = ctk.CTkEntry(root, width=250, placeholder_text="Update Time")
button_section = ctk.CTkLabel(root, text="Buttons: ")
btn1_section = ctk.CTkLabel(root, text="Button 1: ")
btn1_label = ctk.CTkEntry(root, placeholder_text="Label", width=250)
btn1_url = ctk.CTkEntry(root, placeholder_text="URL", width=250)
btn2_section = ctk.CTkLabel(root, text="Button 2: ")
btn2_label = ctk.CTkEntry(root, placeholder_text="Label", width=250)
btn2_url = ctk.CTkEntry(root, placeholder_text="URL", width=250)
start_btn = ctk.CTkButton(root, text="Start", command=poll)
l.pack()
client_id.pack()
large_image.pack()
large_text.pack()
details.pack()
state.pack()
update_time.pack()
button_section.pack()
btn1_section.pack()
btn1_label.pack()
btn1_url.pack()
btn2_section.pack()
btn2_label.pack()
btn2_url.pack()
start_btn.pack()
if __name__ == "__main__":
    ctk.set_default_color_theme("dark-blue")
    ctk.set_appearance_mode("dark")
    root.mainloop() 

    
    
        
