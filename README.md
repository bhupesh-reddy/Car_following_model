# Car_following_model


 This repository provides Python code for processing the Next Generation Simulation (NGSIM) Vehicle Trajectories and Supporting Data, for Interstate 80 (I-80) vehicle trajectory dataset and extracting leader-follower vehicle trajectory pairings. These pairings can be used to evaluate driving behaviour and create automobile following models. Observation is strictly adhered to the same Lane traffic data.

### 2. Data Source

 - The datasource is collected by the Next Generation Simulation (NGSIM) Vehicle Trajectories and Supporting Data, Transportation department of US and reconstructed data for I80 data is requested from the following link http://www.multitude-project.eu/reconstructed-ngsim.html



### 3. Data processing.


- Cleaning the data for empty and null values based on the absence of preceeding vehicle.
- Create the lead and following vehicle pairs variable.
- filtering the data to select Lane 1,2,3 data.
- Created a Time variable for the vehicle pair.
- grouped data based on the vehicle pairs for futher calculations.


### 4. Exploratory Data Analysis

