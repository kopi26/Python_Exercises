from openpyxl import Workbook, load_workbook

# Initial measure set
cupboard_parts = {}
workbook = None


#set the data in same format
def cleanup_data(measure):
    if measure:
        if '-' in measure:
            measure = measure.replace('-','')
        if 'X' in measure:  
            measure = measure.replace('X',' x ')
        #set single space    
        measure_str = ' '.join(measure.split())
        measure_part = measure_str.split('[')
        #remove None values
        measure_part = list(filter(None, measure_part))
        measure_part = [x.replace(']', '').strip() for x in measure_part]
        
        return measure_part

    

#calculate the count of measures
def set_cupboard_parts(code, measure):
    measure_list = []

    #seperate the count and measure      
    for n in range(len(measure)):
        measure_list.append([])
        if(measure[n][0].isdigit()):
            measure_list[n].append(int(measure[n][0]))
            measure_list[n].append(measure[n][1:].strip())
        else:
            measure_list[n].append(measure[n])

    #set measures with code              
    measure_list = [tuple(x) for x in measure_list]
    cupboard_parts[code] = measure_list

    

def access_excel(path):
    xlsx_file = path
    wb = load_workbook(xlsx_file)

    return wb
    

#Access excel file to extract data           
def extract_VANITY_INFO():
    ws = workbook["VANITY INFO"]

    for row in range(1, ws.max_row+1):
        code = ws.cell(row,3).value
        if code != None:
            if(isinstance(code,int)):
                measure = ws.cell(row,4).value
                measure_part = cleanup_data(measure)
                set_cupboard_parts(code, measure_part)


def get_cupboard_orders():
    ws = workbook["Main Sheet"]
    order_list=[]
    for row in range(1, ws.max_row+1):
         order_code = ws.cell(row,5).value
         if order_code != None:
             if(isinstance(order_code,int)):
                 order_list.append(order_code)
    print(order_list)             
    cupboard_parts_count(order_list)
    
def check_match(o_list, m_list):
    if o_list[1] == m_list[1]:
        return True
    else:
        return False

def cupboard_parts_count(order_list):
    cupboardParts_orderList = []
    """
    for order in order_list:
        if order in cupboard_parts:
            print(order, cupboard_parts[order])
            for m_list in cupboard_parts[order]:
                if m_list in cupboardParts_orderList:
                    index = cupboardParts_orderList.index(m_list)
                    cupboardParts_orderList[index] = list(cupboardParts_orderList[index])
                    cupboardParts_orderList[index][0] += m_list[0]
                    cupboardParts_orderList[index] = tuple(cupboardParts_orderList[index])
                else:
                    cupboardParts_orderList.append(m_list)
        else:
            print('Wrong cupboard code !', order)            
    """

    for order in order_list:
        if order in cupboard_parts:
            for m_list in cupboard_parts[order]:
                check_list = cupboardParts_orderList.copy()
                if cupboardParts_orderList:
                    for o_list in cupboardParts_orderList:
                        if o_list[1] == m_list[1]:
                            index = cupboardParts_orderList.index(o_list)
                            cupboardParts_orderList[index] = list(cupboardParts_orderList[index])
                            cupboardParts_orderList[index][0] += m_list[0]
                            cupboardParts_orderList[index] = tuple(cupboardParts_orderList[index])
                        else:
                            check_list.remove(o_list)
                    else:
                        if not check_list:cupboardParts_orderList.append(m_list)
                else:
                    cupboardParts_orderList.append(m_list)
        else:
            print('Wrong cupboard code !', order) 
    
    print('*******')
    for x in cupboardParts_orderList:
        print(x)
    

if __name__ == "__main__":
    path = 'cupboard_parts.xlsx'
    workbook = access_excel(path)
    extract_VANITY_INFO()
    get_cupboard_orders()

    """
    #Print values
    for key in cupboard_parts:
        print(key , ':' , cupboard_parts[key])
    """
