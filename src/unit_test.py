import preprocessing
import util as utils
import pandas as pd
import numpy as np

def test_remove_outliers():
    # Arrange
    config = utils.load_config()

    mock_data = {
            "AP" : [],
            "RH" : []
            }
    mock_data = pd.DataFrame(mock_data)

    expected_data = {
            "AP" : [],
            "RH" : []
            }
    expected_data = pd.DataFrame(expected_data)

    # Act
    processed_data = preprocessing.remove_outliers(mock_data)

    # Assert
    assert processed_data.equals(expected_data)