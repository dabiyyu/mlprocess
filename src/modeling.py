import sys
sys.path.insert(1, '/Users/dabiyyu/Downloads/mlprocess/src')
import util as utils
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

def load_train_feng(params: dict):
    # Load train set
    X_train = utils.pickle_load(params["train_feng_set_path"][0])
    y_train = utils.pickle_load(params["train_feng_set_path"][1])

    return X_train, y_train

def load_valid(params: dict):
    # Load valid set
    X_valid = utils.pickle_load(params["valid_feng_set_path"][0])
    y_valid = utils.pickle_load(params["valid_feng_set_path"][1])

    return X_valid, y_valid

def load_test(params: dict):
    # Load tets set
    X_test = utils.pickle_load(params["test_feng_set_path"][0])
    y_test = utils.pickle_load(params["test_feng_set_path"][1])

    return X_test, y_test

def train_model(X_train, y_train, X_valid, y_valid):
    dtr = DecisionTreeRegressor()
    dtr.fit(X_train, y_train)

    y_pred = dtr.predict(X_valid)
    print(mean_squared_error(y_valid, y_pred)**0.5)

    return dtr

if __name__ == "__main__" :
    # 1. Load config file
    config = utils.load_config()

    # 2. Load set data
    X_train, y_train = load_train_feng(config)
    X_valid, y_valid = load_valid(config)
    X_test, y_test = load_test(config)

    # 3. Train model
    dtr = train_model(X_train, y_train, X_valid, y_valid)

    # 4. Dump model
    utils.pickle_dump(dtr, config["production_model_path"])