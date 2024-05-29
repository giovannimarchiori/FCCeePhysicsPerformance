os=`cat /etc/os-release | grep ^ID= | awk -F '"' '{print $2}'`
if [[ "$os" == "rocky" ]]; then
    source setup_rocky.sh
fi
cwd=$PWD
cd $FCCANALYSESPKG
source setup.sh
cd $cwd


