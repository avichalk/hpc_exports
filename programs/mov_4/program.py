import os
import yt
import numpy as np
from yt.visualization.volume_rendering.transfer_function_helper import TransferFunctionHelper
import multiprocessing


lower_bound = 1e-5
upper_bound = 1e10

homdir = "/home/u20/avichalk/exports/11-4"
    
def loop_one():
    global lower_bound
    global upper_bound
    global homdir
    
    os.chdir("/groups/yshirley/skong/s7_t0p1_g512_4pc_isoth_grav_noTurb_rho0p5_rhoamb0p05_b3_resist0p001_vcol2_vshear0p5_T15")
    file_list = os.listdir()
    file_list_2 = []
    for i in file_list:
        if '.athdf' in i:
            if '.xdmf' not in i:
                file_list_2.append(i)
    # #print(file_list_2)

    # # loop through first dir
    i = 0
    theta = 0
    while i <= 20:
        os.chdir("/groups/yshirley/skong/s7_t0p1_g512_4pc_isoth_grav_noTurb_rho0p5_rhoamb0p05_b3_resist0p001_vcol2_vshear0p5_T15")
        data = yt.load(file_list_2[i])
        sc = yt.create_scene(data)
        # really think about it. it needs to go from 0, 4 to 4, 0.

        x = 2
        z = 2
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
        #sc.show()
        os.chdir(homdir)
        sc.save(str(file_list_2[i]+'1')) # weirdest error ever? and i don't know why it's happening? not a big deal, though
        # did end up wasting some time but it's the weekend so
        print('Done with', str(file_list_2[i]))
        i += 1
        
        
def loop_two():
    global lower_bound
    global upper_bound
    global homdir
    
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
        cam.position = data.arr([2, 0, 2], 'code_length')
        cam.zoom(2.5)

        sc.render()
        #sc.show()
        os.chdir(homdir)
        sc.save(str(file_list_2[i]+'2')) # weirdest error ever? and i don't know why it's happening? not a big deal, though
        # did end up wasting some time but it's the weekend so
        print('Done with', file_list_2[i])
        i += 1

        
def loop_three():
    global lower_bound
    global upper_bound
    global homdir
    
    os.chdir("/groups/yshirley/skong/s7_g512_4pc_isoth_grav_noTurb_rho0p5_rhoamb0p05_b3_resist0p001_vcol2_vshear0p5_T15")
    file_list = os.listdir()
    file_list_2 = []
    for i in file_list:
        if '.athdf' in i:
            if '.xdmf' not in i:
                file_list_2.append(i)
    theta = np.pi/4
    i = 0
    while i <= 10:
        os.chdir("/groups/yshirley/skong/s7_g512_4pc_isoth_grav_noTurb_rho0p5_rhoamb0p05_b3_resist0p001_vcol2_vshear0p5_T15")
        data = yt.load(file_list_2[i])
        sc = yt.create_scene(data)

        x = 2
        z = 2
        coord_array = [x, 0, z]

        tfh = TransferFunctionHelper(data)
        tfh.set_field('density')
        tfh.set_log(True)
        tfh.set_bounds()
        sc[0].tfh.bounds = [lower_bound, upper_bound]

        cam = sc.add_camera()
        cam.position = data.arr([x, 0, z], 'code_length')
        cam.zoom(2.5)

        sc.render()
        #sc.show()
        os.chdir(homdir)
        sc.save(str(file_list_2[i]+'3')) # weirdest error ever? and i don't know why it's happening? not a big deal, though
        # did end up wasting some time but it's the weekend so
        print('Done with', str(file_list_2[i]))
        i += 1

def main():
    #p1 = multiprocessing.Process(target=loop_one(), args=())
    p2 = multiprocessing.Process(target=loop_two(), args=())
    p3 = multiprocessing.Process(target=loop_three(), args=())
    
    #p1.start()
    p2.start()
    p3.start()
    
    #p1.join()
    print('DONE ONE')
    p2.join()
    print('DONE TWO')
    p3.join()
    print('DONE THREE')

main()
