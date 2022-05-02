from email.mime import image
from tkinter import *
from tkinter import ttk
from library import download_image_from_url, set_desktop_background_image
from pokeapi import get_pokemon_list, get_pokemon_image_url
import os 
import sys
import ctypes
from pickle import FRAME

def main():
    
    script_dir = sys.path[0] 
    image_dir = os.path.join(script_dir, 'images')
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    #Making the selected image set to the taskbar
    root = Tk()
    root.title('Pokemon Image Viewer')
    app_id = 'pokemon.image.viewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

    #Calling the image to be set as taskbar image
    root.iconbitmap(os.path.join(script_dir, 'pokemon.ico'))



    #Sizing the window and making sure it can't stretch out things, as well can't shrink image down
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.minsize(500, 600)
    frm = ttk.Frame(root)
    frm.grid(sticky=(N,S,E,W))
    frm.rowconfigure(0, weight=1)
    frm.columnconfigure(0, weight=1)

    img_poke = PhotoImage(file=os.path.join(script_dir, 'pokeball.png'))
    lbl_img = ttk.Label(frm, image=img_poke)
    lbl_img.grid(row=0, column=0, padx=10, pady=10)

    pokemon_list = get_pokemon_list()
    pokemon_list.sort()
    pokemon_list = [p.capitalize() for p in pokemon_list]
    cbo_pokemon = ttk.Combobox(frm, values=pokemon_list, state='readonly')
    cbo_pokemon.set('Select a Pokemon')
    cbo_pokemon.grid(row=1, column=0, padx=10, pady=10)

    def handle_poke_select(event):
        """
        Being able to choose amongst different pokemon.
        """
        pokemon_name = cbo_pokemon.get()
        image_url = get_pokemon_image_url(pokemon_name)
        image_path = os.path.join(image_dir, pokemon_name + '.png')
        download_image_from_url(image_url, image_path)
        img_poke['file'] = image_path
        btn_set_desktop.state(['!disabled'])


    cbo_pokemon.bind('<<ComboboxSelected>>', handle_poke_select)

    def handle_btn_set_desktop():
        """
        Setting the button up to connect the image and set it as a background
        """ 
        pokemon_name = cbo_pokemon.get()
        image_path = os.path.join(image_dir, pokemon_name + '.png')
        set_desktop_background_image(image_path)

    btn_set_desktop = ttk.Button(frm, text='Set as Desktop Image', command=handle_btn_set_desktop)
    btn_set_desktop.state(['disabled'])
    btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)


    root.mainloop()

main()
