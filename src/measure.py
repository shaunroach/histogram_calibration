import pdb

def convert_histogram_to_specific_prediction(ahistogram):
    prob_possiblities = list(range(0.5,1.0,0.1))


def predict_range(histogram, start_histogram, bin_size, prediction_prob, start_index=0):
    curr_prob = 0.0
    start_range = start_histogram + start_index * bin_size
    end_range = start_histogram + len(histogram) * bin_size
    
    for i in range(start_index, len(histogram)):
        if curr_prob + histogram[i] < prediction_prob:
            curr_prob += histogram[i]
        else:
            # Calculate the fraction of the current bin that is needed
            needed_frac = (prediction_prob - curr_prob) / histogram[i]
            end_range = start_histogram + i * bin_size + needed_frac * bin_size
            curr_prob += histogram[i]*needed_frac
            break
    
    while curr_prob < prediction_prob and start_index > 0:
        start_index -= 1
        curr_prob += histogram[start_index]
        if curr_prob > prediction_prob:
            needed_frac = (curr_prob - prediction_prob) / histogram[start_index]
            start_range = start_histogram + start_index * bin_size + needed_frac * bin_size
            break
        start_range = start_histogram + start_index * bin_size
    
    return start_range, end_range


class HistogramParameters():
    def __init__(self):
        self.start = None 
        self.end = None 
        self.num_bins = None 
        self.bin_size = None 

class SpecificPrediction():
    def __init__(self):
        self.label = None 
        self.interval_start = None 
        self.interval_end = None 
        self.probability = None
        self.actual_result = None 
        self.binary_result = None 


class PredictionDataOrganizer():
    def __init__(self):
        self.labels = [] 
        self.histograms = []
        self.actual_results = [] 


if __name__ == "__main__":

    pdb.set_trace()
    