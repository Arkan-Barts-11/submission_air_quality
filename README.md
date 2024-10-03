# Air Quality Dashboard 🌫️

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir submission_air_quality
cd submission_air_quality
python -m venv myenv
myenv\Scripts\activate
pipenv install
pipenv shell
pip install matplotlib streamlit pandas
pip install -r requirements.txt
```

## Run jupyter
```
jupyter-notebook .
```

## Run steamlit app
```
cd dashboard
streamlit run dashboard.py
```
