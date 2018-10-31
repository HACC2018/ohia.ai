import time
import numpy as np
import pandas as pd
from statsmodels.distributions.empirical_distribution import ECDF
from sklearn.linear_model import Ridge
from scipy.stats import rankdata

def run_length_encoding(im):
    pixels = im.flatten(order = 'F')
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return ' '.join(str(x) for x in runs)

class RunLengthEncoder(object):
    """Run length encoding of a binary array."""
    
    def __init__(self, order='C', one_indexing=False):
        """
        order: {'K', 'A', 'C', 'F'}, optional
            Passed to the numpy.flatten function.            
        one_indexing: bool, optional
            If True then start indexing at 1 (rather than 0). The default is False.
        """                      
        
        self._one_indexing = one_indexing
        self._order = order
        
    def encode(self, x: np.ndarray) -> str: 
        """Run length encoding of a binary array.      
        
        Args:
            x: numpy.array
                Binary input array.  
        Returns:
            rle_str: 
                Run length encoded values.  Indexs and lengths are space delimited. 
        """                      
        pixels = x.flatten(order = self._order)
        pixels = np.concatenate([[0], pixels, [0]])
        runs = np.where(pixels[1:] != pixels[:-1])[0] + self._one_indexing
        runs[1::2] -= runs[::2]
        return ' '.join(str(x) for x in runs)
    
    def decode(self, rle_str: str, shape: tuple) -> np.ndarray:
        """Decoding of a run length encoded array.
        
        Args:
            rle_str: str
                run-length string (space delimited)
            shape: tuple
                size (height,width) of array to return 
        Returns:
            x: 
                binary array of size `shape`
        """
        s = rle_str.split()
        starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
        starts -= self._one_indexing
        ends = starts + lengths
        
        img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
        for lo, hi in zip(starts, ends):
            img[lo:hi] = 1
        return img.reshape(shape, order=self._order)


class FastLabelEncoder():
    """Map categorical variable into {0, 1, ..., n_categories}. 
    
    Note: https://stackoverflow.com/questions/45321999/how-can-i-optimize-label-encoding-for-large-data-sets-sci-kit-learn?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa    
    """
    def __init__(self):
        self.lookup = None
    
    def fit(self, x): 
        labels = np.unique(x, return_inverse=True)[1]
        self.lookup = dict(zip(x.flatten(),labels))    
        
    def transform(self, x): 
        return np.vectorize(self.lookup.get)(x)
    
    def fit_transform(self, x):
        self.fit(x)
        return self.transform(x)    


class MeanImputer():
    """Single column mean imputation
    """    
    def __inti__(self):
        self.replace_value = None
    
    def fit(self, x): 
        self.replace_value = np.mean(x[np.isfinite(x)])
        
    def transform(self, x): 
        y = x.copy()
        y[~np.isfinite(x)] = self.replace_value
        return y
    
    def fit_transform(self, x):
        self.fit(x)
        return self.transform(x)    
    
    
class BinEncoder():
    """Bin a numeric variable into {0, 1, ...n_bins-1}.
    """
    def __init__(self, n_bins=100):
        self.n_bins = n_bins
        self.ecdf = None
    
    def fit(self, x): 
        """Calculate empirical CDF 
        Args:
            x (array): input array
        """              
        self.ecdf = ECDF(x)
        
    def transform(self, x): 
        """Transform using empirical CDF 
        Args:
            x (array): array to transform
        """                      
        return np.ceil(self.n_bins*self.ecdf(x)).astype(np.int)
    
    def fit_transform(self, x):
        """Calculate and Transform using empirical CDF 
        Args:
            x (array): array to transform
        """                              
        self.fit(x)
        return self.transform(x)    


class RankEncoder():
    """Map an ordinal variable into {0, 1, ...n_unique} The order
    of the variable is preserved.
    """
    def __init__(self):
        self.lookup = None
    
    def fit(self, x): 
        x = np.unique(np.array(x))
        r = rankdata(x).astype(np.int)
        self.lookup = dict(zip(x, r))    
        
    def transform(self, x): 
        x = np.array(x)
        return np.vectorize(self.lookup.get)(x)
    
    def fit_transform(self, x):
        self.fit(x)
        return self.transform(x)    



