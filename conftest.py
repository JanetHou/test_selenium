# coding:utf-8

import sys
import os
import pytest
from utils.logutils import logger


@pytest.fixture(scope="module", autouse=True)
def set_sys_path():
    p = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(p)
    logger.info("path is :" + p)
