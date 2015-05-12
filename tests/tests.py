

import unittest
import tika
import tika.parse
#from english_class import AttrSet, row_synth, row_keys, to_csv, to_json


#sys.path.append('..')

class CreateTest(unittest.TestCase):
    "Test for New Generator.py Methods"

    def test_local_pdf(self):
        "Parse local PDF"
        self.assertTrue(tika.parse.from_file('201504160015.pdf'))

    def test_local_pdf(self):
        "Parse remote PDF"
        self.assertTrue(tika.parse.from_file(\
            'http://appsrv.achd.net/reports/rwservlet?food_rep_insp&P_ENCOUNTER=201502090012'))


if __name__ == '__main__':
	unittest.main()