analysis = 'ZvvHqq-APC'
production = 'winter2023'
detector = 'IDEA'

print('Analysis: ', analysis)
print('Production: ', production)
print('Detector: ', detector)

import getpass
user = getpass.getuser()

import socket
hostname = socket.gethostname()

# Directory that will contain the output files
basedir = ''
import re
if user == 'gmarchio':
    if re.match(r'^lxplus.*\.cern\.ch$', hostname):
        hostname = 'lxplus.cern.ch'
        basedir = '/eos/user/g/gmarchio/fcc/analysis/%s/%s/%s/' % (analysis, production, detector)
    elif hostname == 'apcatlas01.in2p3.fr':
        basedir = '/home/gmarchio/work/fcc/analysis/output/%s/%s/%s/' % (analysis, production, detector)
print('Base directory for output: ', basedir)

# Dictionary that contains all the cross section informations etc...
procDict = 'FCCee_procDict_%s_%s.json' % (production, detector)
print('Dictionary: ', procDict)

# Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
# procDictAdd={"'wzp6_ee_eeH_Hbb_ecm240'":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}}

# Number of CPUs to use
nCPUS = 96

# List of samples
process_list_sig = {
    # Z(nunu)H
    'wzp6_ee_nunuH_Hbb_ecm240' : {},
    'wzp6_ee_nunuH_Hcc_ecm240' : {},
    'wzp6_ee_nunuH_Hss_ecm240' : {},
    'wzp6_ee_nunuH_Hgg_ecm240' : {},
    'wzp6_ee_nunuH_Htautau_ecm240' : {},
    'wzp6_ee_nunuH_HWW_ecm240' : {},
    'wzp6_ee_nunuH_HZZ_ecm240' : {},
    # Z(bb)H
    'wzp6_ee_bbH_Hbb_ecm240' : {},
    'wzp6_ee_bbH_Hcc_ecm240' : {},
    'wzp6_ee_bbH_Hss_ecm240' : {},
    'wzp6_ee_bbH_Hgg_ecm240' : {},
    'wzp6_ee_bbH_Htautau_ecm240' : {},
    'wzp6_ee_bbH_HWW_ecm240' : {},
    'wzp6_ee_bbH_HZZ_ecm240' : {},
    # Z(cc)H
    'wzp6_ee_ccH_Hbb_ecm240' : {},
    'wzp6_ee_ccH_Hcc_ecm240' : {},
    'wzp6_ee_ccH_Hss_ecm240' : {},
    'wzp6_ee_ccH_Hgg_ecm240' : {},
    'wzp6_ee_ccH_Htautau_ecm240' : {},
    'wzp6_ee_ccH_HWW_ecm240' : {},
    'wzp6_ee_ccH_HZZ_ecm240' : {},
    # Z(ss)H
    'wzp6_ee_ssH_Hbb_ecm240' : {},
    'wzp6_ee_ssH_Hcc_ecm240' : {},
    'wzp6_ee_ssH_Hss_ecm240' : {},
    'wzp6_ee_ssH_Hgg_ecm240' : {},
    'wzp6_ee_ssH_Htautau_ecm240' : {},
    'wzp6_ee_ssH_HWW_ecm240' : {},
    'wzp6_ee_ssH_HZZ_ecm240' : {},
    # Z(qq)H
    'wzp6_ee_qqH_Hbb_ecm240' : {},
    'wzp6_ee_qqH_Hcc_ecm240' : {},
    'wzp6_ee_qqH_Hss_ecm240' : {},
    'wzp6_ee_qqH_Hgg_ecm240' : {},
    'wzp6_ee_qqH_Htautau_ecm240' : {},
    'wzp6_ee_qqH_HWW_ecm240' : {},
    'wzp6_ee_qqH_HZZ_ecm240' : {},
}
process_list_bkg = {
    'p8_ee_ZZ_ecm240': {},
    'p8_ee_WW_ecm240': {},
    'p8_ee_Zqq_ecm240': {},
    'wzp6_ee_nuenueZ_ecm240' : {}
}
processList = process_list_sig | process_list_bkg
# for debug use only one sample
# processList = { 'wzp6_ee_nunuH_Hbb_ecm240' : {} }

# dictionary of possible cuts
cutDict = {
    'selNone' : {
        'cut' : '(0<1)',
        'label' : 'No cuts',
    },
    'sel_nolep' : {
        'cut': 'n_selected_leptons<1',
        'label' : 'No leptons with p>20 GeV',
    },
    'sel_jetE' : {
        'cut' : '(jet1_E>15 && jet1_E<105 && jet2_E>10 && jet2_E<70)',
        'label' : '15<E_j1<105, 10<E_j2<70 GeV',
    },
    'sel_cosThetaJJ' : {
        'cut' : 'higgs_hadronic_cos_theta<0.9',
        'label' : '|cos(theta_jj)|<0.9',
    },
    'sel_cosSumThetaJJ' : {
        'cut' : 'higgs_hadronic_cos_dTheta_jj>0.5',
        'label' : 'cos(th_j1+th_j2)>0.5',
    },
    'sel_cosDPhiJJ' : {
        'cut' : 'higgs_hadronic_cos_dPhi_jj<0.999',
        'label' : 'cos(phi_j1-phi_j2)<0.999',
    },
    'sel_mvis_mmiss'   : {
        'cut' : '(mvis > 70 && mvis < 150 && higgs_hadronic_recoil_m>60 && higgs_hadronic_recoil_m<250)',
        'label' : '70<mvis<150, 60<mmiss<250 GeV'
    },    
    'sel_dmergeok'   : {
        # '(event_d23 >0.) && (event_d34>0.) && (event_d45>0.)'
        'cut' : '(event_d23 >0.) && (event_d34>0.)',
        'label' : 'd23>0, d34>0',
    },
}

# the selection to be applied:
sel = [
    'selNone',
    'sel_nolep',
    'sel_jetE',
    'sel_cosThetaJJ',
    'sel_cosSumThetaJJ',
    'sel_cosDPhiJJ',
    'sel_mvis_mmiss',
    'sel_dmergeok',
]
final_sel_cut = 'sel_dmergeok'

# the cuts for each selection step
cuts = {}
print('Cuts:')
for i, cut in enumerate(sel):
    if i==0:
        cuts[cut] = cutDict[cut]['cut']
    else:
        cuts[cut] = cuts[sel[i-1]] + ' && ' + cutDict[cut]['cut']
    print("  %s : %s" % (cut, cuts[cut]))

# the final selection
final_selec = cuts[final_sel_cut]

# Dictionary of the list of cuts when applying the selection and saving the trees.
# The key is the name of the selection that will be added to the output file
cutList_treeOnly = {
    'trainNN' : final_selec,
}

# Dictionary of the list of cuts for hists only.
# The key is the name of the selection that will be added to the output file.
cutList_histOnly = cuts
cutList_histOnly['finalsel'    ] = final_selec
