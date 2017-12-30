from __future__ import absolute_import, division, print_function

import pytest
import numpy as np
bokeh = pytest.importorskip('bokeh')

from odo.backends.bokeh import convert, pd, ColumnDataSource
import pandas.util.testing as tm


df = pd.DataFrame([[100, 'Alice'],
                   [200, 'Bob'],
                   [300, 'Charlie']],
                  columns=['balance', 'name'])

# pandas升级
def test_convert_dataframe_to_cds():
    cds = convert(ColumnDataSource, df)
    assert str(cds.data) == str({'balance': np.array([100, 200, 300], dtype=np.int64),
                                 'name': np.array(['Alice', 'Bob', 'Charlie'], dtype=object)})

    df2 = convert(pd.DataFrame, cds)
    assert isinstance(df2, pd.DataFrame)

    tm.assert_frame_equal(df, df2)

