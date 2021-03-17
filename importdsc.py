def import_dsc(filename, time_between_scans = 10):
    
    output = []
    store_data = False
    
    with open(filename) as file:
        time_offset = 0
        
        while 1:
            line = file.readline()
        
            if not line:
                break
            
            if 'Program step 2' in line:
                time_offset = time_between_scans + t
                line = file.readline()
                line = file.readline()
                line = file.readline()
                line = file.readline()
                line = file.readline()
                line = file.readline()
                line = file.readline()
                line = file.readline()
                line = file.readline()
                
                
            if store_data:
                data_line = list(dict.fromkeys(line.split(' ')))
                
                t_string = [float(j) for j in data_line[1].split(':')]
           
                t = t_string[0]*60*60 + t_string[1]*60 + t_string[2]

                
                t = float(t) 
                T = float(data_line[2])
                X = float(data_line[3])
                output.append([t + time_offset, T, X])
            
            if 'Data step 1' in line:
                store_data = True
                
                line = file.readline()
                line = file.readline()
                
        return np.array(output) 