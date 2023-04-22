import PySimpleGUI as sg
import csv

sg.theme('DarkTeal')

# Read the data from a CSV file
with open("timetable.csv") as csvfile:
    reader = csv.reader(csvfile)
    # Get the headings row
    headings = next(reader)
    # Get the data rows
    data = list(reader)

# Store the original data
originalData = data.copy()

tableLayout = [[sg.Table(values=data,
                    headings=headings,
                    justification='center',
                    row_height=50,
                    font=("Arial", 14),
                    text_color='black',
                    background_color='white',
                    header_font=("Arial", 14),
                    pad=((10,10),(20,10)),
                    key='table'
                    )]]

filterLayout = [[sg.Text("Filter by:", font=("Arial", 16)),
                  sg.Combo(values=['Course Code', 'Instructor', 'Classroom'], font=("Arial", 14), size=11, key='filter'),
                  sg.Button('Filter',font=("Arial", 13),size=6, key='filterBTN'),
                  sg.Button('Reset',font=("Arial", 13),size=6, key='resetBTN')
                  ]]

# Define the window layout
windowLayout = [
    tableLayout,
    filterLayout
]

window = sg.Window("University Timetable", layout=windowLayout, size=(800, 600))

# Loop until the user closes the window
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == 'filterBTN':
        filterCol = values['filter']
        if filterCol == 'Course Code':
            filterValue = sg.popup_get_text("Filter by Course Code:")
        elif filterCol == 'Instructor':
            filterValue = sg.popup_get_text("Filter by Instructor:")
        elif filterCol == 'Classroom':
            filterValue = sg.popup_get_text("Filter by Classroom:")
        filteredData = []
        for row in data:
            if row[headings.index(filterCol)] == filterValue:
                filteredData.append(row)
        window['table'].update(values=filteredData)
    
    if event == 'resetBTN':
        # Update the table element with the original data and clear the filter
        window['table'].update(values=originalData)
        window['filter'].update('')


window.close()
