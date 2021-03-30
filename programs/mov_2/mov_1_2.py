import os
import yt
import numpy as np
from yt.visualization.volume_rendering.transfer_function_helper import TransferFunctionHelper
#loop through 2nd dir

lower_bound = 1e-5
upper_bound = 1e10

os.chdir("/groups/yshirley/skong/s7_t0p01_g512_4pc_isoth_grav_noTurb_rho0p5_rhoamb0p05_b3_resist0p001_vcol2_vshear0p5_T15")
file_list = os.listdir()
file_list_2 = []
for i in file_list:
    if '.athdf' in i:
        if '.xdmf' not in i:
            file_list_2.append(i)
i = 0
while i <= 10:
    os.chdir("/groups/yshirley/skong/s7_t0p01_g512_4pc_isoth_grav_noTurb_rho0p5_rhoamb0p05_b3_resist0p001_vcol2_vshear0p5_T15") 
    data = yt.load(file_list_2[i])
    sc = yt.create_scene(data)
    
    
    tfh = TransferFunctionHelper(data)
    tfh.set_field('density')
    tfh.set_log(True)
    tfh.set_bounds()
    sc[0].tfh.bounds = [lower_bound, upper_bound]
    
    cam = sc.add_camera()
    cam.position = data.arr([4, 0, 0], 'code_length')
    cam.zoom(2.5)
    
    sc.render()
    #sc.show()
    os.chdir("/home/u20/avichalk/exports/29_3_export")
    sc.save(str(str(i+30))) # weirdest error ever? and i don't know why it's happening? not a big deal, though
    # did end up wasting some time but it's the weekend so
    print('Done with', file_list_2[i])
    i += 1
