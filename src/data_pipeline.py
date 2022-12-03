import pandas as pd
import sys
sys.path.insert(1, '/Users/dabiyyu/Downloads/mlprocess/src')
import util as utils
import copy
from sklearn.model_selection import train_test_split

def read_raw_data(config: dict) -> pd.DataFrame:
    # Return raw dataset
    return pd.read_excel(config["dataset_path"])

def check_data(input_data: pd.DataFrame, config: dict, api: bool = False):
    input_data = copy.deepcopy(input_data)
    config = copy.deepcopy(config)

    if not api:
        # Check column data types
        assert input_data.select_dtypes("float").columns.to_list() == \
            config["float_columns"], "an error occurs in float column(s)."

        # Check range of PE
        assert input_data[config["float_columns"][4]].between(
            config["range_pe"][0],
            config["range_pe"][1]
            ).sum() == len(input_data), "an error occurs in PE range."

    else:
        # In case checking data from api
        # Last 4 column names in list of int columns are not used as predictor (NC2.5, NC1.0, NC0.5, and PM2.5)
        float_columns = config["float_columns"]
        del float_columns[-1:]

        # Check column data types
        assert input_data.select_dtypes("float64").columns.to_list() == \
            float_columns, "an error occurs in float column(s)."

        # Check range of AT
        assert input_data[config["float_columns"][0]].between(
            config["range_at"][0],
            config["range_at"][1]
            ).sum() == len(input_data), "an error occurs in AT range."

        # Check range of V
        assert input_data[config["float_columns"][1]].between(
            config["range_v"][0],
            config["range_v"][1]
            ).sum() == len(input_data), "an error occurs in V range."

        # Check range of AP
        assert input_data[config["float_columns"][2]].between(
            config["range_ap"][0],
            config["range_ap"][1]
            ).sum() == len(input_data), "an error occurs in AP range."

        # Check range of RH
        assert input_data[config["float_columns"][3]].between(
            config["range_rh"][0],
            config["range_rh"][1]
            ).sum() == len(input_data), "an error occurs in RH range."

def split_data(input_data: pd.DataFrame, config: dict):
    # Split predictor and label
    X = input_data[config["predictors"]].copy()
    y = input_data[config["label"]].copy()

    # 1st split train and test
    X_train, X_test, \
    y_train, y_test = train_test_split(
        X, y,
        test_size = config["test_size"],
        random_state = 42
    )

    # 2nd split test and valid
    X_valid, X_test, \
    y_valid, y_test = train_test_split(
        X_test, y_test,
        test_size = config["valid_size"],
        random_state = 42
    )

    return X_train, X_valid, X_test, y_train, y_valid, y_test

if __name__ == "__main__":
    # 1. Load configuration file
    config = utils.load_config()

    # 2. Read all raw dataset
    raw_dataset = read_raw_data(config)

    # 3. Data defense
    check_data(raw_dataset, config)

    # 4. Splitting train, valid, and test set
    X_train, X_valid, X_test, \
        y_train, y_valid, y_test = split_data(raw_dataset, config)

    # 5. Save train, valid and test set
    utils.pickle_dump(X_train, config["train_set_path"][0])
    utils.pickle_dump(y_train, config["train_set_path"][1])

    utils.pickle_dump(X_valid, config["valid_set_path"][0])
    utils.pickle_dump(y_valid, config["valid_set_path"][1])

    utils.pickle_dump(X_test, config["test_set_path"][0])
    utils.pickle_dump(y_test, config["test_set_path"][1])

    utils.pickle_dump(raw_dataset, config["dataset_cleaned_path"])
