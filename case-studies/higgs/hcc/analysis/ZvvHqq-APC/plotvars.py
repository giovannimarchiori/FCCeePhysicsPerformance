# do plots of histograms produced by fccanalysis final

# import common definitions
import os, sys
configdir = os.getenv('FCCANACONFS')
sys.path.append(configdir)
from analysis_config import *

# import ROOT and other libraries
import ROOT
from ROOT import kRed, kPink, kOrange, kCyan, kBlue, kGreen, kViolet, kBlack
from ROOT import kYellow, kDashed, gPad
from ROOT import TCanvas, THStack, TLegend, TFile, TLine, TH1D
import math
import argparse

splitZHother = True

def plotvars(signalOnly = False):

    from analysis_config import basedir
    # vars: varname, preselection, cutmin, cutmax, axis title, legend position, plot type
    vars = [
        # momentum of all leptons (SelNone)
        ('leptons_p'                          , 'selNone',           9999.,     20., 'p(leptons) [GeV]'            , 0.7, 'lin'),

        # missing mass
        ('higgs_hadronic_recoil_mass'         , 'selNone',           9999.,  -9999., 'm_{miss} [GeV]'              , 0.7, 'lin'),

        # number of high momentum leptons
        ('n_selected_leptons'                 , 'selNone',           9999.,     1.0, 'N(high-p leptons)'           , 0.7, 'lin'),
#        ('higgs_hadronic_mass'                , 'sel_dmerge',       100.,    135., 'm_{jj} [GeV]'                , 0.7, 'lin'),
#        ('higgs_hadronic_mass'                , 'sel_dmerge',      9999.,  -9999., 'm_{jj} [GeV]'                , 0.7, 'lin'),   		
#        ('mvis'                               , 'sel_dmerge',      9999.,  -9999., 'm_{vis} [GeV]'               , 0.7, 'lin'),
        # energy of leading and subleading jets
        ('jet1_E'                             , 'sel_nolep',         45.,    105., 'E_{j1} [GeV]'                , 0.15, 'lin'),   
        ('jet2_E'                             , 'sel_nolep',         20.,     70., 'E_{j2} [GeV]'                , 0.7, 'lin'),
        # number of constituents of leading and subleading jet
        ('jet1_nconst'                        , 'sel_jetE',          10.,  -9999., 'N^{const}_{j1}'              , 0.7, 'lin'),
        ('jet2_nconst'                        , 'sel_jetE',           6.,  -9999., 'N^{const}_{j2}'              , 0.7, 'lin'),
#        ('missing_e'                          , 'sel_nconst',        20.,     70., 'p_{miss} [GeV]'              , 0.15, 'lin'),    
#        ('higgs_hadronic_cos_theta'           , 'sel_pmiss',       9999.,     0.9, 'cos(#theta_{jj})'            , 0.15, 'log'),
        # cosine of polar angle of dijet system
        ('higgs_hadronic_cos_theta'           , 'sel_nconst',        9999.,     0.9, 'cos(#theta_{jj})'            , 0.15, 'log'),
        # are two jets back-to-back in theta?
        ('higgs_hadronic_cosSumThetaJJ'       , 'sel_cosThetaJJ',      0.5,   9999., 'cos(#theta_{j1}+#theta_{j2})', 0.15, 'log'),  
#        ('jets_d23'                           , 'sel_cosSumThetaJJ', 500.,  -9999., 'd_{23}'                      , 0.7, 'log'), 
#        ('jets_d34'                           , 'sel_cosSumThetaJJ', 250.,  -9999., 'd_{34}'                      , 0.7, 'log'), 
#        ('jets_d45'                           , 'sel_cosSumThetaJJ', 100.,  -9999., 'd_{45}'                      , 0.7, 'log'), 
#        ('higgs_hadronic_cosDeltaPhiJJ_zoom'  , 'sel_mjj1',         9999.,   0.999, 'cos(#phi_{j1}-#phi_{j2})'    , 0.15, 'log'),
        # are two jets back-to-back in phi?        
        ('higgs_hadronic_cosDeltaPhiJJ_zoom'  , 'sel_cosSumThetaJJ', 9999.,   0.999, 'cos(#phi_{j1}-#phi_{j2})'    , 0.15, 'log'),
        # missing momentum
        ('pmiss'                              , 'sel_cosDPhiJJ',     9999.,  -9999., 'p_{miss} [GeV]'              , 0.15, 'lin'),
        # missing mass
        ('higgs_hadronic_recoil_mass'         , 'sel_cosDPhiJJ',       50.,    140., 'm_{miss} [GeV]'              , 0.7, 'lin'),
        # visible mass
        ('mvis'                               , 'sel_cosDPhiJJ',       70.,    150., 'm_{vis} [GeV]'               , 0.7, 'lin'),
        # missing mass, zoomed
        ('higgs_hadronic_recoil_mass_zoom'    , 'sel_cosDPhiJJ',     9999.,  -9999., 'm_{miss} [GeV]'              , 0.7, 'lin'),
        # visible mass, zoomed
        ('mvis_zoom'                          , 'sel_cosDPhiJJ',     9999.,  -9999., 'm_{vis} [GeV]'               , 0.7, 'lin'),
        # tagging score for leading and subleading jets
        ('jet1_isB'                           , 'trainNN',         9999.,  -9999., 'isB(j1)'                     , 0.7, 'log'), 
        ('jet2_isB'                           , 'trainNN',         9999.,  -9999., 'isB(j2)'                     , 0.7, 'log'), 
        ('jet1_isC'                           , 'trainNN',         9999.,  -9999., 'isC(j1)'                     , 0.7, 'log'), 
        ('jet2_isC'                           , 'trainNN',         9999.,  -9999., 'isC(j2)'                     , 0.7, 'log'), 
        ('jet1_isG'                           , 'trainNN',         9999.,  -9999., 'isG(j1)'                     , 0.7, 'log'), 
        ('jet2_isG'                           , 'trainNN',         9999.,  -9999., 'isG(j2)'                     , 0.7, 'log'), 
        ('jet1_isS'                           , 'trainNN',         9999.,  -9999., 'isS(j1)'                     , 0.7, 'log'), 
        ('jet2_isS'                           , 'trainNN',         9999.,  -9999., 'isS(j2)'                     , 0.7, 'log'), 
        ('jet1_isQ'                           , 'trainNN',         9999.,  -9999., 'isQ(j1)'                     , 0.7, 'log'), 
        ('jet2_isQ'                           , 'trainNN',         9999.,  -9999., 'isQ(j2)'                     , 0.7, 'log'),
        # dmerge for 3->2 and 4->3 steps
        ('jets_d23'                           , 'trainNN',         9999.,  -9999., 'd_{23}'                      , 0.7, 'lin'),
        ('jets_d34'                           , 'trainNN',         9999.,  -9999., 'd_{34}'                      , 0.7, 'lin'),
#        ('higgs_hadronic_mass'                , 'trainNN',         9999.,  -9999., 'm_{jj} [GeV]'                , 0.7, 'lin'),         
    ]
    
    processes = [
        [ 'wzp6_ee_nunuH_Hbb_ecm240' ],
        [ 'wzp6_ee_nunuH_Hcc_ecm240' ],
        [ 'wzp6_ee_nunuH_Hgg_ecm240' ],
        [ 'wzp6_ee_nunuH_Hss_ecm240' ]
    ]
    processLabels = [
        '#nu#bar{#nu}H(b#bar{b})',
        '#nu#bar{#nu}H(c#bar{c})',
        '#nu#bar{#nu}H(gg)',
        '#nu#bar{#nu}H(s#bar{s})'
    ]
    processColors = [
        kRed-2,
        kPink+1,
        kOrange,
        kCyan-6
    ]
    if splitZHother:
        processes.extend([
            ['wzp6_ee_nunuH_Htautau_ecm240'],
            ['wzp6_ee_nunuH_HWW_ecm240'],
            ['wzp6_ee_nunuH_HZZ_ecm240'],
        ])
        processLabels.extend([
            '#nu#bar{#nu}H(#tau#tau)',
            '#nu#bar{#nu}H(WW)',
            '#nu#bar{#nu}H(ZZ)'

        ])
        processColors.extend([
            #kBlue+2,
            kYellow+2,
            kBlue,
            kBlue-2
        ])
    else:
        processes.extend([
            [
                'wzp6_ee_nunuH_Htautau_ecm240',
                'wzp6_ee_nunuH_HWW_ecm240',
                'wzp6_ee_nunuH_HZZ_ecm240'
            ]
        ])
        processLabels.extend(['#nu#bar{#nu}H(other)'])
        processColors.extend([kBlue])
    processes.extend([
        [ 'p8_ee_ZZ_ecm240' ],
        [ 'p8_ee_WW_ecm240' ],
        [ 'p8_ee_Zqq_ecm240' ],
        [ 'wzp6_ee_nuenueZ_ecm240' ],
    ])
    processLabels.extend([
        'ZZ',
        'WW',
        'Z/#gamma*(q#bar{q})',
        '#nu_{e}#bar{#nu}_{e}Z',    
    ])
    processColors.extend([
        kGreen+2,
        kRed,
        kViolet,
        kBlack
    ])

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
                if (signalOnly and not 'wzp6_ee_nunuH' in proc): continue

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
    parser = argparse.ArgumentParser()
    parser.add_argument("--signalOnly", action="store_true")  # default is false
    args = parser.parse_args()
    plotvars(args.signalOnly)