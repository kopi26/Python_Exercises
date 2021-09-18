import PySimpleGUI as sg
import os
import traceback
from excel_access import *
from send_mail import *
import re


# Get last time used parameter
def load_config_params(config_file=CONFIG_FILE_NAME):
    if os.path.exists(config_file):
        return retrive_configfile(config_file)
    else:
        return CONFIG_PARAMS

#Update the input values
def update_config_params(input_values,config_params=CONFIG_PARAMS):
    config_params["file_path"]      = input_values[0]
    config_params["reminder_days"]  = int(input_values[1])
    config_params["expiry_title"]   = input_values[2]
    config_params["output_columns"] = [x.strip(' ') for x in input_values[3].split(',')]
    config_params["email"]          = input_values[4]
    
    #update the config json file
    update_configfile(config_params)

#Error msg & Alert msg
def error_msg(msg):
    return sg.popup(msg, title="ALERT", button_color="red", keep_on_top=True)





if __name__ == '__main__':
    
    config_params = load_config_params()

    # email validation
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Add a touch of color
    sg.theme('DarkAmber')   

    # All the stuff inside your window.
    layout = [
            [sg.Text('File: ', size=(35,2)), sg.Input(config_params["file_path"]), sg.FileBrowse()],
            [sg.Text('Reminder Days Count: ', size=(35,2)), sg.InputText(config_params["reminder_days"])],
            [sg.Text('Expiry Date Title: ', size=(35,2)), sg.InputText(config_params["expiry_title"])],
            [sg.Text('Output File Columns: ', size=(35,2)), sg.InputText(", ".join(config_params["output_columns"]))],
            [sg.Text('Receiver Mail: ', size=(35,2)), sg.InputText(config_params["email"])],
            [sg.Button('Submit'), sg.Button('Cancel')]
            ]

    # Create the Window
    window = sg.Window('Expiry Notification Reminder', layout)
    
    try:
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, input_values = window.read()

            #close the action
            if event in (None, 'Cancel'):
                 break
            
            #submit function 
            elif event == 'Submit':
                #Input Field Validation
                if not '.xlsx' in input_values[0]:
                    sg.popup('Please Select Excel File !',text_color='Red')
                elif not input_values[1]:
                    error_msg( 'Please Fill Reminder Days Count !')   
                elif not input_values[2]:
                    error_msg( 'Please Fill Expiry Date Title !')
                elif not input_values[3]:
                    error_msg( 'Please Fill Output File Columns !')
                elif not input_values[4]:
                    error_msg( 'Please Fill Receiver Mail !')
                elif not input_values[1].isdigit():
                    error_msg( 'Reminder Days Count should be an integer !')
                elif not (re.fullmatch(regex, input_values[4])):
                    error_msg('Invalid Email !')
                else:
                    #config json file access
                    update_config_params(input_values)
                    #get parameters
                    config_params = retrive_configfile(CONFIG_FILE_NAME)

                    #Excel process functions
                    config_params = retrive_configfile(CONFIG_FILE_NAME)
                    result = parse_xlsx_header(config_params)
                
                    #Excel Column Validation
                    if not(result[0] is None):
                        error_msg(result[0])
                    else:
                        data = get_xlsx_data(result[1])
                        filtered_data = filter_data(data, config_params)
                        #Check Filter Data set availabiity
                        if not filtered_data:
                            sg.popup('Oops, No Reminder Clients are Available !', title="Message", keep_on_top=True)
                        else:    
                            write_xlsx_file(filtered_data,config_params)
                            #sending mail
                            send_email(config_params["email"], "Car park expiry remainder", "", OUTPUT_FILE_NAME)
                            sg.popup('Successfully Mail Sent !', title="Message", keep_on_top=True)
                      
        #close the window
        window.close()

    #Display the sytem crash error
    except Exception as e:
        tb = traceback.format_exc()
        sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)
    
    
