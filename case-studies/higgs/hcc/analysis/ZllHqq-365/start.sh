os=`cat /etc/os-release | grep ^ID= | awk -F '"' '{print $2}'`
if [[ "$os" == "rocky" ]]; then
    source setup_rocky.sh
fi
export FCCANALYSES=$PWD/../../../../../../FCCAnalyses
export FCCANALYSIS=$PWD
export FCCANACONFS=$PWD/../../FCCAnalyses-config/ZllHqq-365
cwd=$PWD
cd $FCCANALYSES
source setup.sh
cd $cwd
export FCCANALYSES=$PWD/../../../../../../FCCAnalyses
if [[ "$os" == "rocky" ]]; then
    export FCCANAOUTPUT=
else
    export FCCANAOUTPUT=/eos/user/g/gmarchio/fcc/analysis/selection/ZllHqq-365/
fi
