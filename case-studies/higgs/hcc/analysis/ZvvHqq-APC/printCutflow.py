# import common definitions
import os, sys
configdir = os.getenv('FCCANACONFS')
sys.path.append(configdir)
from analysis_config import *

import subprocess
import math

from ROOT import TFile, TTree

debug = False

# In the tables, split ZHnonhad into WW/ZZ/tautau or not
splitZHother = True

# print significance or efficiency
printSig = False

processes = {
    'vvHbb'      : ['wzp6_ee_nunuH_Hbb_ecm240'],
    'vvHcc'      : ['wzp6_ee_nunuH_Hcc_ecm240'],
    'vvHgg'      : ['wzp6_ee_nunuH_Hgg_ecm240'],
    'vvHss'      : ['wzp6_ee_nunuH_Hss_ecm240'],
    }
if splitZHother:
    processes.update({
        'vvHWW'    : ['wzp6_ee_nunuH_HWW_ecm240'],
        'vvHZZ'    : ['wzp6_ee_nunuH_HZZ_ecm240'],
        'vvHtautau': ['wzp6_ee_nunuH_Htautau_ecm240']
    })
else:
    processes.update({
        'vvHnonhad': ['wzp6_ee_nunuH_Htautau_ecm240',
                      'wzp6_ee_nunuH_HWW_ecm240',
                      'wzp6_ee_nunuH_HZZ_ecm240']
    })
processes.update({
    'qqH'       : ['wzp6_ee_qqH_Hbb_ecm240',
                                   'wzp6_ee_qqH_Hcc_ecm240',
                                   'wzp6_ee_qqH_Hss_ecm240',
                                   'wzp6_ee_qqH_Hgg_ecm240',
                   'wzp6_ee_qqH_Htautau_ecm240',
                                   'wzp6_ee_qqH_HWW_ecm240',
                                   'wzp6_ee_qqH_HZZ_ecm240',
                   'wzp6_ee_ssH_Hbb_ecm240',
                                   'wzp6_ee_ssH_Hcc_ecm240',
                                   'wzp6_ee_ssH_Hss_ecm240',
                                   'wzp6_ee_ssH_Hgg_ecm240',
                   'wzp6_ee_ssH_Htautau_ecm240',
                                   'wzp6_ee_ssH_HWW_ecm240',
                                   'wzp6_ee_ssH_HZZ_ecm240',
                   'wzp6_ee_ccH_Hbb_ecm240',
                                   'wzp6_ee_ccH_Hcc_ecm240',
                                   'wzp6_ee_ccH_Hss_ecm240',
                                   'wzp6_ee_ccH_Hgg_ecm240',
                   'wzp6_ee_ccH_Htautau_ecm240',
                                   'wzp6_ee_ccH_HWW_ecm240',
                                   'wzp6_ee_ccH_HZZ_ecm240',
                   'wzp6_ee_bbH_Hbb_ecm240',
                                   'wzp6_ee_bbH_Hcc_ecm240',
                                   'wzp6_ee_bbH_Hss_ecm240',
                                   'wzp6_ee_bbH_Hgg_ecm240',
                   'wzp6_ee_bbH_Htautau_ecm240',
                                   'wzp6_ee_bbH_HWW_ecm240',
                                   'wzp6_ee_bbH_HZZ_ecm240'],
    'nuenueZ'   : ['wzp6_ee_nuenueZ_ecm240'],
    'Zqq'       : ['p8_ee_Zqq_ecm240'],
    'WW'        : ['p8_ee_WW_ecm240'],
    'ZZ'        : ['p8_ee_ZZ_ecm240']
})

cutList = {}
#for cut in cutList_histOnly:
#    cutList[cut] = cutDict[cut]['label']
for cut in sel:
    cutList[cut] = cutDict[cut]['label']
cutList['finalsel'] = 'All cuts'


# directory containing the cutflow files
basedir += 'analysis-final/hists/'

def getHadFraction(decay):
    fileName = basedir.replace("hists", "trees") + ("wzp6_ee_nunuH_H%s_ecm240_finalsel.root" % decay)
    f = TFile.Open(fileName, "READ")
    events = f.Get("events")
    decayId = 0
    if decay=="WW":
        decayId = 51
    elif decay=="ZZ":
        decayId = 40
    elif decay=="tautau":
        decayId = 10
    fraction = events.GetEntries("MC_HiggsDecay==%d" % decayId)*1./events.GetEntries()
    f.Close()
    return fraction

