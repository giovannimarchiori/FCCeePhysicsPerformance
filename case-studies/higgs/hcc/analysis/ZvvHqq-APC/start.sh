os=`cat /etc/os-release | grep ^ID= | awk -F '"' '{print $2}'`
if [[ "$os" == "rocky" ]]; then
    source setup_rocky.sh
fi
export FCCANALYSES=$PWD/../../../../../../FCCAnalyses
export FCCANALYSIS=$PWD
export FCCANACONFS=$PWD/../../FCCAnalyses-config/ZvvHqq-APC
cwd=$PWD
cd $FCCANALYSES
source setup.sh
cd $cwd
export FCCANALYSES=$PWD/../../../../../../FCCAnalyses
