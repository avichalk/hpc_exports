#!/bin/bash

# Your job will use 1 node, 2 cores, and 12gb of memory total.
#PBS -q windfall
#PBS -l select=1:ncpus=1:mem=6gb:pcmem=6gb
### Specify a name for the job
#PBS -N mov_job_1
### Specify the group name
#PBS -W group_list=yshirley
### Used if job requires partial node only
#PBS -l place=pack:shared
### Leading 0's can be omitted e.g 48:0:0 sets 48 hours
### Walltime is how long your job will run
#PBS -l walltime=000:50:00
### Joins standard error and standard out
#PBS -j oe

cd /home/u20/avichalk/exports/programs/mov_2
python mov_1_2.py 
