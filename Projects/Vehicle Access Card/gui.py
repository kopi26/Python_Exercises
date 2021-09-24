import PySimpleGUI as sg
import os
import traceback
from excel import *
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
    config_params["file_path"]      = file_xlsx
    config_params["reminder_days"]  = int(input_values['dayCount'])
    config_params["expiry_title"]   = input_values['expiry']
    config_params["output_columns"] = input_values['output']
    config_params["email"]          = input_values['email']

    #print(config_params)
    
    #update the config json file
    update_configfile(config_params)

#Error msg & Alert msg
def error_msg(msg):
    return sg.popup(msg, title="ALERT", button_color="red", keep_on_top=True)





if __name__ == '__main__':
    
    config_params = load_config_params()
    

    # email validation
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    #Browse file
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Select File: ', size=(15,2)), sg.Input(config_params["file_path"], key='file', size=(50,2)), sg.FileBrowse()],
        [sg.Button('Ok'), sg.Button('Cancel')]
        ]

    # Create the Window
    window = sg.Window('Expiry Notification Reminder', layout)
    
    while True:
        event, input_values = window.read()

        #close the action
        if event in (None, 'Cancel'):
            break
        elif event == 'Ok':
            #file_xlsx = sg.popup_get_file('File Path:')
            file_xlsx = input_values['file']
            
            if not '.xlsx' in file_xlsx:
                error_msg('Please Select Excel File !')
            else:
                
                # Get Column Titles
                result = parse_xlsx_header(file_xlsx)
                
                if None in result[0]:
                    error_msg('No Data Found !')
                else:
                    #close the window
                    window.close()
                    
                    #Column names
                    col_names = result[0]
                    worksheet = result[1]
                    
                                    
                
                    # Add a touch of color
                    sg.theme('DarkAmber')   

                    # All the stuff inside your window.
                    """
                    layout = [
                            [sg.Text('File: ', size=(35,2)), sg.Input(config_params["file_path"]), sg.FileBrowse()],
                            [sg.Text('Reminder Days Count: ', size=(35,2)), sg.InputText(config_params["reminder_days"])],
                            [sg.Text('Expiry Date Title: ', size=(35,2)), sg.InputText(config_params["expiry_title"])],
                            [sg.Text('Output File Columns: ', size=(35,2)), sg.InputText(", ".join(config_params["output_columns"]))],
                            [sg.Text('Receiver Mail: ', size=(35,2)), sg.InputText(config_params["email"])],
                            [sg.Button('Submit'), sg.Button('Cancel')]
                            ]
                    """

                    layout = [
                            [sg.Text('Reminder Days Count: ', size=(25,2)),
                                 sg.InputText(config_params["reminder_days"], key='dayCount', size=(50,2))],
                            [sg.Text('Expiry Date Title: ', size=(25,2)),
                                 sg.Combo(col_names,default_value='Select Title',key='expiry', size=(50,7))],
                            [sg.Text('Output File Columns: ', size=(25,2)),
                                 sg.Listbox(values=col_names, select_mode='extended',key='output',size=(50,7) )],
                            [sg.Text('Receiver Mail: ', size=(25,2)),
                                 sg.InputText(config_params["email"], key='email', size=(50,2))],
                            [sg.Button('Submit'), sg.Button('Cancel')]
                            ]
                    # Create the Window
                    window = sg.Window('Expiry Notification Reminder', layout)
                
                
                    # Event Loop to process "events" and get the "values" of the inputs
                    while True:
                        event, input_values = window.read()

                        #close the action
                        if event in (None, 'Cancel'):
                            break

                        #submit function 
                        elif event == 'Submit':
                            
                            try:
                                #Input Field Validation
                                
                                if not input_values['dayCount']:
                                    error_msg( 'Please Fill Reminder Days Count !') 
                                elif not input_values['email']:
                                    error_msg( 'Please Fill Receiver Mail !')
                                elif (input_values['expiry'] == 'Select Title'):
                                    error_msg( 'Please Select Expiry Title !')
                                elif not input_values['output']:
                                    error_msg( 'Please Select Output Column(s) !')
                                elif not input_values['dayCount'].isdigit():
                                    error_msg( 'Reminder Days Count should be an integer !')
                                elif not (re.fullmatch(regex, input_values['email'])):
                                    error_msg('Invalid Email !')
                                else:
                                    
                                    #config json file access
                                    update_config_params(input_values)
                                    #get parameters
                                    config_params = retrive_configfile(CONFIG_FILE_NAME)
                                    
                                    #Excel process functions
                                    data = get_xlsx_data(config_params,worksheet)

                                    #Check Data Available
                                    if not data:
                                        error_msg('Data Not Found !')
                                    else:
                                        #Filter data
                                        result = filter_data(data, config_params)
    
                                        if not(result[0] is None):
                                            error_msg(result[0])
                                        else:
                                            #Check Filter Data set availabiity
                                            if not result[1]:
                                                sg.popup('Oops, No Reminder Clients are available !', title="Message", keep_on_top=True)
                                            else:    
                                                write_xlsx_file(result[1],config_params)
                                                
                                                #sending mail
                                                send_email(config_params["email"], "Car park expiry remainder", "", OUTPUT_FILE_NAME)
                                                sg.popup('Successfully mail sent !', title="Message", keep_on_top=True)
                                
                            
                            #Display the sytem crash error
                            except Exception as e:
                                #tb = traceback.format_exc()
                                error_msg(e)
                                #print(tb,e)

                            
                    #close the window
                    window.close()

                    
    #close the window
    window.close()
    
    
