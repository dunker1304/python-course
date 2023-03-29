# 1. Collections Modules
```
  from collections import Counter
  
  list = ['a', 'a', 1, 1, 1, 1]
  Counter(list)
  Counter('asdancncncbbaaacbac')
```

```
  from collections import defaultdict
  d = defaultdict(lambda: 0)

  from collections import namedtuple
```
## python OS module
```
  import os
  import shutil
```

## Datetime module
```
  import datetime
```

## Math and Random module
```
  import math
  #help(math)
  import random

  random.choice()
  random.choices()
  random.sample()
  random.uniform()
  random.gauss()
```

## Python debugger
```
  import pdb

  pdb.set_trace()
```

## Python regular expression
```
  import re
  re.match(pattern, text)
  re.findall(pattern, text)
  re.finditer(pattern, text)

```