# Full Load Electrical Power Output Prediction

The reliability and sustainability of gas turbines in power plants are very dependent on the power output generated. By predicting the resulting power output, it is expected to be able to increase the efficiency and profit of the power plant.

## Predictor
- Ambient Temperature (degree celcius)
- Atmospheric Pressure (mbar)
- Relative Humidity (%)
- Vacuum (exhaust steam pressure) (cm Hg)

## Target
Full Load Electrical Power Output (MW)

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

## Reference
Pınar Tüfekci, Prediction of full load electrical power output of a base load operated combined cycle power plant using machine learning methods, International Journal of Electrical Power & Energy Systems, Volume 60, September 2014, Pages 126-140, ISSN 0142-0615, https://www.sciencedirect.com/science/article/abs/pii/S0142061514000908?via%3Dihub
