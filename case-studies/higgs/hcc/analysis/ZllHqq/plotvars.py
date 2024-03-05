# do plots of histograms produced by fccanalysis final

# import common definitions
import os, sys
configdir = os.getenv('FCCANACONFS')
sys.path.append(configdir)
from analysis_config import *

# import ROOT and other libraries
import ROOT
from ROOT import kRed, kPink, kOrange, kCyan, kBlue, kGreen, kViolet, kBlack
from ROOT import kDashed, gPad
from ROOT import TCanvas, THStack, TLegend, TFile, TLine, TH1D
import math


signalOnly = False
splitZHother = True


def plotvars():

    from analysis_config import basedir
    # basedir = analysis_config.basedir
    print(basedir)
    
    # vars: varname, preselection, cutmin, cutmax, axis title, legend position, plot type
    vars = [
        # momentum of all leptons (selNone)
        ('all_leptons_p', 'selNone', 25., 80., 'p(l_{rec}) [GeV]', 0.7, 'lin'),
        
        # type or reconstructed Z candidate (0=none, 1=Zee, 2=Zmm) (selNone)
        ('zed_flavour',   'selNone', 0.5,    -9999., 'Z type', 0.7, 'lin'),
        
        # momentum of Z leptons (selN_Z)
        ('zed_leptons_p', 'selN_Z', 9999., -9999., 'p(l_{Z}) [GeV]', 0.7, 'lin'),
        
        # zed candidate mass (selN_Z)
        ('dilepton_mass_2', 'selN_Z', 81., 101.,   'm_{ll} [GeV]', 0.15, 'lin'),
        
        # zed candidate direction (selN_mZ)
        ('cos_theta_Z', 'selN_mZ', 9999., 0.8,   '|cos#theta_{ll}|', 0.15, 'lin'),
        
        # leptonic recoil mass (selN_cos)
        ('m_recoil_2', 'selN_cos', 120., 140.,   'm_{recoil} [GeV]', 0.15, 'lin'),
        
        # jets momenta (selN_H)
        ('all_jets_p', 'selN_H', 15., 100.,   'p^{j} [GeV]', 0.7, 'lin'),
        ('jets_p', 'selN_H', 9999., -9999.,   'p^{j} [GeV]', 0.7, 'lin'),
        
        # invariant mass of the jets (selN_H)
        ('hadronic_mass_zoom', 'selN_H', 100., 140.,  'm_{jets} [GeV]', 0.15, 'lin'),
        
        # missing energy (selN_mhad)
        # ('missing_e',       'selN_mhad', 9999.,  30.,   'p_{miss} [GeV]', 0.7, 'lin'),
        ('missing_e',       'selN_H', 9999.,  30.,   'p_{miss} [GeV]', 0.7, 'lin'),
        
        # number of additional high-p electrons and muons (selN_miss)
        # ('N_extra_leptons', 'selN_miss', 0.5, -9999., 'N(l^{high p,extra})', 0.7, 'lin'),
        ('N_extra_leptons', 'selN_H', 0.5, -9999., 'N(l^{high p,extra})', 0.7, 'lin'),
        
        # dmerge (selN_miss)
        # ('jets_d23',       'selN_miss', 2.0,  -9999.,  'd_{23}', 0.7, 'log'),
        # ('jets_d34',       'selN_miss', 1.5,  -9999.,  'd_{34}', 0.7, 'log'),
        # ('jets_d45',       'selN_miss', 1.0,  -9999.,  'd_{45}', 0.7, 'log'),
        ('jets_d23',       'selN_H', 2.0,  -9999.,  'd_{23}', 0.7, 'log'),
        ('jets_d34',       'selN_H', 1.5,  -9999.,  'd_{34}', 0.7, 'log'),
        ('jets_d45',       'selN_H', 1.0,  -9999.,  'd_{45}', 0.7, 'log'),
        
        # tagger score
        # 'trainNN'
        ('jet1_isB',       'finalsel', 9999., -9999.,  'isB(j1)', 0.7, 'log'),
        ('jet2_isB',       'finalsel', 9999., -9999.,  'isB(j2)', 0.7, 'log'),
        ('jet1_isC',       'finalsel', 9999., -9999.,  'isC(j1)', 0.7, 'log'),
        ('jet2_isC',       'finalsel', 9999., -9999.,  'isC(j2)', 0.7, 'log'),
        ('jet1_isG',       'finalsel', 9999., -9999.,  'isG(j1)', 0.7, 'log'),
        ('jet2_isG',       'finalsel', 9999., -9999.,  'isG(j2)', 0.7, 'log'),
        ('jet1_isS',       'finalsel', 9999., -9999.,  'isS(j1)', 0.7, 'log'),
        ('jet2_isS',       'finalsel', 9999., -9999.,  'isS(j2)', 0.7, 'log'),
        ('jet1_isU',       'finalsel', 9999., -9999.,  'isU(j1)', 0.7, 'log'),
        ('jet2_isU',       'finalsel', 9999., -9999.,  'isU(j2)', 0.7, 'log'),
        ('jet1_isD',       'finalsel', 9999., -9999.,  'isD(j1)', 0.7, 'log'),
        ('jet2_isD',       'finalsel', 9999., -9999.,  'isD(j2)', 0.7, 'log'),
        ('jet1_isTAU',     'finalsel', 9999., -9999.,  'isTAU(j1)', 0.7, 'log'),
        ('jet2_isTAU',     'finalsel', 9999., -9999.,  'isTAU(j2)', 0.7, 'log'),

         # the other 4 vars used in the NN
        ('hadronic_mass',  'finalsel', 9999., -9999.,  'm_{jets} [GeV]', 0.7, 'lin'),
        ('missing_e',      'finalsel', 9999., -9999.,  'p_{miss} [GeV]', 0.7, 'lin'),

        ('jets_d23',       'finalsel', 9999., -9999.,  'd_{23}', 0.7, 'lin'),
        ('jets_d34',       'finalsel', 9999., -9999.,  'd_{34}', 0.7, 'lin'),
    ]

    processes = [
        ['wzp6_ee_eeH_Hbb_ecm240',    'wzp6_ee_mumuH_Hbb_ecm240'],
        ['wzp6_ee_eeH_Hcc_ecm240',    'wzp6_ee_mumuH_Hcc_ecm240'],
        ['wzp6_ee_eeH_Hgg_ecm240',    'wzp6_ee_mumuH_Hgg_ecm240'],
        ['wzp6_ee_eeH_Hss_ecm240',    'wzp6_ee_mumuH_Hss_ecm240']]
    processLabels = [
        'llH(b#bar{b})',
        'llH(c#bar{c})',
        'llH(gg)',
        'llH(s#bar{s})']
    processColors = [
        kRed-2,
        kPink+1,
        kOrange,
        kCyan-6]

    if splitZHother:
        processes.extend([
            ['wzp6_ee_eeH_Htautau_ecm240','wzp6_ee_mumuH_Htautau_ecm240'],
            ['wzp6_ee_eeH_HWW_ecm240',    'wzp6_ee_mumuH_HWW_ecm240'],
            ['wzp6_ee_eeH_HZZ_ecm240',    'wzp6_ee_mumuH_HZZ_ecm240']
            ])
        processLabels.extend([
            'llH(#tau#tau)',
            'llH(WW)',
            'llH(ZZ)',
            ])
        processColors.extend([
            kBlue+2,
            kBlue,
            kBlue-2
            ])
    else:
        processes.extend([
            'wzp6_ee_eeH_Htautau_ecm240','wzp6_ee_mumuH_Htautau_ecm240',
            'wzp6_ee_eeH_HWW_ecm240',    'wzp6_ee_mumuH_HWW_ecm240',
            'wzp6_ee_eeH_HZZ_ecm240',    'wzp6_ee_mumuH_HZZ_ecm240'
        ])
        processLabels.extend(['llH(other)'])
        processColors.extend([kBlue])
        
    processes.extend([
        ['p8_ee_ZZ_ecm240'],
        ['p8_ee_WW_ecm240'],
        ['p8_ee_Zqq_ecm240'],
        ['wzp6_ee_ee_Mee_30_150_ecm240', 'wzp6_ee_mumu_ecm240']
    ])
    processLabels.extend([
        'ZZ',
        'WW',
        'Z/#gamma*(q#bar{q})',
        'Z/#gamma*(ll)',
    ])
    processColors.extend([
        kGreen+2,
        kRed,
        kViolet,
        kBlack
    ])

    # baseDir = '/eos/user/g/gmarchio/fcc-test/ZllHqq/analysis-final/root/IDEA'
    # directory containing the cutflow files
    basedir += 'analysis-final/hists/'
    plotpath = basedir.replace('hists','plots') + '/nostack'
    if not os.path.isdir(plotpath):
        os.makedirs(plotpath)

    #Draw histos
    c = TCanvas('c', 'c', 800, 600)

    # loop over variables
    for iVar in range(len(vars)):
        var, sel, cutMin, cutMax, title, legPos, plotStyle = vars[iVar]
        print('Plotting variable ', var)
        
        # initialize stack and legend
        hs = THStack(var, '')
        leg = TLegend(legPos, 0.6, legPos+0.18, 0.88, '', 'brNDC')
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        
        # loop over the processes
        hist = {}
        for iProcess in range(len(processes)):

            procLabel = processLabels[iProcess]
            hist[iProcess] = TH1D()
            first = True
            for proc in processes[iProcess]:
                if (signalOnly and not 'wzp6_ee_eeH' in proc and not 'wzp6_ee_mumuH' in proc): continue
                # if (signalOnly and not 'wzp6_ee_mumuH' in proc): continue

                # open file with histos
                fileName = '{:s}/{:s}_{:s}_histo.root'.format(basedir,proc,sel)
                print('Opening file ', fileName)
                f = TFile.Open(fileName, 'READ')

                # read histo
                print('Getting histogram ', var)
                h = f.Get(var)
                if first:
                    hist[iProcess] = h.Clone(procLabel)
                    first = False
                    hist[iProcess].SetLineColor(processColors[iProcess])
                    hist[iProcess].SetLineWidth(3)
                    hist[iProcess].SetDirectory(0)                  
                else:
                    hist[iProcess].Add(h)
                #h.SetDirectory(0)

                # set graphic attributes of histo
                #h.SetLineColor(processColors[iProcess])
                #h.SetLineWidth(3)

            # normalize histo to 1
            if hist[iProcess].Integral()!=0.0:
                hist[iProcess].Scale(1./hist[iProcess].Integral(), 'nosw2')

            # add histos to stack and legend
            # do not draw histograms with too few entries otherwise plot will have large spikes
            if hist[iProcess].GetEntries()>300.:
                hs.Add(hist[iProcess])
                leg.AddEntry(hist[iProcess],procLabel,'L')


        # draw the histo stack and legend
        c.Clear()
        hs.Draw('hist nostack')    
        hs.GetXaxis().SetTitle(title)
        leg.Draw()
        c.SetLogy(plotStyle=='log')
        gPad.Update()

        # draw the cuts
        print('Drawing cuts')
        yMax = c.GetUymax()
        yMin = c.GetUymin()
        if plotStyle=='log':
            yMax = math.pow(10,yMax)
            yMin = math.pow(10,yMin)
        if cutMin>-9999. :
            l1 = TLine(cutMin, yMin, cutMin, yMax)
            l1.SetLineStyle(kDashed)
            l1.SetLineColor(kBlack)
            l1.SetLineWidth(3)
            l1.Draw()
        if cutMax<9999. :
            l2 = TLine(cutMax, yMin, cutMax, yMax)
            l2.SetLineStyle(kDashed)
            l2.SetLineColor(kBlack)
            l2.SetLineWidth(3)
            l2.Draw()

        if signalOnly:
            c.Print('{:s}/{:s}_{:s}_signal.pdf'.format(plotpath,var,sel))
        else:
            c.Print('{:s}/{:s}_{:s}_sigbkg.pdf'.format(plotpath,var,sel))

if __name__ == "__main__":
    plotvars()
