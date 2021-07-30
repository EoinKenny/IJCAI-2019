# IJCAI-2019: Twin-Systems to Explain Artificial Neural Networks Using Case-Based Reasoning


This repository is the official implementation for the above IJCAI paper (https://www.ijcai.org/proceedings/2019/376). 

An updated version of the algorithm and user studies was recently published at the *Artificial Intelligence Journal* (https://www.sciencedirect.com/science/article/pii/S0004370221000102). It is recommended you refer to this article. I made a colab file which you can use to see the most up-to-date version of the twin system algorithm here:

*SEE UP-TO-DATE VERSION OF TWIN-SYSTEM ALGORITHM HERE*
https://colab.research.google.com/drive/1j62207B5kgKbwFdy4ac9eeO417-nu-rn?usp=sharing



The most up-to-date version of the algorithm is currently being reviewed at the *Knowledge-Based-Systems* journal.

![alt text](https://github.com/EoinKenny/IJCAI-2019/blob/master/imgs/twinsystem.png)



## Requirements

To install requirements:

```setup
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```



## Generating An Explanation
Follow the notebooks one by one to go through the experiments and recreate the results of the main paper.

![alt text](https://github.com/EoinKenny/IJCAI-2019/blob/master/imgs/cifar.png)

![alt text](https://github.com/EoinKenny/IJCAI-2019/blob/master/imgs/mnist.png)





## Results

Table of results from experiment 2 using CNNs:

![alt text](https://github.com/EoinKenny/IJCAI-2019/blob/master/imgs/results.png)





## Cite Bibtext

@inproceedings{ijcai2019-376,
  title     = {Twin-Systems to Explain Artificial Neural Networks using Case-Based Reasoning: Comparative Tests of Feature-Weighting Methods in ANN-CBR Twins for XAI},
  author    = {Kenny, Eoin M. and Keane, Mark T.},
  booktitle = {Proceedings of the Twenty-Eighth International Joint Conference on
               Artificial Intelligence, {IJCAI-19}},
  publisher = {International Joint Conferences on Artificial Intelligence Organization},             
  pages     = {2708--2715},
  year      = {2019},
  month     = {7},
  doi       = {10.24963/ijcai.2019/376},
  url       = {https://doi.org/10.24963/ijcai.2019/376},
}

 }
