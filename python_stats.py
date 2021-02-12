from math import sqrt
class Stats:

  def __init__(self):
    pass

  def mean(self, vector):
    length = len(vector)
    return pow(length, -1) * sum(vector)

  def std(self, vector):
    mean_vector = self.mean(vector)
    length = len(vector)
    summatory = []
    for i in vector:
      summatory.append((i - mean_vector)**2)
    return sqrt(pow(length, -1) * sum(summatory))

  def kurtosis(self, vector):
    standard_vector = self.std(vector)
    mean_vector = self.mean(vector)
    length = len(vector)
    summatory = []
    for i in vector:
      summatory.append(pow((i - mean_vector), 4))
    return (1/length) * (sum(summatory) / pow(standard_vector,4))

  def skewness(self, vector):
    standard_vector = self.std(vector)
    mean_vector = self.mean(vector)
    length = len(vector)
    summatory = []
    for i in vector:
      summatory.append(pow((i-mean_vector), 3))
    return (1/length) * (sum(summatory) / pow(standard_vector, 3))
  
  def covariance(self, X,Y):
    length = len(X)
    mean_x = self.mean(X)
    mean_y = self.mean(Y)
    summatory = []
    for x,y in zip(X,Y):
      summatory.append((x-mean_x) * (y-mean_y))
    return (1/length) * sum(summatory)
  
  def correlation(self,X,Y):
    cov = self.covariance(X,Y)
    std_X = self.std(X)
    std_Y = self.std(Y)

    return cov / (std_X * std_Y)

  def confidence_interval(self, da, a_few=1.96):
    yes_ans = 0
    n = len(da)
    for i in da:
        if i[1]:
            yes_ans += 1
    
    p_hat = yes_ans / n
    compute_error = lambda x: sqrt((x*(1-x)) / n)
    error = compute_error(p_hat)
    
    pos = p_hat + a_few * error
    neg = p_hat - a_few * error

    return pos, neg


if __name__ == "__main__":
  stats = Stats()
  X = [1,2,3,4,5,6,7,8,9,10]
  Y = [7,6,5,4,5,6,7,8,9,10]
  da = [["Jose", 0], ["Esteban", 1], ["Pepe", 1], ["Ernesto", 1], ["Tio", 0], ["Carmen", 1], ["idio", 1], ["Ro", 0], ["jose", 1]]
  print(stats.confidence_interval(da))
