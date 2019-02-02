# Energy Trading API Wrappers
API Wrappers for Energy Markets Data from publicly available sources.

> **disclaimer** While readily useable, this API library is under constant in development. Enjoy!

Supported APIs:

- [WA Gas Bulletin Board](https://gbbwa.aemo.com.au/)

## Installation
* Python 3.6 or 3.7

To install,  use `pip` :
```bash
$ pip install energy-trading-api
```

### Requirements
* Python 3.7


## Usage

### Western Australia Gas Bulletin Board
```python
from energy_trading_api import wagbb
wagbb.capacityOutlook()
```    
[WAGBB API Documentation](https://gbbwa.aemo.com.au/api/v1/document/1f2bc41e-3e42-41eb-86f7-4a10d2d6e4bc/content)
