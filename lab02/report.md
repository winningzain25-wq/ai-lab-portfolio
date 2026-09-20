# Lab 02 Report

## Objective

This analysis compares articles from two different AI-related blogs using sentiment polarity and noun density.

## Data Sources

The dataset contains 20 articles:

- 10 articles from TechnCruncher
- 10 articles from Top10AI

The `source` column identifies the blog for each article.

## Methodology

### Sentiment Polarity

TextBlob was used to calculate sentiment polarity for each article. Polarity values range from negative to positive, with values above zero indicating positive sentiment.

### Noun Density

spaCy was used to identify nouns. Noun density was calculated as:

Noun Density = Number of Nouns / Number of Valid Tokens

Punctuation, spaces, and other non-content tokens were excluded from the denominator.

## Results

| Source | Mean Sentiment Polarity | Mean Noun Density |
|---|---:|---:|
| TechnCruncher | 0.212661 | 0.265975 |
| Top10AI | 0.185539 | 0.253443 |

### Differences

- Sentiment polarity difference: **0.027122**
- Noun density difference: **0.012532**

TechnCruncher has a higher mean sentiment polarity and a higher mean noun density in this sample. Both sources have positive mean sentiment polarity values according to TextBlob.

## Visualization

The grouped bar chart compares the mean sentiment polarity and mean noun density of the two sources.

The figure is saved as `source_comparison.png`.

## Sample-Size Interpretation

The analysis uses 10 articles from each source. Therefore, the results describe the selected samples rather than the entire websites. The differences should not be treated as representative of all articles published by either source. A larger and more systematic sample would be needed to make stronger generalizations.

## Conclusion

The 20-article sample shows differences between TechnCruncher and Top10AI in both mean sentiment polarity and mean noun density. TechnCruncher has a mean sentiment polarity of 0.212661 compared with 0.185539 for Top10AI, while mean noun density is 0.265975 compared with 0.253443. These results are limited by the small sample size.
