import unittest
from _lib import *
import HtmlXmlTestRunner_pkg.HtmlXmlTestRunner as HtmlXmlTestRunner

class SmokeTests(unittest.TestCase):
    def test_100_Start_Browser(self):
        print("XXXXXXXXX Test 1111 started XXXXXXXXX")
        Browser.Start(r"file:///C:/Users/IvomirAssi/Desktop/Lectures/Day-12/1_SampleWebpage.html")
        sleep(1)
        Browser.Maximize()

    def test_200_Check_Stop_Button(self):
        print("XXXXXXXXX Test 222 started XXXXXXXXX")
        click(SamplePage_UI.button_Reload)
        click(SamplePage_UI.button_Test)
        clipboard = UIActions.CopyAllClipboard()
        assert "Clicked" in clipboard

suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
HtmlXmlTestRunner.HTMLTestRunner(file(r"Report.html", "w")).run(suite)

# ↓↓↓↓↓ In the end of the file is another logic to run test ↓↓↓↓↓↓↓


















## It's not the shortest version, but for sure it works stable for years :)
## Recommended to use it
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)

#     # #Use it to add manually test cases - handy when debugging a specific part of the set
# 	  # suite = unittest.TestSuite()
#     # suite.addTest(SmokeTests('test_100_Start_Browser'))
#     # suite.addTest(SmokeTests('FREE_SLOT_FOR_THE_NEXT_TEST'))

#     outfile = open("Report.html", "w")
#     runner = HtmlXmlTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report', description="Description")
#     runner.run(suite)
#     outfile.close()
