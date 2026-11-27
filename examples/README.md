# Original fixture and offline checks

Start with [flow-samples.csv](flow-samples.csv), which describes the fictional reading at each integer minute. It records the assigned sample at the switch, not the approached rate from the left. See the [rate graph](../figures/valve-flow.svg) for the two-sided distinction. From the repository root, reproduce the exact arithmetic and selected edge cases with standard-library Python:

```sh
python3 examples/check-calculus.py
```

These checks do not use a live sensor, account or model.
