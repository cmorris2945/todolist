import PySimpleGUI as sg
from zip_extractor import extract_archive

label1 = sg.Text("Select archive files...")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="archive")

lable2 = sg.Text("Select Destination Directory")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_button1],
                           [lable2, input2, choose_button2],
                           [extract_button, output_label]])

while True:

    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed!")
window.close()