# Input directory where the files produced at the pre-selection level are
inputDir = "/eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZllHqq/"
# inputDir = "/eos/user/g/gmarchio/fcc-new/ZllHqq/analysis/root/IDEA/"
# inputDir = "./testAnalysis/"

# Input directory where the files produced at the pre-selection level are
outputDir = "/eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZllHqq/finalsel/"

# processList = {"wzp6_ee_eeH_Hbb_ecm240": {}}

# Link to the dictonary that contains all the cross section informations etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

# Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
# procDictAdd={"'wzp6_ee_eeH_Hbb_ecm240'":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}}

# Number of CPUs to use
nCPUS = 32

# produces ROOT TTrees, default is False
doTree = True
do_histOnly = False
doNN = True
saveTabular=True

process_list_sig = {
    "wzp6_ee_eeH_Hbb_ecm240": {},
    # "wzp6_ee_eeH_Hcc_ecm240": {},
    # "wzp6_ee_eeH_Hgg_ecm240": {},
    # "wzp6_ee_eeH_Hss_ecm240": {},
    # "wzp6_ee_eeH_Htautau_ecm240": {},
    # "wzp6_ee_eeH_HWW_ecm240": {},
    # "wzp6_ee_eeH_HZZ_ecm240": {},
    # "wzp6_ee_mumuH_Hbb_ecm240": {},
    # "wzp6_ee_mumuH_Hcc_ecm240": {},
    # "wzp6_ee_mumuH_Hgg_ecm240": {},
    # "wzp6_ee_mumuH_Hss_ecm240": {},
    # "wzp6_ee_mumuH_Htautau_ecm240": {},
    # "wzp6_ee_mumuH_HWW_ecm240": {},
    # "wzp6_ee_mumuH_HZZ_ecm240": {},
    #
}
process_list_bkg = {
    # "p8_ee_ZZ_ecm240": {},
    # # "p8_ee_WW_ecm240": {},
    # "p8_ee_Zqq_ecm240": {},
    # "wzp6_ee_mumu_ecm240": {},
    # "wzp6_ee_ee_Mee_30_150_ecm240": {},
}
processList = process_list_sig | process_list_bkg
# processList=[
#     'wzp6_ee_eeH_Hbb_ecm240']

final_selec = "(zed_leptonic_flavour>0)"
final_selec += " && (zed_leptonic_m > 81 && zed_leptonic_m < 101)"
final_selec += " && (zed_leptonic_cos_theta < 0.8)"
final_selec += " && (zed_leptonic_recoil_m > 120 && zed_leptonic_recoil_m < 140)"
# require that there are 2 jets? events with <2 visible particles (such as Z(ll)Z(nn)) would not have 2 jets
# but maybe they will just fail next cut?
# final_selec     += " && (higgs_hadronic_m_2>50 && higgs_hadronic_m_2<140)"
final_selec += " && (higgs_hadronic_m>50 && higgs_hadronic_m<140)"
# apply cut, or include in NN?
final_selec += " && (etmiss < 30)"
final_selec += " && (n_extraleptons<1)"
# final_selec += " && (event_d23 >2.0 ) && (event_d34>1.5) && (event_d45>1.0)"
final_selec += " && (event_d23 >0) && (event_d34>0) && (event_d45>0)"
final_selec_nn = final_selec
final_selec = final_selec + " && ((event_d23+2.5*event_d34)<1250.)"

# NOTE: IF I ADD TIGHTER CUTS ON ETMISS OR MJJ PER CATEGORY,
# E.G. MJJ>110 GeV for cc and 115 for gg, ss
# THEY WILL DISTORT THE MRECOIL DISTRIBUTION FOR THE BKG
# SO THAT I CANNOT FIT IT ANYMORE WITH A 1ST ORDER POLY..
final_selec_g = final_selec_nn + " && (etmiss < 15)"
final_selec_c = final_selec_nn + " && (etmiss < 20)"

