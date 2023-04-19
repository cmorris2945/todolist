import PySimpleGUI as sg

label1 = sg.Text("1) Select your files that you want to compress...")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("2) Select your destination folder...")
input2 = sg.Input()
choose_button2 = sg.FilesBrowse("Choose")

compress_button = sg.Button("COMPRESS!")

window = sg.Window("File Compressor Application",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])


window.read()
window.close()