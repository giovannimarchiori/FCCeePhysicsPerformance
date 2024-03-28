# import common definitions
import os, sys
configdir = os.getenv('FCCANACONFS')
sys.path.append(configdir)
from analysis_config import *

# Input directory where the files produced at the pre-selection level are
inputDir = ''
# Output directory where the output files will be saved
outputDir = ''

if user == 'almaloiz':
    inputDir = ' /eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZllHqq/'
    outputDir = '/eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZllHqq/finalsel/'
elif user == 'gmarchio':
    inputDir = basedir + '/analysis-stage1/'
    outputDir = basedir + '/analysis-final/'
print('Input directory: ', inputDir)
print('Output_directory: ', outputDir)

# Number of CPUs to use (defined in analysis_config)
# Can be overridden with:
# nCPUS = 96

# List of samples (defined in analysis_config)
# Can be overridden with:
# processList = { : {} }
processList = {
    'wzp6_ee_eeH_Huu_ecm240' : {},
    'wzp6_ee_eeH_Hdd_ecm240' : {},
    'wzp6_ee_mumuH_Huu_ecm240' : {},
    'wzp6_ee_mumuH_Hdd_ecm240' : {},
#    'wzp6_ee_eeH_Hbs_ecm240' : {},
#    'wzp6_ee_eeH_Hbd_ecm240' : {},
#    'wzp6_ee_eeH_Hsd_ecm240' : {},
#    'wzp6_ee_eeH_Hcu_ecm240' : {},
#    'wzp6_ee_mumuH_Hbs_ecm240' : {},
#    'wzp6_ee_mumuH_Hbd_ecm240' : {},
#    'wzp6_ee_mumuH_Hsd_ecm240' : {},
#    'wzp6_ee_mumuH_Hcu_ecm240' : {},
}
# Dictionary of the list of cuts when applying the selection and saving the trees.
# The key is the name of the selection that will be added to the output file
# Defined in analysis_config, can be overridden with:
# cutList_treeOnly = {
#     'finalsel': final_selec,
# }

# Dictionary of the list of cuts for hists only.
# The key is the name of the selection that will be added to the output file.
# Defined in analysis_config, can be overridden with:
# cutList_histOnly = {}
# cutList_histOnly['selNone'     ] = '0<1'
