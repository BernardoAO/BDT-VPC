# Bimodal-Detection-analysis
Analysis of the Ventral Prefrontal Cortex in the Bimodal Detection Task

### PREPROCESING:

The spikesorting was done using the toposort repository. The neuron files used for the analysis contain ...
in the form:

session_electrode_neuronID.csv

For example:

059_002e1neuron_1_.csv

Each session has an associated psychometric file in the form:

psycho_session.csv

For example:

psycho059_002.csv

## IMPORT

An example of how to import the data in Python can be found in the file "Import_VPC.py" and in Matlab in the file "VPC_Neuron_analyser.mlx" under the section "Import".


### ANALYSIS:

Analyses for the VPC and the RNN data were done in Matlab, with the file:

->  VPC_Neuron_analyser.mlx

For the mistake trials analysis, a separate file was used:

->  VPC_Neuron_analyser.mlx

RNN models runned in Colab:

-> RNN_BDT.ipynb


Contents of **VPC_Neuron_analyser.mlx**:
* Import
* Psychometrics
* Firering Rate
* GLM
* Mutual Information
* Mutual Information pairs
* AUROC
* Variance
* PCA
* PS Similarity
* dPCA
