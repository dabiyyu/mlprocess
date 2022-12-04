# Full Load Electrical Power Output Prediction

The reliability and sustainability of gas turbines in power plants are very dependent on the power output generated. By predicting the resulting power output, it is expected to be able to increase the efficiency and profit of the power plant.

## Predictor
- Ambient Temperature (AT) degree celcius
- Atmospheric Pressure (AP) mbar
- Relative Humidity (RH) %
- Vacuum (exhaust steam pressure, V) cm Hg

## Target
Full Load Electrical Power Output (PE) MW

## Data Preparation Flowchart
![Alt text](/assets/data_prep.png "Data Preparation")

## Preprocessing Flowchart
![Alt text](/assets/preprocessing.png "Preprocessing")

## Modeling Flowchart
![Alt text](/assets/modeling.png "Modeling")

## Running on Local Machine
1. Download this repository
2. Run api.py
    <br /> &emsp; $ python /src/api.py
3. Run streamlit.py
    <br /> &emsp; $ streamlit run /src/streamlit.py
4. Open http://localhost:8501 in browser
5. Enter variables, then click predict

### input format
integer or float

### output format
float
