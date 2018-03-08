# How to Run SimpleGenderComputer

### To run, first install dependencies:

  `pip install -r requirements.txt`

### Then generate a set of names to compare:

  `python getGender.py` 

Inside this file you will see:
    
    gc = SimpleGenderComputer('nameLists') 

----
### Publication
We have use this tool to analyze Peer Parity in a recent paper: 
[Someone Like Me: How Does Peer Parity Influence
Participation of Women on Stack Overflow?](http://www4.ncsu.edu/~dford3/papers/peer-parity-VLHCC17.pdf)

BibTeX:
  
    @inproceedings{ford2017someone,
    author={Ford, Denae and Harkins, Alisse and Parnin, Chris},
    title={{Someone Like Me}: How Does Peer Parity Influence Participation of Women on Stack Overflow?},
    booktitle = {Proceedings of the IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC)},
    series = {VL/HCC '17},
    pages={239-243}, 
    doi={10.1109/VLHCC.2017.8103473}, 
    year={2017},
    month={Oct}
    }

This tool has been inspired by Vasilescu et al.'s [genderComputer](https://github.com/tue-mdse/genderComputer) tool.


