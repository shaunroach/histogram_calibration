import unittest
import sys
import os
import pdb

# add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import measure

class TestPredictRange(unittest.TestCase):
    def test_predict_range(self):
        test_histogram = [
          0.039696648553747056,
          0.03656564880067407,
          0.009250180393896206,
          0.011455577821367944,
          0.018263583045598535,
          0.02689790939149442,
          0.018746137899351634,
          0.06253634979703211,
          0.04639319650566448,
          0.05941217750543344,
          0.0861820146119475,
          0.07238543340866607,
          0.07856001016654397,
          0.0883216975219114,
          0.11494044229392424,
          0.06725677988965857,
          0.05559225704200185,
          0.043034139232424606,
          0.023262310041986943,
          0.041247506076675024
        ]

        start_histogram = 0
        bin_size = 25.0 
        end_histogram = 500.0
   
        prediction_tuples = set()
        for prediction_prob in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
            for start_ix in range(0,20,1):
                results = measure.predict_range(test_histogram, start_histogram, bin_size, prediction_prob, start_ix)
                key = (results[0], results[1], prediction_prob)
                prediction_tuples.add(key)


        prediction_list = list(prediction_tuples)
        prediction_list.sort(key=lambda x: x[2])
        #print(f"all intervals")
        #print(prediction_list)

        epsilon = 0.00001

        for prediction_prob in [0.1, 0.2, 0.3, 0.4, 0.5]:
            from_left_match = [t for t in prediction_list if t[2] == prediction_prob and t[0] == start_histogram]
            reciprocal_match = [t for t in prediction_list if t[2] == (1-prediction_prob) and t[1] == end_histogram ]
            if( len(from_left_match) > 0 ):
                diff = from_left_match[0][1] - reciprocal_match[0][0]
                print(f"checking {from_left_match[0]} vs {reciprocal_match[0]}")
                self.assertTrue(diff < epsilon)
                
            
            from_right_match = [t for t in prediction_list if t[2] == prediction_prob and t[1] == end_histogram]
            reciprocal_match_right = [t for t in prediction_list if t[2] == (1-prediction_prob) and t[0] == start_histogram ]
            if( len(from_right_match) > 0 ):
                diff = from_right_match[0][0] - reciprocal_match_right[0][1]
                print(f"checking {from_right_match[0]} vs {reciprocal_match_right[0]}")
                self.assertTrue(diff < epsilon)
                
           

if __name__ == "__main__":
    unittest.main()
