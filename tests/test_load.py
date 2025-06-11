import pytest
import pandas as pd
from unittest.mock import patch
from load.load_to_s3 import upload_df


@patch("load.load_to_s3.boto3.client")
def test_load_to_s3_calls_put_object(mock_boto_client):
    df = pd.DataFrame({"symbol": ["AAPL"], "price": [150]})
    mock_s3 = mock_boto_client.return_value
    upload_df(df, data_type="stock")
    assert mock_s3.upload_file.called