j1_b = "(jet1_isB > jet1_isC && jet1_isB>jet1_isU && jet1_isB > jet1_isD && jet1_isB>jet1_isS && jet1_isB>jet1_isG)"
j2_b = "(jet2_isB > jet2_isC && jet2_isB>jet2_isU && jet2_isB > jet2_isD && jet2_isB>jet2_isS && jet2_isB>jet2_isG)"
j1_c = "(jet1_isC > jet1_isB && jet1_isC>jet1_isU && jet1_isC > jet1_isD && jet1_isC>jet1_isS && jet1_isC>jet1_isG)"
j2_c = "(jet2_isC > jet2_isB && jet2_isC>jet2_isU && jet2_isC > jet2_isD && jet2_isC>jet2_isS && jet2_isC>jet2_isG)"
j1_g = "(jet1_isG > jet1_isB && jet1_isG>jet1_isC && jet1_isG>jet1_isU && jet1_isG>jet1_isD && jet1_isG>jet1_isS)"
j2_g = "(jet2_isG > jet2_isB && jet2_isG>jet2_isC && jet2_isG>jet2_isU && jet2_isG>jet2_isD && jet2_isG>jet2_isS)"
j1_s = "(jet1_isS > jet1_isB && jet1_isS>jet1_isC && jet1_isS>jet1_isU && jet1_isS>jet1_isD && jet1_isS>jet1_isG)"
j2_s = "(jet2_isS > jet2_isB && jet2_isS>jet2_isC && jet2_isS>jet2_isU && jet2_isS>jet2_isD && jet2_isS>jet2_isG)"
# j1_q = "(jet1_isQ > jet1_isB && jet1_isQ>jet1_isC && jet1_isQ>jet1_isQ && jet1_isQ>jet1_isS)"
# j2_q = "(jet2_isQ > jet2_isB && jet2_is
j1_u = "(jet1_isU > jet1_isB && jet1_isU > jet1_isC && jet1_isU > jet1_isS && jet1_isU > jet1_isG && jet1_isU > jet1_isD && jet1_isU > jet1_isTAU)"
j2_u = "(jet2_isU > jet2_isB && jet2_isU > jet2_isC && jet2_isU > jet2_isS && jet2_isU > jet2_isG && jet2_isU > jet2_isD && jet2_isU > jet2_isTAU)"
j1_d = "(jet1_isD > jet1_isB && jet1_isD > jet1_isC && jet1_isD > jet1_isS && jet1_isD > jet1_isG && jet1_isD > jet1_isU && jet1_isD > jet1_isTAU)"
j2_d = "(jet2_isD > jet2_isB && jet2_isD > jet2_isC && jet2_isD > jet2_isS && jet2_isD > jet2_isG && jet2_isD > jet2_isU && jet2_isD > jet2_isTAU)"
j1_tau = "(jet1_isTAU > jet1_isB && jet1_isTAU > jet1_isC && jet1_isTAU > jet1_isS && jet1_isTAU > jet1_isG && jet1_isTAU > jet1_isD && jet1_isTAU > jet1_isU)"
j2_tau = "(jet2_isTAU > jet2_isB && jet2_isTAU > jet2_isC && jet2_isTAU > jet2_isS && jet2_isTAU > jet2_isG && jet2_isTAU > jet2_isD && jet2_isTAU > jet2_isU)"


b2 = f"({j1_b} && {j2_b})"
b1 = f"(({j1_b} && !{j2_b}) || (!{j1_b} && {j2_b}))"
b0 = f"(!{j1_b} && !{j2_b})"

c2 = f"({j1_c} && {j2_c})"
c1 = f"(({j1_c} && !{j2_c}) || (!{j1_c} && {j2_c}))"
c0 = f"(!{j1_c} && !{j2_c})"

g2 = f"({j1_g} && {j2_g})"
g1 = f"(({j1_g} && !{j2_g}) || (!{j1_g} && {j2_g}))"
g0 = f"(!{j1_g} && !{j2_g})"

# q2 = f"({j1_q} && {j2_q})"
# q1 = f"(({j1_q} && !{j2_q}) || (!{j1_q} && {j2_q}))"
# q0 = f"(!{j1_q} && !{j2_q})"

u2 = f"({j1_u} && {j2_u})"
u1 = f"(({j1_u} && !{j2_u}) || (!{j1_u} && {j2_u}))"
u0 = f"(!{j1_u} && !{j2_u})"

d2 = f"({j1_d} && {j2_d})"
d1 = f"(({j1_d} && !{j2_d}) || (!{j1_d} && {j2_d}))"
d0 = f"(!{j1_d} && !{j2_d})"

