import unittest
from data_analysis import analyze_sentiment

class TestDataAnalysis(unittest.TestCase):
    def test_analyze_sentiment_positive(self):
        text = 'Great news about Bitcoin!'
        result = analyze_sentiment(text)
        self.assertEqual(result, 'Positive')

    def test_analyze_sentiment_negative(self):
        text = 'Bitcoin prices crashing!'
        result = analyze_sentiment(text)
        self.assertEqual(result, 'Negative')