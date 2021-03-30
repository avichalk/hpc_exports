# Your job will use 1 node, 9 cores, and 54gb of memory total.
#PBS -q standard
#PBS -l select=1:ncpus=9:mem=54gb:pcmem=6gb
### Specify a name for the job
#PBS -N job_name
### Specify the group name
#PBS -W group_list=yshirley
### Used if job requires partial node only
#PBS -l place=pack:shared
### CPUtime required in hhh:mm:ss.
### Leading 0's can be omitted e.g 48:0:0 sets 48 hours
#PBS -l cputime=00:00:10
### Walltime is how long your job will run
#PBS -l walltime=00:00:10
### Joins standard error and standard out
#PBS -j oe



print('hello world! this works!')

