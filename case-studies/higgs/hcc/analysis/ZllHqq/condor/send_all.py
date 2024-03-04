import os, sys

debug = False

## MC production to run on
production = 'winter2023'
detector = 'IDEA'


## name/tag of the physics analysis (SET AUTOMATICALLY, DO NOT MODIFY)
# analysis_name = 'ZllHqq'
# analysis_name = 'ZnunuHqq'
analysis_name = os.path.split(os.getcwd())[0].split('/')[-1]
print('Analysis name: ', analysis_name)


## input and output directories (SET AUTOMATICALLY, DO NOT MODIFY)
indir = '/eos/experiment/fcc/ee/generation/DelphesEvents/'+production+'/'+detector
outdir = '/eos/user/g/gmarchio/fcc-test/{:s}/analysis-stage1/root/{:s}/'.format(analysis_name, detector)
print('Input location: ', indir)
print('Output location: ', outdir)


## analysis script (SET AUTOMATICALLY, DO NOT MODIFY)
# script = '../../{:s}/analysis.py'.format(analysis_name)
anaconfigs = os.getenv('FCCANACONFS')
if anaconfigs == '':
    anaconfigs = '../../../FCCAnalyses-config/%s/' % analysis_name

print('Config directory: ', anaconfigs)
script = '%s/analysis_stage1.py' % anaconfigs
print('Analysis script: ' , script)


## run nev_per_job = -1 to run on all event in input root files
# TRY LONGLUNCH IF JOBS DO NOT START
#queue = 'longlunch'
queue = 'workday'
#queue = 'espresso'
#nev_per_job = 100
nev_per_job = -1
print('Condor queue: ', queue)
print('Condor events per job: ', nev_per_job)


## list of samples to run on
samples = []

if analysis_name=='ZllHqq':
    samples = [
            # Z(ll)H
            'wzp6_ee_eeH_Hbb_ecm240',
            'wzp6_ee_eeH_Hcc_ecm240',
            'wzp6_ee_eeH_Hss_ecm240',
            'wzp6_ee_eeH_Hgg_ecm240',
            'wzp6_ee_eeH_Htautau_ecm240',
            'wzp6_ee_eeH_HWW_ecm240',
            'wzp6_ee_eeH_HZZ_ecm240',
            'wzp6_ee_mumuH_Hbb_ecm240',
            'wzp6_ee_mumuH_Hcc_ecm240',
            'wzp6_ee_mumuH_Hss_ecm240',
            'wzp6_ee_mumuH_Hgg_ecm240',
            'wzp6_ee_mumuH_Htautau_ecm240',
            'wzp6_ee_mumuH_HWW_ecm240',
            'wzp6_ee_mumuH_HZZ_ecm240',
        ]
    samples.extend([
        # bkg
        'p8_ee_WW_ecm240',
        'p8_ee_ZZ_ecm240',
        'p8_ee_Zqq_ecm240',
        'wzp6_ee_mumu_ecm240',
        'wzp6_ee_ee_Mee_30_150_ecm240'
        ])
elif analysis_name == 'ZnunuHqq':
    samples = [
            # Z(nunu)H
            'wzp6_ee_nunuH_Hbb_ecm240',
            'wzp6_ee_nunuH_Hcc_ecm240',
            'wzp6_ee_nunuH_Hss_ecm240',
            'wzp6_ee_nunuH_Hgg_ecm240',
            'wzp6_ee_nunuH_Htautau_ecm240',
            'wzp6_ee_nunuH_HWW_ecm240',
            'wzp6_ee_nunuH_HZZ_ecm240',
            # Z(bb)H
            'wzp6_ee_bbH_Hbb_ecm240',
            'wzp6_ee_bbH_Hcc_ecm240',
            'wzp6_ee_bbH_Hss_ecm240',
            'wzp6_ee_bbH_Hgg_ecm240',
            'wzp6_ee_bbH_Htautau_ecm240',
            'wzp6_ee_bbH_HWW_ecm240',
            'wzp6_ee_bbH_HZZ_ecm240',
            # Z(cc)H
            'wzp6_ee_ccH_Hbb_ecm240',
            'wzp6_ee_ccH_Hcc_ecm240',
            'wzp6_ee_ccH_Hss_ecm240',
            'wzp6_ee_ccH_Hgg_ecm240',
            'wzp6_ee_ccH_Htautau_ecm240',
            'wzp6_ee_ccH_HWW_ecm240',
            'wzp6_ee_ccH_HZZ_ecm240',
            # Z(ss)H
            'wzp6_ee_ssH_Hbb_ecm240',
            'wzp6_ee_ssH_Hcc_ecm240',
            'wzp6_ee_ssH_Hss_ecm240',
            'wzp6_ee_ssH_Hgg_ecm240',
            'wzp6_ee_ssH_Htautau_ecm240',
            'wzp6_ee_ssH_HWW_ecm240',
            'wzp6_ee_ssH_HZZ_ecm240',
            # Z(qq)H
            'wzp6_ee_qqH_Hbb_ecm240',
            'wzp6_ee_qqH_Hcc_ecm240',
            'wzp6_ee_qqH_Hss_ecm240',
            'wzp6_ee_qqH_Hgg_ecm240',
            'wzp6_ee_qqH_Htautau_ecm240',
            'wzp6_ee_qqH_HWW_ecm240',
            'wzp6_ee_qqH_HZZ_ecm240',
        ]
    samples.extend([
        # bkg
        'p8_ee_WW_ecm240',
        'p8_ee_ZZ_ecm240',
        'p8_ee_Zqq_ecm240',
        'wzp6_ee_nuenueZ_ecm240'
        #'wzp6_ee_mumu_ecm240',
        #'wzp6_ee_ee_Mee_30_150_ecm240'    
    ])


from datetime import datetime
now = datetime.now()
string = now.strftime('%Y-%m-%d-%H:%M:%S')
logfile = 'condor-sub-%s.txt' %string

outf = open(logfile, 'w')
outf.write('Analysis name: %s\n' % analysis_name)
outf.write('Input location: %s\n' % indir)
outf.write('Output location: %s\n' % outdir)
outf.write('Config directory: %s\n' % anaconfigs)
outf.write('Analysis script: %s\n' % script)
outf.write('Condor queue: %s\n' % queue)
outf.write('Condor events per job: %s\n\n' % nev_per_job)


### run condor jobs
# os.system('rm -rf std/*')
for s in samples:
    cmd = 'python submitAnalysisJobs.py --indir {}/{} '.format(indir, s)
    cmd += '--outdir {}/{} '.format(outdir, s)
    cmd += '--queue {} --script {} --nev {} '.format(queue, script, nev_per_job)
    if debug:
        cmd += '--dry'
    print(cmd)
    outf.write(cmd)
    outf.write('\n')
    os.system(cmd)
