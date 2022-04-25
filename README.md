# Car_following_model


 This repository provides Python code for processing the Next Generation Simulation (NGSIM) Vehicle Trajectories and Supporting Data, for Interstate 80 (I-80) vehicle trajectory dataset and extracting leader-follower vehicle trajectory pairings. These pairings can be used to evaluate driving behaviour and create automobile following models. Observation is strictly adhered to the same Lane traffic data. The code provided here is used to reation time 1 sec. 
 
 To reproduce the work presented here you can follow the below steps.

# Execution steps in local machine.

1. System Requirements.
2. Data source.
3. datacleaning
4. Model execution. 
5. Results

### System Requirements.

- python 3.7.0 or higher versions
- packages(Sklearn, metrics, numpy, matplotlib.pyplot, seaborn, random, sklearn.ensemble(RandomForestRegressor), plot_vehicle_pair, sklearn.metrics(r2_score,mean_absolute_error, mean_squared_error) )
- operating system - Windows 
- IDE - Jupyter Notebook/sypder
- 
### 2. Data Source

 - The datasource is collected by the Next Generation Simulation (NGSIM) Vehicle Trajectories and Supporting Data, Transportation department of US and reconstructed data for I80 data is requested from the following link http://www.multitude-project.eu/reconstructed-ngsim.html



### 3. Data processing.

Download the "I80_restructuring_data_modelling.ipynb"  notebook file and executed the cells to clean the data.

##### cleaning process.

- Cleaning the data for empty and null values based on the absence of preceeding vehicle.
- Create the lead and following vehicle pairs variable.
- filtering the data to select Lane 1,2,3 data.
- Created a Time variable for the vehicle pair.
- grouped data based on the vehicle pairs for futher calculations.
- saving the cleaned data as new file.

### Model.
- Download ML_models folder and execute the mentioned cells in the given order. 
pairs-selection.py -> pairs_split_prediction.py -> pairsselection.py -> plot_vehicle_pair.py -> model.py
- This python files can be executed from Spyder. While executing use the clean dataset stored from the results from data cleaning step.
- plots will be generated in the end.

### Result.
The RMSE,MAE,MAPE are calculated for the predicted values.


