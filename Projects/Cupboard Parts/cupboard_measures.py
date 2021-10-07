from openpyxl import Workbook, load_workbook

# Initial measure set
measure_set = {}


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
def measure_count(code, measure):
    measure_list = []

    #seperate the count and measure      
    for n in range(len(measure)):
        measure_list.append([])
        if(measure[n][0].isdigit()):
            measure_list[n].append(int(measure[n][0]))
            measure_list[n].append(measure[n][1:].strip())
        else:
            measure_list[n].append(measure[n])

    #set list into tuple               
    measure_list = [tuple(x) for x in measure_list]

    #seperate same measures in same code  
    if code in measure_set:
        for m_list in measure_list:
                if m_list in measure_set[code]:
                    index = measure_set[code].index(m_list)
                    measure_set[code][index] = list(measure_set[code][index])
                    measure_set[code][index][0] += m_list[0]
                    measure_set[code][index] = tuple(measure_set[code][index])
                else:
                    measure_set[code].append(m_list)
    else:
        measure_set[code] = measure_list
           


#Access excel file to extract data           
def extract_excel(path):
    xlsx_file = path
    wb = load_workbook(xlsx_file)
    ws = wb["VANITY INFO"]

    for row in range(1, ws.max_row+1):
        code = ws.cell(row,3).value
        if code != None:
            if(isinstance(code,int)):
                measure = ws.cell(row,4).value
                measure_part = cleanup_data(measure)
                measure_count(code, measure_part)


if __name__ == "__main__":
    path = 'cupboard_parts.xlsx'
    extract_excel(path)    

#Print values
for key in measure_set:
    print(key , ':' , measure_set[key])
