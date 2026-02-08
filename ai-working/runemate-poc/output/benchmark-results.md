
## Runemate Forge: Compression Benchmark Results

| File | Original | Staves | Ratio | PQ Overhead | Net | PQ Offset? |
|------|----------|--------|-------|-------------|-----|-----------|
| bci-alert.html | 2,393 B | 856 B | 64.2% | +23,666 B | -22,129 B | NO |
| bci-dashboard.html | 20,633 B | 4,353 B | 78.9% | +23,666 B | -7,386 B | NO |
| bci-settings.html | 10,500 B | 3,355 B | 68.0% | +23,666 B | -16,521 B | NO |

### Total Transmission Comparison

| File | Classical+HTML | PQ+HTML | PQ+Staves | vs Classical |
|------|---------------|---------|-----------|-------------|
| bci-alert.html | 11,905 B | 35,571 B | 34,034 B | +22,129 B |
| bci-dashboard.html | 30,145 B | 53,811 B | 37,531 B | +7,386 B |
| bci-settings.html | 20,012 B | 43,678 B | 36,533 B | +16,521 B |