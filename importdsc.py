def import_dsc(filename, time_between_scans = 10, baselined='True'):
    import numpy as np
    
    forward = []
    reverse = []
    
    store_data = False
    store_to_forward = True
    
    with open(filename, errors='ignore') as file:
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
                if store_to_forward:
                    forward.append([t + time_offset, T, X])
                else:
                    reverse.append([t + time_offset, T, X])
                    
            
            if 'Data step 1' in line:
                store_data = True
                
                line = file.readline()
                line = file.readline()
                

        
        return np.array(forward), np.array(reverse)
    
def baselined(xdata, ydata, f_l = -300, f_r = -100, r_l = 100, r_f = 300, order =3, offset = 32.7):

    x_baseline = np.concatenate([xdata[f_l:f_r], xdata[r_l:r_f]]) 
    y_baseline = np.concatenate([ydata[f_l:f_r], ydata[r_l:r_f]]) 

    baseline_fit = np.polyfit(x_baseline, y_baseline, order)
    y_baselined = ydata - np.polyval(baseline_fit, xdata)

    print(baseline_fit)

    return xdata, y_baselined + offset
