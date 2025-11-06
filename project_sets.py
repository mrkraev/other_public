# -*- coding: utf-8 -*-
import copy

from siman import header
from siman.set_functions import InputSet, inherit_iset, make_sets_for_conv, init_default_sets


# 0 or 8 - no relaxation
# 1 or 9 - only atoms
# 2 - full relax; 


#set_potential uses relative paths


user_vasp_sets = [
('static_light', 'static', {'KSPACING': 0.3, 'EDIFF': 1e-4}), 
]


'''
setname = 'static' #SP
if init or setname not in varset: #init only once
    s = InputSet(setname, calculator = 'vasp') #default starting set without relaxation
    s.kpoints_file = True
    s.add_nbands = 1.5
    s.params = {
        'ISTART'    : 0,
        'NELM'      : 50,
        'EDIFF'     : 1e-05,
        'NSW'       : 0,
        'PREC'      : "Normal",
        'ALGO'      : "Normal",
        'ENCUT'     : 400,
        'ENAUG'     : 400*1.75,
        'KSPACING'  : 0.2,
        'KGAMMA'    : ".TRUE.",
        'LREAL'     : "Auto",
        'ISMEAR'    : 0,
        'SIGMA'     : 0.1,
        'LPLANE'    : ".TRUE.",
        'NPAR'      : 1,
        'mul_nbands_small_cell'      : 3,
        }
    s.vasp_params = s.params
    s.potdir = copy.deepcopy(header.nu_dict)

    s.update()
    header.varset[setname] = copy.deepcopy(s)
    header.varset = read_vasp_sets([('opts' ,'static', {'IBRION'    : 1, 'ISIF'      : 2, 'NSW':20, 'EDIFFG':-0.05, },)] )
'''