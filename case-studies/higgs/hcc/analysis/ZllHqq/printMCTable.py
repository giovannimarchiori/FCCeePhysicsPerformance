#!/usr/bin/env python
import json
import os

procDict = 'FCCee_procDict_winter2023_IDEA.json'
lumiRef = 5e3 # fb-1
outFile = 'samples_winter2023.tex'

processSamples = {
    'vvHbb'      : 'wzp6_ee_nunuH_Hbb_ecm240',
    'vvHcc'      : 'wzp6_ee_nunuH_Hcc_ecm240',
    'vvHss'      : 'wzp6_ee_nunuH_Hss_ecm240',
    'vvHgg'      : 'wzp6_ee_nunuH_Hgg_ecm240', 
    'vvHtautau'  : 'wzp6_ee_nunuH_Htautau_ecm240',
    'vvHWW'      : 'wzp6_ee_nunuH_HWW_ecm240',
    'vvHZZ'      : 'wzp6_ee_nunuH_HZZ_ecm240',
    'vvHuu'      : 'wzp6_ee_nunuH_Huu_ecm240',
    'vvHdd'      : 'wzp6_ee_nunuH_Hdd_ecm240',
    'vvHbd'      : 'wzp6_ee_nunuH_Hbd_ecm240',
    'vvHbs'      : 'wzp6_ee_nunuH_Hbs_ecm240',
    'vvHsd'      : 'wzp6_ee_nunuH_Hsd_ecm240',
    'vvHcu'      : 'wzp6_ee_nunuH_Hcu_ecm240',
    'eeHbb'      : 'wzp6_ee_eeH_Hbb_ecm240',
    'eeHcc'      : 'wzp6_ee_eeH_Hcc_ecm240',
    'eeHss'      : 'wzp6_ee_eeH_Hss_ecm240',
    'eeHgg'      : 'wzp6_ee_eeH_Hgg_ecm240', 
    'eeHtautau'  : 'wzp6_ee_eeH_Htautau_ecm240',
    'eeHWW'      : 'wzp6_ee_eeH_HWW_ecm240',
    'eeHZZ'      : 'wzp6_ee_eeH_HZZ_ecm240',
    'eeHuu'      : 'wzp6_ee_eeH_Huu_ecm240',
    'eeHdd'      : 'wzp6_ee_eeH_Hdd_ecm240',
    'eeHbd'      : 'wzp6_ee_eeH_Hbd_ecm240',
    'eeHbs'      : 'wzp6_ee_eeH_Hbs_ecm240',
    'eeHsd'      : 'wzp6_ee_eeH_Hsd_ecm240',
    'eeHcu'      : 'wzp6_ee_eeH_Hcu_ecm240',
    'mumuHbb'    : 'wzp6_ee_mumuH_Hbb_ecm240',
    'mumuHcc'    : 'wzp6_ee_mumuH_Hcc_ecm240',
    'mumuHss'    : 'wzp6_ee_mumuH_Hss_ecm240',
    'mumuHgg'    : 'wzp6_ee_mumuH_Hgg_ecm240', 
    'mumuHtautau': 'wzp6_ee_mumuH_Htautau_ecm240',
    'mumuHWW'    : 'wzp6_ee_mumuH_HWW_ecm240',
    'mumuHZZ'    : 'wzp6_ee_mumuH_HZZ_ecm240',
    'mumuHuu'    : 'wzp6_ee_mumuH_Huu_ecm240',
    'mumuHdd'    : 'wzp6_ee_mumuH_Hdd_ecm240',
    'mumuHbd'    : 'wzp6_ee_mumuH_Hbd_ecm240',
    'mumuHbs'    : 'wzp6_ee_mumuH_Hbs_ecm240',
    'mumuHsd'    : 'wzp6_ee_mumuH_Hsd_ecm240',
    'mumuHcu'    : 'wzp6_ee_mumuH_Hcu_ecm240',
    'qqHbb'      : 'wzp6_ee_qqH_Hbb_ecm240',
    'qqHcc'      : 'wzp6_ee_qqH_Hcc_ecm240',
    'qqHss'      : 'wzp6_ee_qqH_Hss_ecm240',
    'qqHgg'      : 'wzp6_ee_qqH_Hgg_ecm240',
    'qqHtautau'  : 'wzp6_ee_qqH_Htautau_ecm240',
    'qqHWW'      : 'wzp6_ee_qqH_HWW_ecm240',
    'qqHZZ'      : 'wzp6_ee_qqH_HZZ_ecm240',
    'ssHbb'      : 'wzp6_ee_ssH_Hbb_ecm240',
    'ssHcc'      : 'wzp6_ee_ssH_Hcc_ecm240',
    'ssHss'      : 'wzp6_ee_ssH_Hss_ecm240',
    'ssHgg'      : 'wzp6_ee_ssH_Hgg_ecm240',
    'ssHtautau'  : 'wzp6_ee_ssH_Htautau_ecm240',
    'ssHWW'      : 'wzp6_ee_ssH_HWW_ecm240',
    'ssHZZ'      : 'wzp6_ee_ssH_HZZ_ecm240',
    'ccHbb'      : 'wzp6_ee_ccH_Hbb_ecm240',
    'ccHcc'      : 'wzp6_ee_ccH_Hcc_ecm240',
    'ccHss'      : 'wzp6_ee_ccH_Hss_ecm240',
    'ccHgg'      : 'wzp6_ee_ccH_Hgg_ecm240',
    'ccHtautau'  : 'wzp6_ee_ccH_Htautau_ecm240',
    'ccHWW'      : 'wzp6_ee_ccH_HWW_ecm240',
    'ccHZZ'      : 'wzp6_ee_ccH_HZZ_ecm240',
    'bbHbb'      : 'wzp6_ee_bbH_Hbb_ecm240',
    'bbHcc'      : 'wzp6_ee_bbH_Hcc_ecm240',
    'bbHss'      : 'wzp6_ee_bbH_Hss_ecm240',
    'bbHgg'      : 'wzp6_ee_bbH_Hgg_ecm240',
    'bbHtautau'  : 'wzp6_ee_bbH_Htautau_ecm240',
    'bbHWW'      : 'wzp6_ee_bbH_HWW_ecm240',
    'bbHZZ'      : 'wzp6_ee_bbH_HZZ_ecm240',
    'nuenueZ'    : 'wzp6_ee_nuenueZ_ecm240',
    'WW'         : 'p8_ee_WW_ecm240',
    'ZZ'         : 'p8_ee_ZZ_ecm240',
    'Zqq'        : 'p8_ee_Zqq_ecm240',
    'Zee'        : 'wzp6_ee_ee_Mee_30_150_ecm240',
    'Zmumu'      : 'wzp6_ee_mumu_ecm240',
}