tau2 = f"({j1_tau} && {j2_tau})"
tau1 = f"(({j1_tau} && !{j2_tau}) || (!{j1_u} && {j2_tau}))"
tau0 = f"(!{j1_tau} && !{j2_tau})"

s2 = f"({j1_s} && {j2_s})"
s1 = f"(({j1_s} && !{j2_s}) || (!{j1_s} && {j2_s}))"
s0 = f"(!{j1_s} && !{j2_s})"

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    # "finalsel": final_selec,
    # 2b (Hbb enriched)
    #    "selN_2b"     : final_selec   + " && (n_selected_btagged_jets == 2)",
    # <2b, 2c (Hcc enriched)
    #    "selN_0b2c"   : final_selec_c + " && (n_selected_ctagged_jets == 2) && (n_selected_btagged_jets == 0)",
    #    "selN_1b2c"   : final_selec_c + " && (n_selected_ctagged_jets == 2) && (n_selected_btagged_jets == 1)",
    #    "selN_2c"     : final_selec_c + " && (n_selected_ctagged_jets == 2) && (n_selected_btagged_jets < 2)",
    # 1b, < 2c (Hbb enriched)
    #    "selN_1b0c"   : final_selec   + " && (n_selected_btagged_jets == 1) && (n_selected_ctagged_jets == 0)",
    #    "selN_1b1c"   : final_selec   + " && (n_selected_ctagged_jets == 1) && (n_selected_btagged_jets == 1)",
    # 0b, 1c (Hcc enriched)
    #    "selN_0b1c"   : final_selec_c + " && (n_selected_btagged_jets == 0) && (n_selected_ctagged_jets == 1)",
    # 0b, 0c, 1 or 2g (Hgg enriched)
    #    "selN_0b0c2g" : final_selec_g + " && (n_selected_btagged_jets == 0) && (n_selected_ctagged_jets == 0) && (n_selected_gtagged_jets == 2)",
    #    "selN_0b0c1g" : final_selec_g + " && (n_selected_btagged_jets == 0) && (n_selected_ctagged_jets == 0) && (n_selected_gtagged_jets == 1)",
    # untagged (0b, 0c, 0g) (Hnonhad enriched)
    #    "selN_0b0c0g" : final_selec_g + " && (n_selected_btagged_jets == 0) && (n_selected_ctagged_jets == 0) && (n_selected_gtagged_jets == 0)",
    #
    "trainNN": final_selec_nn,
    # "selN_2b": final_selec + " && " + b2,
    # "selN_2c": final_selec + " && " + c2,
    # "selN_2g": final_selec + " && " + g2,
    # "selN_2s": final_selec + " && " + s2,
    # "selN_2q": final_selec + " && " + u2 + "&&" + d2,
    # "selN_2u": final_selec + "&&" + u2,
    # "selN_2d": final_selec + "&&" + d2,
    # "selN_2tau": final_selec + "&&" + tau2,
    # "selN_1b": final_selec + " && " + b1,
    # "selN_1g": final_selec + " && " + g1 + " && " + b0,
    # "selN_1c": final_selec + " && " + c1 + " && " + b0 + " && " + g0,
    # "selN_1s": final_selec + " && " + s1 + " && " + b0 + " && " + c0 + " && " + g0,
}

