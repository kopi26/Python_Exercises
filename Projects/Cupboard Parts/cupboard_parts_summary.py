import sys
from openpyxl import Workbook, load_workbook
from parse_cupboard_parts import *

workbook = None
cupboard_parts = {}
cupboard_orders = []
<<<<<<< HEAD

ordered_materials = []
ordered_style = []
ordered_color = []
ordered_measure = []

#Default Values
materials = []
styles = []
colors = []
"""
#Initail Values
materials = [
    "MAPLE",
    "OAK",
    "MDF",
    "HARDROCK"
    ]
    
styles = [
    "RICHMOND FLAT",
    "RICHMOND RAISED",
    "ASHTON FLAT",
    "ASHTON RAISED",
    "MONACO FLAT",
    "MONACO RAISED",
    "HAMPTON FLAT",
    "HAMPTON RAISED",
    "SHAKER",
    "BEADED SHAKER",
    "FUSION",
    "URBAN",
    "MADISON",
    "SIERRA",
    "KENZO FLAT",
    "KENZO RAISED",
    "LOTUS FLAT",
    "LOTUS RAISED",
    "VISTA FLAT",
    "VISTA RAISED",
    "CAPRICE FLAT",
    "CAPRICE RAISED",
    "RUBY"
    ]
colors = [
    AHM 10 MATTE
    AHM 10 H/G
    AHM 20 MATTE
    AHM 20 BISCUIT H/G
    AHM 30 MATTE
    AHM 40 MATTE
    AHM 1000
    AHM 1100
    AHM 1200
    AHM 1300
    AHM 1400
    AHM 1500
    AHM 1600
    AHM 1700
    AHM 1800
    AHM 1900
    AHM 2000
    AHM 2100
    AHM 2200
    AHM 2300
    AHM 2400
    AHM 2500
    AHM 2600
    AHM 2700
    AHM 2800
    AHM 2900
    AHM 3000
    AHM 3100
    AHM 3200
    AHM 3300
    "AHM 3400",
    "AHM 3500",
        ]
"""


=======
>>>>>>> 8cdb2fc8ba268931dcc8cf12085aadf7086459c2

#get excel access
def access_excel(path):
    xlsx_file = path
    wb = load_workbook(xlsx_file)
    return wb



#set the data as same format and cleanup unnecessary characters
def cleanup_data(measure):
    if measure:
        measure = measure.replace('-','')
        measure = measure.replace('x',' X ')
        measure = measure.replace('X',' X ')
        #set single space    
        measure_str = ' '.join(measure.split())
        
        return measure_str
    
    

#Extract cupboard parts default measures data           
def extract_VANITY_INFO():
    ws = workbook["VANITY INFO"]

    for row in range(1, ws.max_row+1):
        code = ws.cell(row,3).value
        if code != None:
            if(isinstance(code,int)):
                measure = ws.cell(row,4).value
                measure_part = cleanup_data(measure)
                cupboard_parts[code] = split_parts_details(measure_part,code,row)

<<<<<<< HEAD
    """                         
    for code in cupboard_parts:
        print(code , ':')
        for part in cupboard_parts[code]:
            print(part)
        print()


    """
#Extract cupboard parts default material,style and color data
def extract__INFO_SHEET():
    ws = workbook["INFO SHEET"]

    for row in range(1, ws.max_row+1):
        material_name = ws.cell(row,2).value
        style_name = ws.cell(row,6).value
        color_name = ws.cell(row,1).value
        if material_name != None:
            if not material_name in materials:
                materials.append(material_name)
            else:
                print(f'DUPLICATE material: {material_name}')
        if style_name != None:
            if not style_name in styles:
                styles.append(style_name)
            else:
                print(f'DUPLICATE style: {style_name}')
        if color_name != None:
            if not color_name in colors:
                colors.append(color_name)
            else:
                print(f'DUPLICATE color: {color_name}')
                
            

def set_ordered_items(material,style,color,row):
    if material in materials:
        if not material in ordered_materials:
            ordered_materials.append(material)
    else:
        print(f'INVALID material : {material} -> [ROW: {row}]')

    if style in styles:
        if not style in ordered_style:
            ordered_style.append(style)
    else:
        print(f'INVALID style : {style} -> [ROW: {row}]')

    if color in colors:
        if not color in ordered_color:
            ordered_color.append(color)
    else:
        print(f'INVALID color : {color} -> [ROW: {row}]')

    

=======
>>>>>>> 8cdb2fc8ba268931dcc8cf12085aadf7086459c2
    
#get orders details
def get_Orders_MAIN_SHEET():
    ws = workbook["Main Sheet"]
    order_list = []
    
    for row in range(1, ws.max_row+1):
        order_code = ws.cell(row,5).value
<<<<<<< HEAD
        if order_code != None:
            if(isinstance(order_code,int)):
                material = ws.cell(row,8).value
                style = ws.cell(row,7).value
                color = ws.cell(row,9).value
                #get ordered types of values
                set_ordered_items(material,style,color,row)
                
                if order_code in cupboard_parts:
                    order_list = cupboard_parts[order_code]
                    for order in order_list: 
                        order.insert(1,material)
                        order.insert(2,style)
                        order.insert(3,color)
                        
                        #join types by underscore
                        order[1] = '_'.join(order[1:])

                        #remove same items after join from list
                        del order[2:]
    
                        check_list = cupboard_orders.copy()
                        if cupboard_orders:
                            for parts in cupboard_orders:
                                if order[1] in parts[1]:
                                    index = cupboard_orders.index(parts)
                                    cupboard_orders[index][0] += order[0]
                                else:
                                    check_list.remove(parts)
                            else:
                                cupboard_orders.append(order)
                        
                        else:
                            cupboard_orders.append(order)
=======
        if(isinstance(order_code,int)):
            material = ws.cell(row,8).value.strip()
            style = ws.cell(row,7).value.strip()
            color = ws.cell(row,9).value.strip()
            
            if order_code in cupboard_parts:
                order_list = cupboard_parts[order_code]
                for order in order_list:
                    # Create a new order list
                    order = order[:]

                    order.insert(1,material)
                    order.insert(2,style)
                    order.insert(3,color)
                    
                    #join types by underscore
                    order[1] = '_'.join(order[1:])

                    #remove same items after join from list
                    del order[2:]

                    for parts in cupboard_orders:
                        if order[1] == parts[1]:
                            index = cupboard_orders.index(parts)
                            cupboard_orders[index][0] += order[0]
                            break
                    else:
                        cupboard_orders.append(order)
            else:
                print(f'INVALID order number {order_code} in row {row}')
>>>>>>> 8cdb2fc8ba268931dcc8cf12085aadf7086459c2
                    
    for parts in cupboard_orders:
        print(parts)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <excel_file>')
        exit(1)
    path = sys.argv[1]
    workbook = access_excel(path)
    extract_VANITY_INFO()
    get_Orders_MAIN_SHEET()
   
