import psutil
import time
def main():
    processes = []
    for proc in psutil.process_iter():
        if any(procstr in proc.name() for procstr in ['gmod']):
            processes.append((proc, proc.memory_percent()))
            #print('\n',proc,proc.memory_percent,proc.cpu_percent)
            #print('\n',proc)
            print('[+] GMOD RAM:',proc.memory_percent(),'%')
            
            
            #print('[+] GMOD CPU:',proc.cpu_percent(),'%')#print(proc.cpu_percent)
            #print('[+] CPU:',psutil.cpu_stats())
    
    
            #RAM TRESHOLD
            ram=(psutil.virtual_memory().available)/1024/1024/1024
            print('[+] RAM AVAILABLE:',ram,'GB')
            print('[+] RAM:',psutil.virtual_memory())
            
            #psutil.sensors_temperatures()
    # print('\n',sorted(processes, key=lambda x: x[1]))#[-1][0].kill()
if __name__ == '__main__':
    main()