###Dictionary of the list of cuts for hists only. The key is the name of the selection that will be added to the output file.
###Empty: no hists
cut_list_histOnly = {}
cut_list_histOnly["Nosel"] = "0<1"
cut_list_histOnly["selN_Z"] = (
    cut_list_histOnly["Nosel"] + " && (zed_leptonic_flavour>0)"
)
cut_list_histOnly["selN_mZ"] = (
    cut_list_histOnly["selN_Z"] + " && (zed_leptonic_m > 81 && zed_leptonic_m < 101)"
)
cut_list_histOnly["selN_cos"] = (
    cut_list_histOnly["selN_mZ"] + " && (zed_leptonic_cos_theta < 0.8)"
)
cut_list_histOnly["selN_H"] = (
    cut_list_histOnly["selN_cos"]
    + " && (zed_leptonic_recoil_m > 120 && zed_leptonic_recoil_m<140)"
)
# cut_list_histOnly["selN_mhad"] = (
#     cut_list_histOnly["selN_H"]
#     + " && (higgs_hadronic_m > 100 && higgs_hadronic_m < 140)"
# )
# cut_list_histOnly["selN_mhad"  ] = cut_list_histOnly["selN_H"   ] + " && (higgs_hadronic_m_2 > 100 && higgs_hadronic_m_2 < 140)"
cut_list_histOnly["selN_miss"] = cut_list_histOnly["selN_H"] + " && (etmiss < 30)"
cut_list_histOnly["selN_lepveto"] = (
    cut_list_histOnly["selN_miss"] + " && (n_extraleptons<1)"
)
cut_list_histOnly["selN_nn"] = final_selec_nn
cut_list_histOnly["selN_e"] = final_selec_nn + " && zed_leptonic_flavour==1"
cut_list_histOnly["selN_mu"] = final_selec_nn + " && zed_leptonic_flavour==2"
cut_list_histOnly["finalsel_e"] = final_selec + " && zed_leptonic_flavour==1"
cut_list_histOnly["finalsel_mu"] = final_selec + " && zed_leptonic_flavour==2"

if do_histOnly:
    cutList = cutList | cut_list_histOnly


