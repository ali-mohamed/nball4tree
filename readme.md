# Install the package

* for Ubuntu platform please first install python3-tk
```
sudo apt-get install python3-tk
```

* for Ubuntu or Mac platform type:

```
$ git clone https://github.com/gnodisnait/nball4tree.git
$ cd nball4tree
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

```

# Experiment 1:  Training and evaluating nball embeddings
## Experiment 1.1: Training nball embeddings
* [datasets for training arabic nball embeddings](https://drive.google.com/open?id=1XJC7RVwIBNGd3P3ML3AAUn7ut5EvuIlA)
* shell command for running the nball construction and training process
```
% you need to create an empty file nball.txt for output

$ python nball.py --train_nball data/nball.txt --w2v dataset/w2v.ar --ws_child dataset/wordSenseChildren.ar --ws_catcode dataset/catcode.ar --log log.txt
% --train_nball: output file of nball embeddings
% --w2v: file of pre-trained word embeddings
% --ws_child: file of parent-children relations among word-senses
% --ws_catcode: file of the parent location code of a word-sense in the tree structure
% --log: log file, shall be located in the same directory as the file of nball embeddings
```
The training process can take around 2 hours. 


## Experiment 1.2: Checking whether tree structures are perfectly embedded into word-embeddings
* main input is the output directory of nballs created in Experiment 1.1
* shell command for running the nball construction and training process
```
$ python nball.py --zero_energy <output-path> --ball <output-file> --ws_child /Users/<user-name>/data/glove/wordSenseChildren.txt
% --zero_energy <output-path> : output path of the nballs of Experiment 1.1, e.g. ```data/data_out```
% --ball <output-file> : the name of the output nball-embedding file, e.g. ```data/nball.txt```
% --ws_child dataset/wordSenseChildren.ar: file of parent-children relations among word-senses
```
The checking process can take around 20 minutes.
* result

If zero-energy is achieved, a big nball-embedding file will be created ```<output-path>/<output-file>```
otherwise, failed relations and word-senses will be printed.

** Test result at Ubuntu platform:
![img|630x420](https://github.com/gnodisnait/nball4tree/blob/master/pic/success_result.png)
 
- [nball embeddings with 6103 balls](https://drive.google.com/open?id=1cgRKKxa0apPE3RLkUiPY46l64VDc92k9)

# Experiment 2: Observe neighbors of word-sense using nball embeddings
* [pre-trained nball embeddings](https://drive.google.com/open?id=1cgRKKxa0apPE3RLkUiPY46l64VDc92k9)
```
$ python nball.py --neighbors "TrAbls_n1AR" --ball data/nball.txt  --num 10
% --neighbors: list of word-senses
% --ball: file location of the nball embeddings
% --num: number of neighbors
```

* Results of nearest neighbors look like below:

 <a href="url"><img src="https://github.com/gnodisnait/nball4tree/blob/master/pic/nbneighbors.png"   height="700" width="500" ></a></p>

# References

Tiansi Dong, Chrisitan Bauckhage, Hailong Jin, Juanzi Li, Olaf Cremers, Daniel Speicher, Armin B. Cremers, Joerg Zimmermann (2019). *Imposing Category Trees Onto Word-Embeddings Using A Geometric Construction*. **ICLR-19** The Seventh International Conference on Learning Representations, May 6 – 9, New Orleans, Louisiana, USA.

