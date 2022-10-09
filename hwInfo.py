##################################################################################
# coreInfo
##################################################################################
import gc
import os
import sys
import time
import machine as mc

##################################################################################
# system setting
##################################################################################
gc.enable()
gc.collect()

mc.freq(160000000)

##################################################################################
# system setting
##################################################################################
def show_hw_info():
    uname = os.uname()
    mem_total = gc.mem_alloc()+gc.mem_free()
    free_percent = "("+str((gc.mem_free())/mem_total*100.0)+"%)"
    alloc_percent = "("+str((gc.mem_alloc())/mem_total*100.0)+"%)"
    stat = os.statvfs('/flash')
    block_size = stat[0]
    total_blocks = stat[2]
    free_blocks  = stat[3]
    rom_total = (total_blocks * block_size)/1024
    rom_free = (free_blocks * block_size)/1024
    rom_usage = (rom_total-rom_free)
    rfree_percent = "("+str(rom_free/rom_total*100.0)+"%)"
    rusage_percent = "("+str(rom_usage/rom_total*100.0)+"%)"
    #print("ID ............:",mc.unique_id())
    print("ID ............: ", end="")
    print("".join("\\x%02x" % i for i in mc.unique_id()))
    
    print("Platform ......:",sys.platform.upper())
    print("Version .......:",sys.version)
    print("Memory")
    print("   total ......:",mem_total/1024,"KB")
    print("   usage ......:",gc.mem_alloc()/1024,"KB",alloc_percent)
    print("   free .......:",gc.mem_free()/1024,"KB",free_percent)
    print("ROM")
    print("   total ......:", rom_total,"KB" )
    print("   usage ......:", rom_usage,"KB",rfree_percent )
    print("   Free .......:", rom_free,"KB",rusage_percent )
    print("system name ...:",uname.sysname.upper())
    print("node name .....:",uname.nodename)
    print("release .......:",uname.release)
    print("version .......:",uname.version)
    print("machine .......:",uname.machine)
    print("Frequency .....:",mc.freq())
    try:
        import ulab
        print("ulab ..........:",ulab.__version__)
    except:
        print("ulab ..........: None")
    
##################################################################################
# main program
##################################################################################
try:
    show_hw_info()
except KeyboardInterrupt:
    pass
print("end of program")
