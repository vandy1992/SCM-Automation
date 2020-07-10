from unittest import TestLoader, TestSuite, TextTestRunner
from tests.PR_Create_New import PR_createnew
from tests.PR_split_merge import Split_Merge_test
from tests.PT_Create_New import purchase_tender_Test
from tests.test_PT_split_merge import Split_Merge_PT
import allure
import pytest

import testtools as testtools

if __name__=="__main__":

    loader=TestLoader()
    suite=TestSuite((
        loader.loadTestsFromTestCase(PR_createnew),
        loader.loadTestsFromTestCase(Split_Merge_test),
        loader.loadTestsFromTestCase(purchase_tender_Test),
        loader.loadTestsFromTestCase(Split_Merge_PT)
        ))

    runner=TextTestRunner(verbosity=2)
    runner.run(suite)

    # concurrent_suite= testtools.ConcurrentStreamTestSuite(lambda : ((case, None) for case in suite))
    # concurrent_suite.run(testtools.StreamResult())