processLabels = {
    'vvHbb'      : '$\\nunuh (\\bb)$',
    'vvHcc'      : '$\\nunuh (\\cc)$',
    'vvHss'      : '$\\nunuh (\\ssbar)$',
    'vvHgg'      : '$\\nunuh (gg)$',
    'vvHtautau'  : '$\\nunuh (\\tautau)$',
    'vvHWW'      : '$\\nunuh (\\ww)$',
    'vvHZZ'      : '$\\nunuh (\\zz)$',
    'vvHuu'      : '$\\nunuh (\\uu)$',
    'vvHdd'      : '$\\nunuh (\\dd)$',
    'vvHbs'      : '$\\nunuh (\\bs)$',
    'vvHbd'      : '$\\nunuh (\\bd)$',
    'vvHsd'      : '$\\nunuh (\\sd)$',
    'vvHcu'      : '$\\nunuh (\\cu)$',
    'eeHbb'      : '$\\eeh (\\bb)$',
    'eeHcc'      : '$\\eeh (\\cc)$',
    'eeHss'      : '$\\eeh (\\ssbar)$',
    'eeHgg'      : '$\\eeh (gg)$',
    'eeHtautau'  : '$\\eeh (\\tautau)$',
    'eeHWW'      : '$\\eeh (\\ww)$',
    'eeHZZ'      : '$\\eeh (\\zz)$',
    'eeHuu'      : '$\\eeh (\\uu)$',
    'eeHdd'      : '$\\eeh (\\dd)$',
    'eeHbs'      : '$\\eeh (\\bs)$',
    'eeHbd'      : '$\\eeh (\\bd)$',
    'eeHsd'      : '$\\eeh (\\sd)$',
    'eeHcu'      : '$\\eeh (\\cu)$',
    'mumuHbb'    : '$\\mumuh (\\bb)$',
    'mumuHcc'    : '$\\mumuh (\\cc)$',
    'mumuHss'    : '$\\mumuh (\\ssbar)$',
    'mumuHgg'    : '$\\mumuh (gg)$',
    'mumuHtautau': '$\\mumuh (\\tautau)$',
    'mumuHWW'    : '$\\mumuh (\\ww)$',
    'mumuHZZ'    : '$\\mumuh (\\zz)$',
    'mumuHuu'    : '$\\mumuh (\\uu)$',
    'mumuHdd'    : '$\\mumuh (\\dd)$',
    'mumuHbs'    : '$\\mumuh (\\bs)$',
    'mumuHbd'    : '$\\mumuh (\\bd)$',
    'mumuHsd'    : '$\\mumuh (\\sd)$',
    'mumuHcu'    : '$\\mumuh (\\cu)$',
    'qqHbb'      : '$\\qqh (\\bb)$',
    'qqHcc'      : '$\\qqh (\\cc)$',
    'qqHss'      : '$\\qqh (\\ssbar)$',
    'qqHgg'      : '$\\qqh (gg)$',
    'qqHtautau'  : '$\\qqh (\\tautau)$',
    'qqHWW'      : '$\\qqh (\\ww)$',
    'qqHZZ'      : '$\\qqh (\\zz)$',
    'ssHbb'      : '$\\ssh (\\bb)$',
    'ssHcc'      : '$\\ssh (\\cc)$',
    'ssHss'      : '$\\ssh (\\ssbar)$',
    'ssHgg'      : '$\\ssh (gg)$',
    'ssHtautau'  : '$\\ssh (\\tautau)$',
    'ssHWW'      : '$\\ssh (\\ww)$',
    'ssHZZ'      : '$\\ssh (\\zz)$',
    'ccHbb'      : '$\\cch (\\bb)$',
    'ccHcc'      : '$\\cch (\\cc)$',
    'ccHss'      : '$\\cch (\\ssbar)$',
    'ccHgg'      : '$\\cch (gg)$',
    'ccHtautau'  : '$\\cch (\\tautau)$',
    'ccHWW'      : '$\\cch (\\ww)$',
    'ccHZZ'      : '$\\cch (\\zz)$',
    'bbHbb'      : '$\\bbh (\\bb)$',
    'bbHcc'      : '$\\bbh (\\cc)$',
    'bbHss'      : '$\\bbh (\\ssbar)$',
    'bbHgg'      : '$\\bbh (gg)$',
    'bbHtautau'  : '$\\bbh (\\tautau)$',
    'bbHWW'      : '$\\bbh (\\ww)$',
    'bbHZZ'      : '$\\bbh (\\zz)$',
    'nuenueZ'    : '$\\nunuz$',
    'WW'         : '\\ww',
    'ZZ'         : '\\zz',
    'Zqq'        : '\\zqq',
    'Zee'        : '\\zee',
    'Zmumu'      : '\\zmumu',
}

