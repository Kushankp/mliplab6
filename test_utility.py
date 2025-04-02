import pytest
import pandas as pd
import numpy as np
from prediction_demo import data_preparation,data_split,train_model,eval_model

@pytest.fixture
def housing_data_sample():
    return pd.DataFrame(
      data ={
      'price':[13300000,12250000],
      'area':[7420,8960],
    	'bedrooms':[4,4],	
      'bathrooms':[2,4],	
      'stories':[3,4],	
      'mainroad':["yes","yes"],	
      'guestroom':["no","no"],	
      'basement':["no","no"],	
      'hotwaterheating':["no","no"],	
      'airconditioning':["yes","yes"],	
      'parking':[2,3],
      'prefarea':["yes","no"],	
      'furnishingstatus':["furnished","unfurnished"]}
    )

def test_data_preparation(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    # Target and datapoints has same length
    assert feature_df.shape[0]==len(target_series)

    #Feature only has numerical values
    assert feature_df.shape[1] == feature_df.select_dtypes(include=(np.number,np.bool_)).shape[1]

@pytest.fixture
def feature_target_sample(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    return (feature_df, target_series)

def test_data_split(feature_target_sample):
    # Split the feature-target sample using the data_split function
    return_tuple = data_split(*feature_target_sample)

    # Ensure the length of return_tuple is 4 (X_train, X_test, y_train, y_test)
    assert len(return_tuple) == 4, f"Expected tuple length of 4, but got {len(return_tuple)}"

    # Extract X_train, X_test, y_train, y_test from the return_tuple
    X_train, X_test, y_train, y_test = return_tuple

    # Ensure X_train and X_test have the same number of columns as the original feature data
    assert X_train.shape[1] == feature_target_sample[0].shape[1], "X_train has different number of features"
    assert X_test.shape[1] == feature_target_sample[0].shape[1], "X_test has different number of features"

    # Adjust the expected values for small sample sizes
    expected_y_train_size = max(1, int(feature_target_sample[1].shape[0] * 0.8))
    expected_y_test_size = feature_target_sample[1].shape[0] - expected_y_train_size

    # Ensure that y_train and y_test have the correct number of rows
    assert y_train.shape[0] == expected_y_train_size, f"y_train has {y_train.shape[0]} rows, expected {expected_y_train_size}"
    assert y_test.shape[0] == expected_y_test_size, f"y_test has {y_test.shape[0]} rows, expected {expected_y_test_size}"

    # Additional sanity checks: X_train and X_test should not be identical
    assert not X_train.equals(X_test), "X_train and X_test should not be the same"

    # Ensure the same for y_train and y_test
    assert not y_train.equals(y_test), "y_train and y_test should not be the same"
