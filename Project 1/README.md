# Project 1

### Portfolio 1 Construction
The portfolio is intended to be exposed to a global market. As such its weights are designed to be a function of each coutry's or continent's population.
I chose ETF's that, when taken as a group, represented the globe.
Their weight were set soley on the percentage of the global population that resides in their borders.

Europe: SPEU

North America: SPY(USA),EWC(Canada),EWW(Mexico)

South America: ILF

Asia: AAXJ(or all of Asia excluding Japan), EWJ(Japan)

Africa: AFK

Australia: EWA

|      | Pop           | Percent |
|------|---------------|---------|
| SPEU | 748,373,324   | 9.83%   |
| SPY  | 331,449,281   | 4.35%   |
| EWC  | 38,010,000    | 0.50%   |
| EWW  | 128,900,000   | 1.69%   |
| ILF  | 438,039,141   | 5.75%   |
| AAXJ | 4,564,200,000 | 59.93%  |
| EWJ  | 125,800,000   | 1.65%   |
| AFK  | 1,216,000,000 | 15.97%  |
| EWA  | 25,690,000    | 0.34%   |
|      | 7,616,461,746 | 100.00% |

### Portfolio 2 Construction
This portfolio, while using the same nine ETFs from the first portfolio, distributes the weight via the GDP of each ETFs region as a percentage of the global GDP.

| Tick | GDP                | Percent     |
|------|--------------------|-------------|
| SPEU | 17,100,000,000,000 | 21.31%      |
| SPY  | 20,900,000,000,000 | 26.05%      |
| EWC  | 1,643,000,000,000  | 2.04%       |
| EWW  | 1,076,000,000,000  | 1.34%       |
| ILF  | 3,990,000,000,000  | 4.97%       |
| AAXJ | 26,515,000,000,000 | 33.05%      |
| EWJ  | 5,065,000,000,000  | 6.31%       |
| AFK  | 2,600,000,000,000  | 3.24%       |
| EWA  | 1,331,000,000,000  | 1.65%       |
|      | 80,220,000,000,000 | 100.00%     |

Using python and yahoo finance I have pulled the data for each of these ETF's for the last 10 years.
