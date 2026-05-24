#!/usr/bin/env python3
"""
Crypto Sentiment Analyzer - Analyze market sentiment from social media and news
Tracks fear/greed index and social sentiment

BTC Tips: 1KPUa9Njq86NJwmwqVmdjZ4oC8eHrXKqf9
"""
import json
import urllib.request
import sys
from datetime import datetime

def get_fear_greed_index():
    """Fetch Crypto Fear & Greed Index"""
    url = "https://api.alternative.me/fng/?format=json"
    req = urllib.request.Request(url, headers={'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read())

def display_sentiment():
    """Display sentiment analysis"""
    print("=" * 70)
    print("CRYPTO SENTIMENT ANALYZER")
    print(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    try:
        data = get_fear_greed_index()
        index = data['data'][0]['value']
        classification = data['data'][0]['value_classification']
        
        print(f"\nFear & Greed Index: {index} ({classification})")
        
        if int(index) <= 25:
            print("🔴 EXTREME FEAR - Historically good buying opportunity")
        elif int(index) <= 45:
            print("🟠 FEAR - Market is undervalued")
        elif int(index) <= 55:
            print("🟡 NEUTRAL - Balanced market")
        elif int(index) <= 75:
            print("🟢 GREED - Market is overvalued")
        else:
            print("🔴 EXTREME GREED - Historically good selling opportunity")
        
        print(f"\nHistorical Context:")
        print(f"  - Extreme Fear (<25): Buy signal")
        print(f"  - Extreme Greed (>75): Sell signal")
        print(f"  - Current: {classification}")
        
    except Exception as e:
        print(f"Error fetching sentiment: {e}")
    
    print(f"\nBTC Tips: 1KPUa9Njq86NJwmwqVmdjZ4oC8eHrXKqf9")

def main():
    display_sentiment()

if __name__ == "__main__":
    main()
