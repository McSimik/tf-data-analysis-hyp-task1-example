import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 964993301 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    px=x_success/x_cnt
    py=y_success/y_cnt
    dis=px*(1-px)/x_cnt + py*(1-py)/y_cnt
    
    return (py-px)/np.sqrt(dis) <= norm.ppf(0.02)
