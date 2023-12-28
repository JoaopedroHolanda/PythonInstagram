import instaloader
from tkinter import *
L = instaloader.Instaloader()
def baixarFotos():
    try:
        profile = instaloader.Profile.from_username(L.context, profileName.get())
    except instaloader.exceptions.ProfileHasNoPicsException:
        print(f"O perfil {profileName.get()} não foi encontrado!")
        exit()

    for post in profile.get_posts():
        if post.typename == 'GraphImage':
            L.download_post(post, target=profileName.get())
            print(f"Baixando: {post.url}")

    private = profile.is_private
    if private == True:
        private_label.config(text="Instagram Privado!!! \n Não é possível baixar as fotos!")
    else:
        private_label.config(text="Fotos baixadas!")

    bio = profile.biography
    bio_label.config(text= "Biografia: " + bio) 

janela = Tk()
janela.title("Baixar fotos do Instagram")
janela.geometry("600x400+500+200")
janela.iconbitmap("Instagram.ico")
label = Label(text="Informe o perfil do Instagram:", font=("Arial", 14, "italic"))
profileName = Entry(width=70, font=("Arial", 12))
baixar = Button(text="Baixar", command=baixarFotos)
bio_label = Label(janela, text="", wraplength=500, font=("Arial", 12))
private_label = Label(janela, font=("Arial", 14, "italic"))

label.pack()
profileName.pack()
baixar.pack()
bio_label.pack()  
private_label.pack()
janela.mainloop()
