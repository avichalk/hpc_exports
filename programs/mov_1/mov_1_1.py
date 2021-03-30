import os
import yt
import numpy as np
from yt.visualization.volume_rendering.transfer_function_helper import TransferFunctionHelper
# loop for directories
# loop for files (change this dir)
os.chdir('/groups/yshirley/skong/s7_t0p1_g512_4pc_isoth_grav_noTurb_rho0p5_rhoamb0p05_b3_resist0p001_vcol2_vshear0p5_T15')
#dir_list = os.listdir()
file_list = os.listdir()
file_list_2 = []
for i in file_list:
    if '.athdf' in i:
        if '.xdmf' not in i:
            file_list_2.append(i)
#print(file_list_2)
lower_bound = 1e-5
upper_bound = 1e10
# loop through first dir
i = 0
theta = 0
while i <= 20:
    os.chdir('/groups/yshirley/skong/s7_t0p1_g512_4pc_isoth_grav_noTurb_rho0p5_rhoamb0p05_b3_resist0p001_vcol2_vshear0p5_T15')
    data = yt.load(file_list_2[i])
    sc = yt.create_scene(data)
        
    x = 4*np.sin(theta)
    z = 4*np.cos(theta)
    coord_array = [x, 0, z]
    
    tfh = TransferFunctionHelper(data)
    tfh.set_field('density')
    tfh.set_log(True)
    tfh.set_bounds()
    sc[0].tfh.bounds = [lower_bound, upper_bound]
    
    cam = sc.add_camera()
    cam.position = data.arr(coord_array, 'code_length')
    cam.zoom(2.5)
    
    sc.render()
    os.chdir('/home/u20/avichalk/exports/21_3_export')
    sc.save(str(str(file_list_2[i])+str(i)))
    theta += np.pi/80
    i += 1
