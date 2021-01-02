# hello_world.py

from heroquest_solo_main import Heroquest_solo
import PySimpleGUIWeb as sg

HQ_SOLO = Heroquest_solo()


layout = [
          [sg.Button("Come è fatto il corridoio?", key = "_AISLES_"),sg.Multiline('', key = "_AISLES_TEXT_", size=(60,6))],
          [sg.Button("Ci sono tesori?", key="_THRESURES_"), sg.Multiline('', key = "_THRESURES_TEXT_", background_color='green', size=(100,3))],
          [sg.Button("Cosa contiene?", key="_CHEST_")],
          [sg.Multiline('', key="_CHEST_TEXT_", size=(100, 3))],
          [sg.Button("Scopri come è fatta la stanza", key="_ROOM_GENERATOR_")],
          [sg.InputText('Inserisci il numero di caselle della stanza', key = "_ROOM_GENERATOR_NUMBER_", size=(100,3))],
          [sg.Multiline('', key="_ROOM_GENERATOR_TEXT_", size=(100, 3))],
          [sg.Button("Ci sono mostri nella stanza?", key="_MONSTERS_GENERATOR_")],
          [sg.Multiline('', key="_MONSTERS_GENERATOR_TEXT_", size=(100, 3))],
          [sg.Button("Ci sono trabocchetti o porte segrete?", key="_TRAPS_SECRET_")],
          [sg.Multiline('', key="_TRAPS_TEXT_", size=(100, 3))],
          [sg.Multiline('', key="_SECRET_DOOR_TEXT_", size=(100, 3))]
          ]
# Create the window
window = sg.Window("Heroquest solo assistant", layout, margins=(105, 105))

# Create an event loop
while True:
    event, values = window.read()

    if event == "_AISLES_":
        msg = HQ_SOLO.aisles(HQ_SOLO.random_numbers())
        window["_AISLES_TEXT_"].update(str(msg))

    if event == "_THRESURES_":
        msg = HQ_SOLO.thresures(HQ_SOLO.random_numbers())
        window["_THRESURES_TEXT_"].update(str(msg))

    if event == "_CHEST_":
        msg = HQ_SOLO.chest(HQ_SOLO.random_numbers())
        window["_CHEST_TEXT_"].update(str(msg))

    if event == "_TRAPS_SECRET_":
        msg_traps = HQ_SOLO.traps(HQ_SOLO.random_numbers())
        msg_secret_door = HQ_SOLO.secret_doors(HQ_SOLO.random_numbers())
        window["_TRAPS_TEXT_"].update(str(msg_traps))
        window["_SECRET_DOOR_TEXT_"].update(str(msg_secret_door))


    if event == "_ROOM_GENERATOR_":
        msg = HQ_SOLO.room_generator(HQ_SOLO.random_numbers(), window["_ROOM_GENERATOR_NUMBER_"].get())
        window["_ROOM_GENERATOR_TEXT_"].update(str(msg))


    if event == "_MONSTERS_GENERATOR_":
        msg = HQ_SOLO.monsters_generator(HQ_SOLO.random_numbers(), window["_ROOM_GENERATOR_NUMBER_"].get())
        window["_MONSTERS_GENERATOR_TEXT_"].update(str(msg))


    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()