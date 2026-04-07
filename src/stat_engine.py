class StatEngine:
    def __init__(self, data):
        self.data = self._clean_data(data)

    def _clean_data(self, data):
        if not data:
            raise ValueError("Data cannot be empty")

        clean = []
        for x in data:
            if isinstance(x, (int, float)):
                clean.append(x)
            else:
                raise TypeError("All elements must be numeric")

        return clean
    #mean

    def get_mean(self):
        return sum(self.data) / len(self.data)
    
    #median

    def get_median(self):
        data = sorted(self.data)
        n = len(data)
        mid = n // 2

        if n % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        else:
            return data[mid]
    
    # mode

    def get_mode(self):
        freq = {}

        for x in self.data:
            freq[x] = freq.get(x, 0) + 1

        max_count = max(freq.values())
        
        if max_count == 1:
            return "No mode (all values are unique)"

        modes = [k for k, v in freq.items() if v == max_count]
        return modes
    # variance

    def get_variance(self, is_sample=True):
        mean = self.get_mean()
        n = len(self.data)

        squared_diff = [(x - mean) ** 2 for x in self.data]
        total = sum(squared_diff)

        if is_sample:
            return total / (n - 1)
        else:
            return total / n
    
    # standard deviation

    def get_standard_deviation(self, is_sample=True):
        variance = self.get_variance(is_sample)
        return variance ** 0.5
    
    # outliers

    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()

        outliers = []
        for x in self.data:
            if abs(x - mean) > threshold * std:
                outliers.append(x)

        return outliers


    