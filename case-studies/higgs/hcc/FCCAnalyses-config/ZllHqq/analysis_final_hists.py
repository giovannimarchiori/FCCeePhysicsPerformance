import os, sys

# import common definitions
configdir = os.getenv('FCCANACONFS')
sys.path.append(configdir)
from analysis_final_common import *

# produces ROOT TTrees, default is False
doTree = False
saveTabular = True

cutList = cutList_histOnly

# Dictionary for the ouput variable/hitograms.
# The key is the name of the variable in the output files.
# "name" is the name of the variable in the input file
# "title" is the x-axis label of the histogram
# "bin" the number of bins of the histogram
# "xmin" the minimum x-axis value
# "xmax" the maximum x-axis value.
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
