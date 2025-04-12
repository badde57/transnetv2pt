# implementation from https://github.com/soCzech/TransNetV2
# Pytorch implementation of TransNet V2

## Installation

You can install this package directly from GitHub:

```bash
pip install git+https://github.com/<OWNER>/<REPO>.git@<BRANCH> # Replace with actual repo/branch
```

Or, if you have cloned the repository:

```bash
pip install .
# or for development:
pip install -e .
```

## Usage

```python
from transnetv2pt import predict_video
scenes = predict_video('video.mp4')
```
