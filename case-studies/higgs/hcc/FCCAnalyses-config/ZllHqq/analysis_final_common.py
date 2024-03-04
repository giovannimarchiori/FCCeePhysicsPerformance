# Input directory where the files produced at the pre-selection level are
# inputDir = "/eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZllHqq/"
inputDir = "/eos/user/g/gmarchio/fcc-test/ZllHqq/analysis-stage1/root/IDEA/"

# Input directory where the files produced at the pre-selection level are
# outputDir = "/eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZllHqq/finalsel/
outputDir = "/eos/user/g/gmarchio/fcc-test/ZllHqq/analysis-final/root/IDEA/"

# Dictonary that contains all the cross section informations etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

# Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
# procDictAdd={"'wzp6_ee_eeH_Hbb_ecm240'":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}}

# Number of CPUs to use
nCPUS = 32

# List of samples
process_list_sig = {
    "wzp6_ee_eeH_Hbb_ecm240": {},
    "wzp6_ee_eeH_Hcc_ecm240": {},
    "wzp6_ee_eeH_Hgg_ecm240": {},
    "wzp6_ee_eeH_Hss_ecm240": {},
    "wzp6_ee_eeH_Htautau_ecm240": {},
    "wzp6_ee_eeH_HWW_ecm240": {},
    "wzp6_ee_eeH_HZZ_ecm240": {},
    #
    "wzp6_ee_mumuH_Hbb_ecm240": {},
    "wzp6_ee_mumuH_Hcc_ecm240": {},
    "wzp6_ee_mumuH_Hgg_ecm240": {},
    "wzp6_ee_mumuH_Hss_ecm240": {},
    "wzp6_ee_mumuH_Htautau_ecm240": {},
    "wzp6_ee_mumuH_HWW_ecm240": {},
    "wzp6_ee_mumuH_HZZ_ecm240": {},
}
process_list_bkg = {
    # "p8_ee_ZZ_ecm240": {},
    # "p8_ee_WW_ecm240": {},
    # "p8_ee_Zqq_ecm240": {},
    # "wzp6_ee_mumu_ecm240": {},
    # "wzp6_ee_ee_Mee_30_150_ecm240": {},
}
processList = process_list_sig | process_list_bkg

#
nosel = "0<1"
sel_Z = "(zed_leptonic_flavour>0)"
sel_mZ = "(zed_leptonic_m > 81 && zed_leptonic_m < 101)"
sel_cosThetaZ = "(zed_leptonic_cos_theta < 0.8)"
sel_mrecoil = "(zed_leptonic_recoil_m > 120 && zed_leptonic_recoil_m < 140)"
sel_mjj = "(higgs_hadronic_m>50 && higgs_hadronic_m<140)"
sel_leptonveto = "(n_extraleptons<1)"
sel_dmergeok = "(event_d23 >0) && (event_d34>0) && (event_d45>0)"

final_selec = nosel
final_selec += (" && " + sel_Z)
final_selec += (" && " + sel_mZ)
final_selec += (" && " + sel_cosThetaZ)
final_selec += (" && " + sel_mrecoil)
final_selec += (" && " + sel_mjj)
# do not apply cut, include in NN - will kill H(tautau) otherwise
# final_selec += " && (etmiss < 30)"
final_selec += (" && " + sel_leptonveto)
# do not apply cut, include in NN - will kill H(tautau) otherwise
#final_selec     += " && (event_d23 >2.0 ) && (event_d34>1.5) && (event_d45>1.0)"
final_selec += (" && " + sel_dmergeok)

# Dictionary of the list of cuts. The key is the name of the selection that will be added to the output file
cutList_treeOnly = {
    "trainNN": final_selec,
}

# Dictionary of the list of cuts for hists only. The key is the name of the selection that will be added to the output file.
cutList_histOnly = {}
cutList_histOnly["selNone"     ] = "0<1"
cutList_histOnly["selN_Z"      ] = cutList_histOnly["selNone"  ] + " && (zed_leptonic_flavour>0)"
cutList_histOnly["selN_mZ"     ] = cutList_histOnly["selN_Z"   ] + " && (zed_leptonic_m > 81 && zed_leptonic_m < 101)"
cutList_histOnly["selN_cos"    ] = cutList_histOnly["selN_mZ"  ] + " && (zed_leptonic_cos_theta < 0.8)"
cutList_histOnly["selN_H"      ] = cutList_histOnly["selN_cos" ] + " && (zed_leptonic_recoil_m > 120 && zed_leptonic_recoil_m<140)"
#cutList_histOnly["selN_mhad"   ] = cutList_histOnly["selN_H"   ] + " && (higgs_hadronic_m > 100 && higgs_hadronic_m < 140)"
#cutList_histOnly["selN_miss"   ] = cutList_histOnly["selN_mhad"] + " && (etmiss < 30)"
#cutList_histOnly["selN_lepveto"] = cutList_histOnly["selN_miss"] + " && (n_extraleptons<1)"
cutList_histOnly["selN_lepveto"] = cutList_histOnly["selN_H"] + " && (n_extraleptons<1)"
cutList_histOnly["finalsel"    ] = final_selec
cutList_histOnly["finalsel_e"  ] = final_selec + " && zed_leptonic_flavour==1"
cutList_histOnly["finalsel_mu" ] = final_selec + " && zed_leptonic_flavour==2"
