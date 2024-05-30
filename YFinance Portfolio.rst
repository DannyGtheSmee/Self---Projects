.. code:: ipython3

    import pandas
    pandas._version




.. parsed-literal::

    <module 'pandas._version' from '/Users/throwgoods/anaconda3/lib/python3.10/site-packages/pandas/_version.py'>




.. code:: ipython3

    import pandas as pd
    import yfinance as yf  # Yahoo Finance API
    
    # Fetch historical stock data
    ticker = 'AAPL'
    data = yf.download(ticker, start='2023-01-01', end='2023-11-01')
    
    # Display data
    print(data.head())
    
    # Perform analysis (e.g., calculate moving averages)
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    
    # Visualization
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Stock Price')
    plt.plot(data['SMA_50'], label='50-day SMA')
    plt.plot(data['SMA_200'], label='200-day SMA')
    plt.legend()
    plt.show()



.. parsed-literal::

    [*********************100%%**********************]  1 of 1 completed
                      Open        High         Low       Close   Adj Close  \
    Date                                                                     
    2023-01-03  130.279999  130.899994  124.169998  125.070000  124.374802   
    2023-01-04  126.889999  128.660004  125.080002  126.360001  125.657639   
    2023-01-05  127.129997  127.769997  124.760002  125.019997  124.325081   
    2023-01-06  126.010002  130.289993  124.889999  129.619995  128.899521   
    2023-01-09  130.470001  133.410004  129.889999  130.149994  129.426575   
    
                   Volume  
    Date                   
    2023-01-03  112117500  
    2023-01-04   89113600  
    2023-01-05   80962700  
    2023-01-06   87754700  
    2023-01-09   70790800  



.. image:: output_2_1.png


.. code:: ipython3

    pip install yfinance


