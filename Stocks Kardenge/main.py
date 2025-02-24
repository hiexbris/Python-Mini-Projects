import yfinance
import pandas
import numpy as np
from sklearn.metrics import f1_score, roc_auc_score


def read_data():
    global stock_OHLC
    data = yfinance.download('BAJFINANCE.NS', '2020-01-01', '2024-01-01') # cal for BajajFinance
    df = data.to_csv('data')
    stock_OHLC = pandas.read_csv('data')


def msa():
    # MSA calc
    stock_OHLC['MA_50'] = stock_OHLC['Close'].rolling(window=50).mean()
    stock_OHLC['MA_200'] = stock_OHLC['Close'].rolling(window=200).mean()


def ema():
    # EMA calc
    stock_OHLC['EMA_5'] = stock_OHLC['Close'].ewm(span=5, adjust=False).mean()


def rsi():
    # RSI calc
    delta = stock_OHLC['Close'].diff(1)
    # calc amount of gain and loss
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    RS = gain / loss
    # applying formula
    RSI = 100 - (100 / (1 + RS))
    stock_OHLC['RSI'] = RSI


def macd():
    # calc macd
    stock_OHLC['EMA_12'] = stock_OHLC['Close'].ewm(span=12, min_periods=0, adjust=False).mean()
    stock_OHLC['EMA_26'] = stock_OHLC['Close'].ewm(span=26, min_periods=0, adjust=False).mean()
    stock_OHLC['MACD'] = stock_OHLC['EMA_12'] - stock_OHLC['EMA_26']
    stock_OHLC['MACD_signal_line'] = stock_OHLC['MACD'].ewm(span=9, min_periods=0, adjust=False).mean()


def bollinger_bonds():
    # calc bollinger_bonds
    stock_OHLC['MA_20'] = stock_OHLC['Close'].rolling(window=20).mean()
    stock_OHLC['std_20'] = stock_OHLC['Close'].rolling(window=20).std()
    stock_OHLC['upper_band'] = stock_OHLC['MA_20'] + 2 * stock_OHLC['std_20']
    stock_OHLC['lower_band'] = stock_OHLC['MA_20'] - 2 * stock_OHLC['std_20']


def buy_sell_hold_msa(lst):
    # the -1 and 1 signifies if the msa line is below close or above close, if it goes form below to bottom we write a target variable

    result = []
    prev_val = None
    count_1 = 0
    count_minus_1 = 0

    for val in lst:
        if prev_val is not None:
            if prev_val == -1 and val == 1:  # Change from -1 to 1
                result.append("buy")
                count_minus_1 = 0  # Reset count for -1
            elif prev_val == 1 and val == -1:  # Change from 1 to -1
                result.append("sell")
                count_1 = 0  # Reset count for 1
            elif val == 1:
                count_1 += 1
                if count_1 >= 5:
                    result.append("buy")
                else:
                    result.append('hold')
            elif val == -1:
                count_minus_1 += 1
                if count_minus_1 >= 5:
                    result.append("sell")
                else:
                    result.append('hold')
            else:
                result.append('hold')
        else:
            result.append('hold')  # Initial value

        prev_val = val
    return result


def msa_signal():
    # basically checks whether the line is below or above close
    signal_msa_200 = np.where((stock_OHLC['MA_200'] > stock_OHLC['Close']), 1, np.where((stock_OHLC['MA_200'] < stock_OHLC['Close']), -1, 0))
    stock_OHLC['MSA_200_signal'] = buy_sell_hold_msa(signal_msa_200)

    signal_msa_50 = np.where((stock_OHLC['MA_50'] > stock_OHLC['Close']), 1, np.where((stock_OHLC['MA_50'] < stock_OHLC['Close']), -1, 0))
    stock_OHLC['MSA_50_signal'] = buy_sell_hold_msa(signal_msa_50)


def buy_sell_hold_ema(lst):
    # same thing sma one does

    result = []
    prev_val = None

    for val in lst:
        if prev_val is not None:
            if prev_val == -1 and val == 1:  # Change from -1 to 1
                result.append("sell")
            elif prev_val == 1 and val == -1:  # Change from 1 to -1
                result.append("buy")
            else:
                result.append('hold')
        else:
            result.append('hold')  # Initial value

        prev_val = val
    return result


def ema_signal():
    # checks whether the ema line is below or above close
    signal_ema_5 = np.where((stock_OHLC['EMA_5'] > stock_OHLC['Close']), 1, np.where((stock_OHLC['EMA_5'] < stock_OHLC['Close']), -1, 0))
    stock_OHLC['EMA_5_signal'] = buy_sell_hold_ema(signal_ema_5)


def rsi_signal(lst):
    # converting above 70 values to buy and below 30 to sell

    result = []

    for val in lst:
        if val >= 70:
            result.append('buy')
        elif val <= 30:
            result.append('sell')
        else:
            result.append('hold')

    return result


def macd_signal(lst):
    # same thing we did for msa and ema
    result = []
    prev_val = None

    for val in lst:
        if prev_val is not None:
            if prev_val == -1 and val == 1:  # Change from -1 to 1
                result.append("buy")
            elif prev_val == 1 and val == -1:  # Change from 1 to -1
                result.append("sell")
            else:
                result.append('hold')
        else:
            result.append('hold')  # Initial value

        prev_val = val
    return result


