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

# dictionary of possible cuts
cutDict = {
    'selNone' : {
        'cut' : '(0<1)',
        'label' : 'No cuts',
    },
    'sel_Z' : {
        'cut' : '(zed_leptonic_flavour>0)',
        'label' : 'one Z->ll candidate',
        },
    'sel_mZ' : {
        'cut' : '(zed_leptonic_m > 81 && zed_leptonic_m < 101)',
        'label' : 'm(ll) 81-101 GeV',
        },
    'sel_cosThetaZ' : {
        'cut' : '(zed_leptonic_cos_theta < 0.8)',
        'label' : '|cos(theta_ll)|<0.8',
    },
    'sel_mrecoil' : {
        'cut' : '(zed_leptonic_recoil_m > 120 && zed_leptonic_recoil_m < 140)',
        'label' : 'm(recoil) 120-140 GeV',
    },
    'sel_mjj' : {
      #  'cut' : '(higgs_hadronic_m>100 && higgs_hadronic_m<140)',
      #  'label' : '100<m(jets)<140 GeV',
        'cut' : '(higgs_hadronic_m>50 && higgs_hadronic_m<140)',
        'label' : '50<m(jets)<140 GeV',
    },
    'sel_emiss' : {
        'cut' : '(etmiss < 30)',
        'label' : 'Emiss < 30 GeV',
    },                
    'sel_leptonveto' : {
        'cut' : '(n_extraleptons<1)',
        'label' : 'max p(extra lep) < 25 GeV',
    },
    'sel_dmergeok'   : {
        # '(event_d23 >0.) && (event_d34>0.) && (event_d45>0.)'
        'cut' : '(event_d23 >0.) && (event_d34>0.)',
        'label' :  'd23>0, d34>0',
    },
}

# the selection to be applied:
sel = [
    'selNone',
    'sel_Z',
    'sel_mZ',
    'sel_cosThetaZ',
    'sel_mrecoil',
    # 'sel_mjj',     # removed, will kill H(tautau) otherwise)
    # 'sel_emiss',   # removed, will kill H(tautau) otherwise)
    'sel_leptonveto',
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
