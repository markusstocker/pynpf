source activate pynpf
conda build recipe
conda install --use-local pynpf
conda remove pynpf
source deactivate pynpf

conda env list
conda create --name pynpf python
conda env remove --name pynpf