.. parsed-literal::

    Collecting yfinance
      Downloading yfinance-0.2.31-py2.py3-none-any.whl (65 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m65.6/65.6 kB[0m [31m1.3 MB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hRequirement already satisfied: pytz>=2022.5 in ./anaconda3/lib/python3.10/site-packages (from yfinance) (2022.7)
    Collecting frozendict>=2.3.4
      Downloading frozendict-2.3.8-cp310-cp310-macosx_10_9_x86_64.whl (36 kB)
    Collecting html5lib>=1.1
      Downloading html5lib-1.1-py2.py3-none-any.whl (112 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m112.2/112.2 kB[0m [31m3.1 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting peewee>=3.16.2
      Downloading peewee-3.17.0.tar.gz (2.9 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m2.9/2.9 MB[0m [31m15.0 MB/s[0m eta [36m0:00:00[0m00:01[0m00:01[0m
    [?25h  Installing build dependencies ... [?25ldone
    [?25h  Getting requirements to build wheel ... [?25ldone
    [?25h  Preparing metadata (pyproject.toml) ... [?25ldone
    [?25hRequirement already satisfied: numpy>=1.16.5 in ./anaconda3/lib/python3.10/site-packages (from yfinance) (1.23.5)
    Requirement already satisfied: appdirs>=1.4.4 in ./anaconda3/lib/python3.10/site-packages (from yfinance) (1.4.4)
    Requirement already satisfied: lxml>=4.9.1 in ./anaconda3/lib/python3.10/site-packages (from yfinance) (4.9.1)
    Requirement already satisfied: beautifulsoup4>=4.11.1 in ./anaconda3/lib/python3.10/site-packages (from yfinance) (4.11.1)
    Collecting multitasking>=0.0.7
      Downloading multitasking-0.0.11-py3-none-any.whl (8.5 kB)
    Collecting requests>=2.31
      Downloading requests-2.31.0-py3-none-any.whl (62 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m62.6/62.6 kB[0m [31m1.7 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: pandas>=1.3.0 in ./anaconda3/lib/python3.10/site-packages (from yfinance) (1.5.3)
    Requirement already satisfied: soupsieve>1.2 in ./anaconda3/lib/python3.10/site-packages (from beautifulsoup4>=4.11.1->yfinance) (2.3.2.post1)
    Requirement already satisfied: webencodings in ./anaconda3/lib/python3.10/site-packages (from html5lib>=1.1->yfinance) (0.5.1)
    Requirement already satisfied: six>=1.9 in ./anaconda3/lib/python3.10/site-packages (from html5lib>=1.1->yfinance) (1.16.0)
    Requirement already satisfied: python-dateutil>=2.8.1 in ./anaconda3/lib/python3.10/site-packages (from pandas>=1.3.0->yfinance) (2.8.2)
    Requirement already satisfied: certifi>=2017.4.17 in ./anaconda3/lib/python3.10/site-packages (from requests>=2.31->yfinance) (2022.12.7)
    Requirement already satisfied: idna<4,>=2.5 in ./anaconda3/lib/python3.10/site-packages (from requests>=2.31->yfinance) (3.4)
    Requirement already satisfied: charset-normalizer<4,>=2 in ./anaconda3/lib/python3.10/site-packages (from requests>=2.31->yfinance) (2.0.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in ./anaconda3/lib/python3.10/site-packages (from requests>=2.31->yfinance) (1.26.14)
    Building wheels for collected packages: peewee
      Building wheel for peewee (pyproject.toml) ... [?25ldone
    [?25h  Created wheel for peewee: filename=peewee-3.17.0-py3-none-any.whl size=135721 sha256=89f2abcf5f822dc7f93267a2d01efa6c1b0ba8266698b60d38993d188e8f648c
      Stored in directory: /Users/throwgoods/Library/Caches/pip/wheels/e2/b9/da/716514851b65304b2d24f2a161398b9470da589b08a5a586c8
    Successfully built peewee
    Installing collected packages: peewee, multitasking, requests, html5lib, frozendict, yfinance
      Attempting uninstall: requests
        Found existing installation: requests 2.28.1
        Uninstalling requests-2.28.1:
          Successfully uninstalled requests-2.28.1
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    conda-repo-cli 1.0.41 requires requests_mock, which is not installed.
    conda-repo-cli 1.0.41 requires clyent==1.2.1, but you have clyent 1.2.2 which is incompatible.
    conda-repo-cli 1.0.41 requires nbformat==5.4.0, but you have nbformat 5.7.0 which is incompatible.
    conda-repo-cli 1.0.41 requires requests==2.28.1, but you have requests 2.31.0 which is incompatible.[0m[31m
    [0mSuccessfully installed frozendict-2.3.8 html5lib-1.1 multitasking-0.0.11 peewee-3.17.0 requests-2.31.0 yfinance-0.2.31
    Note: you may need to restart the kernel to use updated packages.


.. code:: ipython3

    import pandas as pd
    import yfinance as yf  # Yahoo Finance API
    
    # Fetch historical stock data
    ticker = 'NKE'
    data = yf.download(ticker, start='2023-01-01', end='2023-11-01')
    
    # Display data
    print(data.head())
    
    # Perform analysis (e.g., calculate moving averages)
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    
    # Visualization
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Stock Price')
    plt.plot(data['SMA_50'], label='50-day SMA')
    plt.plot(data['SMA_200'], label='200-day SMA')
    plt.legend()
    plt.show()



.. parsed-literal::

    [*********************100%%**********************]  1 of 1 completed
                      Open        High         Low       Close   Adj Close  \
    Date                                                                     
    2023-01-03  118.550003  119.489998  117.440002  118.750000  117.629326   
    2023-01-04  119.959999  122.230003  119.529999  121.209999  120.066109   
    2023-01-05  120.279999  122.339996  120.080002  120.620003  119.481682   
    2023-01-06  122.000000  125.360001  121.769997  124.529999  123.354774   
    2023-01-09  125.000000  126.610001  124.550003  124.849998  123.671761   
    
                  Volume  
    Date                  
    2023-01-03   8124800  
    2023-01-04   8550700  
    2023-01-05   6046700  
    2023-01-06  10080700  
    2023-01-09   9397900  



.. image:: output_4_1.png


