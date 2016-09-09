# Homework 1

**Name**: Yuxuan Han

**NetID**: yxh204

### Assignment 2

I used the following chain of commands to create a new directory named `PUI2016_yxh204` in my compute environment and the environment variable and alias that come with it.
```
ssh -X -A -t yxh204@gw.cusp.nyu.edu ssh -A -X compute
```

```
mkdir PUI2016_yxh204
```

```
touch .bash_profile
echo "PUI2016=/home/cusp/yxh204/PUI2016_yxh204" >> .bash_profile
echo "alias pui2016='cd $PUI2016'" >> .bash_profile
source .bash_profile
```