dictFound=False
if os.path.isfile('./' + procDict):
    procDict = './' + procDict
    dictFound=True
else:
    print('Dictionary not found in local directory, trying alternative folders: ')
    procFolders = os.getenv('FCCDICTSDIR').split(':')
    if len(procFolders) == 0:
        folder = '/cvmfs/fcc.cern.ch/FCCDicts'
        print(folder)
        if os.path.isfile(folder + '/' + procDict):
            procDict = folder + '/' + procDict
            dictFound = True
    else:
        for folder in procFolders:
            print(folder)
            if os.path.isfile(folder + '/' + procDict):
                procDict = folder + '/' + procDict
                dictFound = True
                break
if not dictFound:
    print('Dictionary not found, exiting')
    exit(1)

print('Using dictionary: ', procDict)
print('Using a reference luminosity of %f fb' % lumiRef)
print('The output will also be saved to latex file ', outFile)

f = open(procDict, 'r') 
procDict = json.load(f)

print('{:15s} {:>15s} {:>10s} {:>15s} {:>15s}'.format('Process', 'sigma [fb]', 'Ngen', 'Lgen [/fb]', 'Lgen/L'))
outf = open(outFile, 'w')
outf.write('\\begin{table}[!htbp]\n')
outf.write('\\centering\n')
outf.write('\\caption{For each simulated signal and background process, the theoretical\n')
outf.write('cross-section $\\sigma$, the number of generated events $N_\\mathrm{gen}$,\n')
outf.write('the equivalent luminosity $L_\\mathrm{gen} = N_\\mathrm{gen}/\\sigma$ and\n')
outf.write('its ratio to the nominal luminosity $L=5$~ab$^{-1}$.}\n') 
outf.write('\\label{tab:samples}\n')
outf.write('\\begin{tabular}{llrrr}\n')
outf.write('\\toprule\n')
outf.write('{:20s} & {:>15s} & {:>15s} & {:>15s} & {:>15s} \\\\\n'.format('Process', '$\\sigma$ [fb]', '$N_\\mathrm{gen}$', '$L_\\mathrm{gen}$ [fb$^{-1}$]', '$L_\\mathrm{gen}/L$'))
outf.write('\\midrule\n')

for proc in processSamples:
    pr = processSamples[proc]
    if (pr=='wzp6_ee_eeH_Huu_ecm240' or
        pr=='wzp6_ee_eeH_Hdd_ecm240' or
        pr=='wzp6_ee_mumuH_Huu_ecm240' or
        pr=='wzp6_ee_mumuH_Hdd_ecm240'):
        print('Skipping sample', pr)
        print('Please check if they have been produced recently and in that case remove this part of the code')
        continue

    xsection = 1e3*procDict[pr]["crossSection"]*procDict[pr]["kfactor"]*procDict[pr]["matchingEfficiency"]
    events = procDict[pr]["sumOfWeights"]
    lumi = events/xsection
    lumiratio = lumi/lumiRef
    print('{:15s} {:15.9f} {:10.0f} {:15.0f} {:15.3f}'.format(proc, xsection, events, lumi, lumiratio))
    outf.write('{:20s} & {:15.9f} & {:15.0f} & {:15.0f} & {:15.3f} \\\\\n'.format(processLabels[proc], xsection, events, lumi, lumiratio))
outf.write('\\bottomrule\n')
outf.write('\\end{tabular}\n')
outf.write('\\end{table}\n')
