# Bimodal-Detection-analysis
Analysis of the Ventral Prefrontal Cortex in the Bimodal Detection Task

## Preprocesing

The spikesorting was done using the toposort repository. The neuron .csv files used for the analysis contain the spike times for each unit centered at the time of the stimulus arrival. The arrays are in the shape trials x n_spikes.
The name is in the form:

session_electrode_neuronID.csv

for example:

059_002e1neuron_1_.csv

Each session has an associated psychometric file in the form:

psycho_session.csv

for example:

psycho059_002.csv

The file named "All_Psyco.csv" contains the label of the corresponding psychometric file for each neuron.

## Import

An example of how to import the data in Python can be found in the file "Import_VPC.py", and with MATLAB in the file "VPC_Neuron_analyser.mlx" under the "Import" section.


## Analysis

Analyses for the VPC and the RNN data were done in MATLAB, with the file:

->  VPC_Neuron_analyser.mlx

For the mistake trials analysis, a separate file was used:

->  VPC_Neuron_analyser.mlx

RNN models were trained in PyTorch:

-> RNN_BDT.ipynb


Contents of **VPC_Neuron_analyser.mlx**:
* Import
* Psychometrics
* Frequency
* GLM
* MLM
* Mutual Information
* Mutual Information pairs
* AUROC
* Variance
* PCA
* PS Similarity
* dPCA (using Kobak repository, found at https://github.com/machenslab/dPCA)
