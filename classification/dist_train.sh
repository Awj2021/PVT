env_name="pvt"
miniconda=/mnt/fast/nobackup/scratch4weeks/wa00433/miniconda3
# conda=/mnt/fast/nobackup/scratch4weeks/wa00433/miniconda3/bin/conda
# source $miniconda/etc/profile.d/conda.sh
# $conda init
# $conda activate $env_name
cd /mnt/fast/nobackup/scratch4weeks/wa00433/projects/repos/PVT/classification/
$miniconda/envs/$env_name/bin/python3.8 main.py --config configs/pvt_v2/pvt_v2_b2.py