yieldsInitial = {}
yieldsFinal = {}
yieldsPrevious = {}

# print title of table
print('')
if printSig:
    print('{:30s} '.format('Cut'), end='')
    for proc in processes:
        if 'vvH' in proc:
            print('{:>10s} {:>5s} '.format(proc, ''), end='')
        else:
            print('{:>10s} '.format(proc), end='')
    print('')
    print('{:30s} '.format(''), end='')
    for proc in processes:
        if 'vvH' in proc:
            print('{:>10s} {:>5s} '.format('Yield', 'Sig'), end='')
        else:
            print('{:>10s} '.format('Yield'), end='')
    print('')              
else:
    print('{:30s} '.format('Cut'), end='')
    for proc in processes:
        print('{:>10s} {:>5s} '.format(proc, ''), end='')
    print('')
    print('{:30s} '.format(''), end='')
    for proc in processes:
        print('{:>10s} {:>5s} '.format('Yield', 'Eff'), end='')
    print('')               

# loop over the cuts and populate table rows
for cut in cutList:
    if debug: print(cut)
    yields = {}
    sumYields = 0.0
    for proc in processes:
        yields[proc] = 0.
        for subproc in processes[proc]:
            filename = basedir+'/'+subproc+'_cutflow_weighted.txt'
            if os.path.isfile(filename):
                cmd = "grep \ " + cut + "\  " + basedir + "/"+subproc+"_cutflow_weighted.txt | awk '{print $5}'"
                if debug: print(cmd)
                subproc_return = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode()
                if debug: print(subproc_return)
                yields[proc] += float(subproc_return.split('\n')[-2])
        else:
            yields[proc] += 0.0
        sumYields += yields[proc]
    if (cut=='selNone'): yieldsInitial=dict(yields)
    if (cut=='finalsel'): yieldsFinal=dict(yields)
    print('{:30s} '.format(cutList[cut]), end='')
    if printSig:
        sig = {}
        for proc in processes:
            if 'vvH' in proc:
                sig[proc] = yields[proc]/math.sqrt(sumYields)
                print('{:10.0f} {:5.0f} '.format(yields[proc],sig[proc]), end='')
            else:
                print('{:10.0f} '.format(yields[proc]), end='')
        print('')
    else:
        eff = {}        
        if cut!='selNone':
            for proc in processes:
                eff[proc] = 100.*yields[proc]/yieldsPrevious[proc]
                print('{:10.0f} {:5.0f} '.format(yields[proc], eff[proc]), end='')
        else:
            for proc in processes:
                print('{:10.0f} {:>5s} '.format(yields[proc], '-'), end= '')
        print('')
        yieldsPrevious = dict(yields)  
print('\n')

str = '{:30s}'.format('Efficiency (%)')
for proc in processes: str+='{:>10s}'.format(proc)
print(str)
str = '{:30s}'.format('')
for proc in processes:
    if (yieldsInitial[proc]!=0.):
        str+='{:10.2f}'.format(yieldsFinal[proc]*100./yieldsInitial[proc])
    else:
        str+='{:10s}'.format('')
print(str)
print('')


# Print efficiency for HWW/ZZ/tautau normalised taking into account hadronic BRs
# Not correct because some events pass selection even if they are not fully had
# For instance Z(nunu)Z(qq)
if splitZHother:
    BRhad = {
        'WW': 0.454,
        'ZZ': 0.489,
        'tautau': 0.42
    }
    # calculated from nunuH_HWW/ZZ/tautau after finalsel
    fracHad = {
        'WW': getHadFraction("WW"),
        'ZZ': getHadFraction("ZZ"),
        'tautau': getHadFraction("tautau"),
        }
    str = '{:50s}'.format('Eff. in ZH(other) channels wrt had decays (%)')
    for decay in BRhad:
        str+='{:>10s}'.format(decay)
    print(str)
    str = '{:50s}'.format('')
    for decay in BRhad:
        str+='{:10.2f}'.format(yieldsFinal['vvH'+decay]*100./yieldsInitial['vvH'+decay]*fracHad[decay]/BRhad[decay])  
    print(str)
    print('')

