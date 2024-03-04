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
    inputDir = basedir+'/analysis-stage1/'
    outputDir = basedir+'/analysis-final/'
print('Input directory: ', inputDir)
print('Output_directory: ', outputDir)

# Number of CPUs to use
# nCPUS = 96

# List of samples
# process_list_sig = {
#     'wzp6_ee_eeH_Hbb_ecm240': {},
#     'wzp6_ee_eeH_Hcc_ecm240': {},
#     'wzp6_ee_eeH_Hgg_ecm240': {},
#     'wzp6_ee_eeH_Hss_ecm240': {},
#     'wzp6_ee_eeH_Htautau_ecm240': {},
#     'wzp6_ee_eeH_HWW_ecm240': {},
#     'wzp6_ee_eeH_HZZ_ecm240': {},
#     #
#     'wzp6_ee_mumuH_Hbb_ecm240': {},
#     'wzp6_ee_mumuH_Hcc_ecm240': {},
#     'wzp6_ee_mumuH_Hgg_ecm240': {},
#     'wzp6_ee_mumuH_Hss_ecm240': {},
#     'wzp6_ee_mumuH_Htautau_ecm240': {},
#     'wzp6_ee_mumuH_HWW_ecm240': {},
#     'wzp6_ee_mumuH_HZZ_ecm240': {},
# }
# process_list_bkg = {
#     'p8_ee_ZZ_ecm240': {},
#     'p8_ee_WW_ecm240': {},
#     'p8_ee_Zqq_ecm240': {},
#     'wzp6_ee_mumu_ecm240': {},
#     'wzp6_ee_ee_Mee_30_150_ecm240': {},
# }
# processList = process_list_sig | process_list_bkg

#
nosel = '0<1'
sel_Z = '(zed_leptonic_flavour>0)'
sel_mZ = '(zed_leptonic_m > 81 && zed_leptonic_m < 101)'
sel_cosThetaZ = '(zed_leptonic_cos_theta < 0.8)'
sel_mrecoil = '(zed_leptonic_recoil_m > 120 && zed_leptonic_recoil_m < 140)'
sel_mjj = '(higgs_hadronic_m>50 && higgs_hadronic_m<140)'
sel_leptonveto = '(n_extraleptons<1)'
sel_dmergeok = '(event_d23 >0.) && (event_d34>0.) && (event_d45>0.)'

final_selec = nosel
final_selec += (' && ' + sel_Z)
final_selec += (' && ' + sel_mZ)
final_selec += (' && ' + sel_cosThetaZ)
final_selec += (' && ' + sel_mrecoil)
final_selec += (' && ' + sel_mjj)
# do not apply cut, include in NN - will kill H(tautau) otherwise
# final_selec += ' && (etmiss < 30)'
final_selec += (' && ' + sel_leptonveto)
# do not apply cut, include in NN - will kill H(tautau) otherwise
# final_selec     += ' && (event_d23 >2.0 ) && (event_d34>1.5) && (event_d45>1.0)'
# final_selec += (' && ' + sel_dmergeok)

# Dictionary of the list of cuts. The key is the name of the selection that will be added to the output file
cutList_treeOnly = {
    'trainNN': final_selec,
}

# Dictionary of the list of cuts for hists only. The key is the name of the selection that will be added to the output file.
cutList_histOnly = {}
cutList_histOnly['selNone'     ] = '0<1'
cutList_histOnly['selN_Z'      ] = cutList_histOnly['selNone'  ] + ' && (zed_leptonic_flavour>0)'
cutList_histOnly['selN_mZ'     ] = cutList_histOnly['selN_Z'   ] + ' && (zed_leptonic_m > 81 && zed_leptonic_m < 101)'
cutList_histOnly['selN_cos'    ] = cutList_histOnly['selN_mZ'  ] + ' && (zed_leptonic_cos_theta < 0.8)'
cutList_histOnly['selN_H'      ] = cutList_histOnly['selN_cos' ] + ' && (zed_leptonic_recoil_m > 120 && zed_leptonic_recoil_m<140)'
#cutList_histOnly['selN_mhad'   ] = cutList_histOnly['selN_H'   ] + ' && (higgs_hadronic_m > 100 && higgs_hadronic_m < 140)'
#cutList_histOnly['selN_miss'   ] = cutList_histOnly['selN_mhad'] + ' && (etmiss < 30)'
#cutList_histOnly['selN_lepveto'] = cutList_histOnly['selN_miss'] + ' && (n_extraleptons<1)'
cutList_histOnly['selN_lepveto'] = cutList_histOnly['selN_H'] + ' && (n_extraleptons<1)'
cutList_histOnly['finalsel'    ] = final_selec
cutList_histOnly['finalsel_e'  ] = final_selec + ' && zed_leptonic_flavour==1'
cutList_histOnly['finalsel_mu' ] = final_selec + ' && zed_leptonic_flavour==2'