class BayesianEncoder():
    """Bayesian target encoding using various posterior statistics. 
    """
    
    def __init__(self, group_col, target_col, stat_type='mean', N_min=1000):
        """
        Args:
            group_col (str): column to group by
            target_col (str): target variable used in encoding
            stat_type (str): Statistic to encode. One of the following: "mean", 
            "var", "median", "skewness", "kurtosis".  Default is "mean".
            N_min (int): Pseudo count hyperparameter. Larger values favor the prior
            distribution. Default is 1000. 
        """
        self._group_col = group_col
        self._target_col = target_col
        self._stat_type = stat_type
        self._N_min = N_min
        
    # get counts from train set
    def fit(self, df):
        """Calculate posterior parameters        
        Args:
            df (DataFrame): Dataframe containing the target_col and group columns
        """        
        self._prior_mean = np.mean(df[self._target_col])
        stats = df[[self._target_col, self._group_col]].groupby(self._group_col)
        stats = stats.agg(['sum', 'count'])[self._target_col]    
        stats.rename(columns={'sum': 'n', 'count': 'N'}, inplace=True)
        stats.reset_index(level=0, inplace=True)           
        self._stats = stats
        
    # extract posterior statistics
    def transform(self, df):
        """Lookup posterior parameters. 
        Args:
            df (DataFrame): Dataframe containing the target_col and group columns
        Returns:
            value (array): Encoded group variable.
        """              
                
        df_stats = pd.merge(df[[self._group_col]], self._stats, how='left')
        n = df_stats['n'].copy()
        N = df_stats['N'].copy()
        
        # fill in missing
        nan_indexs = np.isnan(n)
        n[nan_indexs] = self._prior_mean
        N[nan_indexs] = 1.0
        
        # prior parameters
        N_prior = np.maximum(self._N_min-N, 0)
        alpha_prior = self._prior_mean*N_prior
        beta_prior = (1-self._prior_mean)*N_prior
        
        # posterior parameters
        alpha = alpha_prior + n
        beta =  beta_prior + N-n
        
        # calculate statistics
        if self._stat_type=='mean':
            num = alpha
            dem = alpha+beta
        
        elif self._stat_type=='var':
            num = alpha*beta
            dem = (alpha+beta)**2*(alpha+beta+1)
            
        elif self._stat_type=='mode':
            num = alpha-1
            dem = alpha+beta-2
            
        elif self._stat_type=='median':
            num = alpha-1/3
            dem = alpha+beta-2/3
        
        elif self._stat_type=='skewness':
            num = 2*(beta-alpha)*np.sqrt(alpha+beta+1)
            dem = (alpha+beta+2)*np.sqrt(alpha*beta)

        elif self._stat_type=='kurtosis':
            num = 6*(alpha-beta)**2*(alpha+beta+1) - alpha*beta*(alpha+beta+2)
            dem = alpha*beta*(alpha+beta+2)*(alpha+beta+3)

        elif self._stat_type=='weight_of_evidence':
            num = np.log(alpha/beta)
            dem = 1.0
            
        elif self._stat_type=='information_value':            
            num = (alpha - beta) * np.log(alpha/beta)
            dem = 1.0    
        else:
            raise NotImplementedError('stat_type not defined')
            
        # replace missing
        value = num/dem
        value[~np.isfinite(value)] = np.nanmedian(value)
        return value
    
    def fit_transform(self, df):
        self.fit(df)
        return self.transform(df)



class RidgeEncoder():
    """Mapping from numeric variable to target using ridge regression.
    """    
    def __init__(self, encode_col, target_col, alpha=1):
        """
        Args:
            encode_col (str): Column to encode.
            target_col (str): Target variable to predict.
            alpha: l2 penalty. Default is alpha=1
        """               
        self._encode_col = encode_col
        self._target_col = target_col
        self._model = Ridge(alpha)
        
    def fit(self, df): 
        """Fit a model to the data.
        Args:
            df (DataFrame): Dataframe containing the target_col and group columns
        """                      
        X = np.expand_dims(df[self._encode_col], 1)
        y = df[self._target_col].values
        self._model.fit(X, y)

    def transform(self, df): 
        """Predict target col. 
        Args:
            df (DataFrame): Dataframe containing the target_col and group columns
        Returns:
            value (array): Predicted target value.
        """                      
        X = np.expand_dims(df[self._encode_col], 1)
        return self._model.predict(X)
    
    def fit_transform(self, x):
        self.fit(df)
        return self.transform(df)        