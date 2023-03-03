LDAGRL

A lncRNA-disease association prediction tool development based on bridge heterogeneous information network via graph representation learning for family medicine and primary care (LDAGRL)/<br>


Data: 
Five types of biomedical entities feature information and nine kinds of biomedical entity associations information.
-----

Code:

    The source code of LDAGRL_SDNE:

        AllNode
        -----------------
              A way to build a BHnet

        NodeFeature
        -----------------
              The calculation method of node feature

        TrainTest
        -----------------
              Training and prediction algorithms
          
        OpenNE-master
        -----------------
               A Open-source framework for conducting graph embedding inclding SDNE,node2vec,deepwalk etc.
    

     The source code of LDAGRL_GCN:

        Training and prediction codes

      

(i)Example for LDAGRL_SDNE:

Requirements:
numpy==1.21.6
pandas==1.3.5
networkx==2.0
scipy==0.19.1
tensorflow==1.10.0
gensim==3.0.1
scikit-learn==1.0.2
matplotlib==3.5.2
   
   
You can valide the model by running each of the code files listed below:

   (1)TrainTestBridge.py
   (2)TrainTestAttribute.py
   (3)TrainTestAttribute+Bridge.py

Specifically, you can:

   cd example/
   
   cd TrainTestAttribute/
      run TrainTestAttribute.py
      
   cd TrainTestBridge/
      run TrainTestBridge.py
      
   cd TrainTestAttribute+Bridge/
      run TrainTestAttribute+Bridge.py

(ii)Example for LDAGRL_GCN:

Requirements:
torch==1.11.0
torch-geometric==2.0.4
xgboost==1.6.2
scikit-learn==1.0.2
pandas==1.3.5
numpy==1.21.6
matplotlib==3.5.2

Specifically, you can:

cd LDAGRL_GCN/ 
1. Run python main_pyg.py to obtian the embedding of nodes.
2. After obtaining the embedding of nodes, you can run classify.ipynb to obtain the predictive results.

        