histoList = {}
# Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
if doNN:
    histoList = {
        # "n_btags":{"name":"n_selected_btagged_jets","title":"N_{b-tags}","bin":3,"xmin":-0.5,"xmax":2.5},
        # "n_ctags":{"name":"n_selected_ctagged_jets","title":"N_{c-tags}","bin":3,"xmin":-0.5,"xmax":2.5},
        # "n_gtags":{"name":"n_selected_gtagged_jets","title":"N_{g-tags}","bin":3,"xmin":-0.5,"xmax":2.5},
        "jet1_isB": {
            "name": "jet1_isB",
            "title": "isB(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isC": {
            "name": "jet1_isC",
            "title": "isC(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isG": {
            "name": "jet1_isG",
            "title": "isG(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isS": {
            "name": "jet1_isS",
            "title": "isS(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isU": {
            "name": "jet1_isU",
            "title": "isU(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isD": {
            "name": "jet1_isD",
            "title": "isD(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isTAU": {
            "name": "jet1_isTAU",
            "title": "isTAU(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isB": {
            "name": "jet2_isB",
            "title": "isB(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isC": {
            "name": "jet2_isC",
            "title": "isC(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isG": {
            "name": "jet2_isG",
            "title": "isG(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isS": {
            "name": "jet2_isS",
            "title": "isS(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isU": {
            "name": "jet2_isU",
            "title": "isU(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isD": {
            "name": "jet2_isD",
            "title": "isD(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isTAU": {
            "name": "jet2_isTAU",
            "title": "isTAU(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jets_d23": {
            "name": "event_d23",
            "title": "d_{23}",
            "bin": 50,
            "xmin": 0,
            "xmax": 2000.0,
        },
        "jets_d34": {
            "name": "event_d34",
            "title": "d_{34}",
            "bin": 50,
            "xmin": 0,
            "xmax": 1000.0,
        },
        "jets_d45": {
            "name": "event_d45",
            "title": "d_{45}",
            "bin": 50,
            "xmin": 0,
            "xmax": 500.0,
        },
        "N_extraleptons": {
            "name": "n_extraleptons",
            "title": "N(l^{highE,extra})",
            "bin": 5,
            "xmin": -0.5,
            "xmax": 4.5,
        },
        "hadronic_mass": {
            "name": "higgs_hadronic_m",
            "title": "m_{jets} [GeV]",
            "bin": 80,
            "xmin": 50,
            "xmax": 140,
        },
        "missing_e": {
            "name": "etmiss",
            "title": "E_{miss} [GeV]",
            "bin": 60,
            "xmin": 0,
            "xmax": 30,
        },
        "zed_flavour": {
            "name": "zed_leptonic_flavour",
            "title": "Z flavour",
            "bin": 3,
            "xmin": -0.5,
            "xmax": 2.5,
        },
        "m_recoil": {
            "name": "zed_leptonic_recoil_m",
            "title": "m_{recoil} [GeV]",
            "bin": 80,
            "xmin": 120,
            "xmax": 140,
        },
        
        #test Alexis
        "extraleptons_p": {
            "name": "extraleptons_p",
            "title": "p(l^{iso,extra}) [GeV]",
            "bin": 70,
            "xmin": 0,
            "xmax": 140,
        },
        "all_jets_p": {
            "name": "jet_p",
            "title": "E^{j} [GeV]",
            "bin": 70,
            "xmin": 0,
            "xmax": 140,
        },
        "jets_p": {
            "name": "selected_jets_p",
            "title": "p^{j} [GeV]",
            "bin": 70,
            "xmin": 0,
            "xmax": 140,
        },
        "N_jets": {
            "name": "n_selected_jets",
            "title": "N_{jets}",
            "bin": 10,
            "xmin": -0.5,
            "xmax": 9.5,
        },
        "m_jets": {
            "name": "selected_jets_m",
            "title": "m_{jets}",
            "bin": 100,
            "xmin": -0,
            "xmax": 200,
        },
        "p_Higgs": {
            "name": "higgs_hadronic_p",
            "title": "p_{Higgs}",
            "bin": 100,
            "xmin": -0,
            "xmax": 200,
        },
        "p_Higgs_2": {
            "name": "higgs_hadronic_p_2",
            "title": "p_{Higgs}_2",
            "bin": 100,
            "xmin": -0,
            "xmax": 200,
        },
        # "N_btag_jets":{"name":"n_selected_btagged_jets","title":"N_{b-jets}","bin":5,"xmin":-0.5,"xmax":4.5},
        # "N_ctag_jets":{"name":"n_selected_ctagged_jets","title":"N_{c-jets}","bin":5,"xmin":-0.5,"xmax":4.5},
        # "N_gtag_jets":{"name":"n_selected_gtagged_jets","title":"N_{g-jets}","bin":5,"xmin":-0.5,"xmax":4.5},
        "cos_theta_Z": {
            "name": "zed_leptonic_cos_theta",
            "title": "|cos#theta_{ll}|",
            "bin": 20,
            "xmin": 0,
            "xmax": 1,
        },
        "zed_leptonic_phi": {
            "name": "zed_leptonic_phi",
            "title": "\phi_{ll}",
            "bin": 360,
            "xmin": -180,
            "xmax": 180,
        },
        "dilepton_mass": {
            "name": "zed_leptonic_m",
            "title": "m_{ll} [GeV]",
            "bin": 110,
            "xmin": 0,
            "xmax": 220,
        },
        "dilepton_mass_2": {
            "name": "zed_leptonic_m",
            "title": "m_{ll} [GeV]",
            "bin": 80,
            "xmin": 70,
            "xmax": 110,
        },
        "dilepton_charge": {
            "name": "zed_leptonic_charge",
            "title": "q_{ll}",
            "bin": 5,
            "xmin": -2.5,
            "xmax": 2.5,
        },
        "hadronic_mass": {
            "name": "higgs_hadronic_m",
            "title": "m_{jets} [GeV]",
            "bin": 110,
            "xmin": 0,
            "xmax": 220,
        },
        "hadronic_mass_2": {
            "name": "higgs_hadronic_m_2",
            "title": "m_{jets} [GeV]",
            "bin": 110,
            "xmin": 0,
            "xmax": 220,
        },
        "hadronic_mass_zoom": {
            "name": "higgs_hadronic_m",
            "title": "m_{jets} [GeV]",
            "bin": 100,
            "xmin": 50,
            "xmax": 150,
        },
    }

else:
    histoList = {
        "zed_flavour": {
            "name": "zed_leptonic_flavour",
            "title": "Z flavour",
            "bin": 3,
            "xmin": -0.5,
            "xmax": 2.5,
        },
        "all_leptons_p": {
            "name": "leptons_p",
            "title": "p(l^{rec}) [GeV]",
            "bin": 48,
            "xmin": 0,
            "xmax": 120,
        },
        "zed_leptons_p": {
            "name": "zed_leptons_p",
            "title": "p(l^{sel}) [GeV]",
            "bin": 70,
            "xmin": 0,
            "xmax": 140,
        },
        "extraleptons_p": {
            "name": "extraleptons_p",
            "title": "p(l^{iso,extra}) [GeV]",
            "bin": 70,
            "xmin": 0,
            "xmax": 140,
        },
        "N_extra_leptons": {
            "name": "n_extraleptons",
            "title": "N(l^{extra})",
            "bin": 5,
            "xmin": -0.5,
            "xmax": 4.5,
        },
        "all_jets_p": {
            "name": "jet_p",
            "title": "E^{j} [GeV]",
            "bin": 70,
            "xmin": 0,
            "xmax": 140,
        },
        "jets_p": {
            "name": "selected_jets_p",
            "title": "p^{j} [GeV]",
            "bin": 70,
            "xmin": 0,
            "xmax": 140,
        },
        "N_jets": {
            "name": "n_selected_jets",
            "title": "N_{jets}",
            "bin": 10,
            "xmin": -0.5,
            "xmax": 9.5,
        },
        # "N_btag_jets":{"name":"n_selected_btagged_jets","title":"N_{b-jets}","bin":5,"xmin":-0.5,"xmax":4.5},
        # "N_ctag_jets":{"name":"n_selected_ctagged_jets","title":"N_{c-jets}","bin":5,"xmin":-0.5,"xmax":4.5},
        # "N_gtag_jets":{"name":"n_selected_gtagged_jets","title":"N_{g-jets}","bin":5,"xmin":-0.5,"xmax":4.5},
        "cos_theta_Z": {
            "name": "zed_leptonic_cos_theta",
            "title": "|cos#theta_{ll}|",
            "bin": 20,
            "xmin": 0,
            "xmax": 1,
        },
        "missing_e": {
            "name": "etmiss",
            "title": "E_{miss} [GeV]",
            "bin": 60,
            "xmin": 0,
            "xmax": 60,
        },
        "dilepton_mass": {
            "name": "zed_leptonic_m",
            "title": "m_{ll} [GeV]",
            "bin": 110,
            "xmin": 0,
            "xmax": 220,
        },
        "dilepton_mass_2": {
            "name": "zed_leptonic_m",
            "title": "m_{ll} [GeV]",
            "bin": 80,
            "xmin": 70,
            "xmax": 110,
        },
        "dilepton_charge": {
            "name": "zed_leptonic_charge",
            "title": "q_{ll}",
            "bin": 5,
            "xmin": -2.5,
            "xmax": 2.5,
        },
        "hadronic_mass": {
            "name": "higgs_hadronic_m",
            "title": "m_{jets} [GeV]",
            "bin": 110,
            "xmin": 0,
            "xmax": 220,
        },
        "hadronic_mass_2": {
            "name": "higgs_hadronic_m_2",
            "title": "m_{jets} [GeV]",
            "bin": 110,
            "xmin": 0,
            "xmax": 220,
        },
        "hadronic_mass_zoom": {
            "name": "higgs_hadronic_m",
            "title": "m_{jets} [GeV]",
            "bin": 100,
            "xmin": 50,
            "xmax": 150,
        },
        "m_recoil": {
            "name": "zed_leptonic_recoil_m",
            "title": "m_{recoil} [GeV]",
            "bin": 80,
            "xmin": 120,
            "xmax": 140,
        },
        "m_recoil_2": {
            "name": "zed_leptonic_recoil_m",
            "title": "m_{recoil} [GeV]",
            "bin": 90,
            "xmin": 70,
            "xmax": 160,
        },
        "jets_d23": {
            "name": "event_d23",
            "title": "d_{23}",
            "bin": 50,
            "xmin": 0,
            "xmax": 2000.0,
        },
        "jets_d34": {
            "name": "event_d34",
            "title": "d_{34}",
            "bin": 50,
            "xmin": 0,
            "xmax": 1000.0,
        },
        "jets_d45": {
            "name": "event_d45",
            "title": "d_{45}",
            "bin": 50,
            "xmin": 0,
            "xmax": 500.0,
        },
    }
    
    
    
    # mumuHTAUTAU
    #        All events                   : 400000
    #    After selection trainNN      : 382
    #    After selection Nosel        : 400000
    #    After selection selN_Z       : 367972
    #    After selection selN_mZ      : 338400
    #    After selection selN_cos     : 275281
    #    After selection selN_H       : 263262
    #    After selection selN_miss    : 130659
    #    After selection selN_lepveto : 92306
    #    After selection selN_nn      : 382
    #    After selection selN_e       : 0
    #    After selection selN_mu      : 382
    #    After selection finalsel_e   : 0
    #    After selection finalsel_mu  : 371
