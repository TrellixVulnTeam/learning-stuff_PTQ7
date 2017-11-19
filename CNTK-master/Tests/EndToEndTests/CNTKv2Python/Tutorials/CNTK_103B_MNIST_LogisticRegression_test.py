# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

import os
import re
import numpy as np

abs_path = os.path.dirname(os.path.abspath(__file__))
notebook = os.path.join(abs_path, "..", "..", "..", "..", "Tutorials", "CNTK_103B_MNIST_LogisticRegression.ipynb")

def test_cntk_103b_mnist_logisticregression_noErrors(nb):
    errors = [output for cell in nb.cells if 'outputs' in cell
              for output in cell['outputs'] if output.output_type == "error"]
    assert errors == []

expectedEvalErrorByDeviceId = { -1: 7.4, 0: 7.4 }

def test_cntk_103b_mnist_logisticregression_evalCorrect(nb, device_id):
    testCell = [cell for cell in nb.cells
                if cell.cell_type == 'code' and re.search('trainer\.test_minibatch', cell.source)]
    assert len(testCell) == 1
    m = re.match(r"Average test error: (?P<actualEvalError>\d+\.\d+)%\r?$", testCell[0].outputs[0]['text'])
    # TODO tighten tolerances
    assert np.isclose(float(m.group('actualEvalError')), expectedEvalErrorByDeviceId[device_id], atol=0.5)
