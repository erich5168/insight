# Insight

Personal Financial Analysis Agent.  

Status:
- Complete loading singular file
- Cleaning / Sanitization layer inplace
- Symple aggregation

> Note: Check Technical_Context_Summary:
>
> All the technical elements of this snapshot.


## How to get Started

### 1. Rebuild the environment from `uv.lock`
```
uv sync
```

### 2. Run your script
```
uv run python src/insight/sandbox/data_wrangling/load.py

uv run python src/insight/sandbox/data_wrangling/poc_clean_magnitude.py
```

