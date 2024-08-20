import customtkinter as ctk

janela = ctk.CTk()

janela._set_appearance_mode("light")

btn = ctk.CTkButton(master = janela, text='Test')
btn.pack()

janela.mainloop()