def bollinger_bonds_signal():
    # a buy signal is generated if lower bond goes above close and then once again goes below after one day
    buy_signals = (stock_OHLC['Close'] < stock_OHLC['lower_band']) & (stock_OHLC['Close'].shift(1) > stock_OHLC['lower_band'].shift(1))

    # a buy signal is generated if upper bond goes above close and then once again goes below after one day
    sell_signals = (stock_OHLC['Close'] > stock_OHLC['upper_band']) & (stock_OHLC['Close'].shift(1) < stock_OHLC['upper_band'].shift(1))

    # Generate hold signals for periods between buy and sell signals
    hold_signals = ~(buy_signals | sell_signals)

    signals = []
    for buy, sell, hold in zip(buy_signals, sell_signals, hold_signals):
        if buy:
            signals.append('buy')
        elif sell:
            signals.append('sell')
        else:
            signals.append('hold')

    return signals


def final_conversion():

    global final_signal
    global imp_data

    final_signal = stock_OHLC.loc[200:, ['MSA_50_signal', 'MSA_200_signal', 'RSI_signal', 'bollinger_bonds_signals', 'MACD_signal', 'EMA_5_signal']].copy()
    imp_data = stock_OHLC.loc[200:, ['Close', 'MA_50', 'MA_200', 'EMA_5', 'RSI', 'MACD', 'MACD_signal_line', 'lower_band', 'upper_band']].copy()

    final_labels = []

    # we calculate the number of buy or sell according to function, if the number of buy is higher we take the final output as buy for our given data
    for index, row in final_signal.iterrows():
        count = 0

        # Count the occurrences of 'Buy' and 'Sell' in the row
        for label in row:
            if label == 'buy':
                count += 1
            elif label == 'sell':
                count -= 1

        # Determine final label based on count
        if count > 1:
            final_label = 'buy'
        elif count < -1:
            final_label = 'sell'
        else:
            final_label = 'hold'

        # Append final label to the list
        final_labels.append(final_label)

    # Add final labels to the DataFrame
    final_signal['final_signal'] = final_labels

    #we make another loop which classify the buy, sell data into buy or not to buy and sell or not to sell( 3 columns as LR only works for 0 and 1 values)
    hold = []

    for value in final_signal['final_signal']:

        if value == 'buy' or value == 'sell':
            label = 0
        elif value == 'hold':
            label = 1

        hold.append(label)

    final_signal['hold'] = hold

    buy = []

    for value in final_signal['final_signal']:

        if value == 'hold' or value == 'sell':
            label = 0
        elif value == 'buy':
            label = 1

        buy.append(label)

    final_signal['buy'] = buy

    sell = []

    for value in final_signal['final_signal']:

        if value == 'buy' or value == 'hold':
            label = 0
        elif value == 'sell':
            label = 1

        sell.append(label)

    final_signal['sell'] = sell


def add_intercept(X):
    intercept = np.ones((X.shape[0], 1))
    return np.concatenate((intercept, X), axis=1)


def sigmoid(z):
    # LR function
    return 1 / (1 + np.exp(-z))


def gradient_descent(X, y, lr=0.000000001, num_iter=10000):
    # calc gradient
    X = add_intercept(X)
    theta = np.zeros(X.shape[1]) # making theta matrices

    for i in range(num_iter):
        # calc z using matrix multiply
        z = np.dot(X, theta)
        # predicting vlaues
        h = sigmoid(z)
        # h - y signifies the error
        gradient = np.dot(X.T, (h - y)) / y.size
        # then theta is mutliplies by gradient and LR s overtime it gets corrected
        theta -= lr * gradient

    return theta


def predict_prob(X, theta):
    X = add_intercept(X)
    # now we give it our testing data to calculate probability
    return sigmoid(np.dot(X, theta))


read_data()
msa()
ema()
rsi()
macd()
bollinger_bonds()
msa_signal()
ema_signal()

stock_OHLC['bollinger_bonds_signals'] = bollinger_bonds_signal()
signal_macd_5 = np.where((stock_OHLC['MACD'] > stock_OHLC['MACD_signal_line']), 1, np.where((stock_OHLC['MACD'] < stock_OHLC['MACD_signal_line']), -1, 0))
stock_OHLC['MACD_signal'] = macd_signal(signal_macd_5)
stock_OHLC['RSI_signal'] = rsi_signal(stock_OHLC['RSI'])

final_conversion()

# finding out vlaues for theta for hold or not to hold, buy or not to buy, ... as LR only works for 2 variables so we have to break our question in 3 loops then calculate the highest probability

hold_theta = gradient_descent(imp_data.to_numpy(), final_signal['hold'].to_numpy())
buy_theta = gradient_descent(imp_data.to_numpy(), final_signal['buy'].to_numpy())
sell_theta = gradient_descent(imp_data.to_numpy(), final_signal['sell'].to_numpy())


ding_dong = predict_prob(imp_data.tail(5).to_numpy(), hold_theta)
ding_dong_1 = predict_prob(imp_data.tail(5).to_numpy(), buy_theta)
ding_dong_2 = predict_prob(imp_data.tail(5).to_numpy(), sell_theta)

arrays = [ding_dong, ding_dong_1, ding_dong_2]

max_indices = []

# here we find the highest probability of hold , buy , sell and take actions

for i in range(len(ding_dong)):
    max_val = float('-inf')
    max_index = None
    for j, arr in enumerate(arrays):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = j
    max_indices.append(max_index)

for i in range(0, len(max_indices)):
    if max_indices[i] == 0:
        max_indices[i] = 'hold'
    elif max_indices[i] == 1:
        max_indices[i] = 'buy'
    elif max_indices[i] == 2:
        max_indices[i] = 'sell'

print(max_indices)

f1 = f1_score(final_signal['hold'], predict_prob(imp_data.to_numpy(), hold_theta))
auc_roc = roc_auc_score(final_signal['hold'], predict_prob(imp_data.to_numpy(), hold_theta))

