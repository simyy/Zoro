#!/bin/bash

# 项目

GitUrl=""

# 环境

ENV="DEV"
PATH="/opt/work"


while getopts "e:p:" opt; do  
    case $opt in 
        e)
            ENV=$OPTARG
            ;;
        p)
            PATH=$OPTARG
            ;;
    esac
done

echo "Current ENV: $ENV"
echo "Current PATH: $PATH"

# virtualenv

if [ ! -d "$PATH/zoro" ];then
    cd $PATH
    virtualenv -p python3 zoro
fi

# git

cd "$PATH/zoro"
git clone $GitUrl $PATH/zoro/src

# active env

cd $PATH/zoro
source $PATH/zoro/bin/activate

# install package

pip install -r $PATH/zoro/src/requirements.txt

# run deamon

# Todo ...
