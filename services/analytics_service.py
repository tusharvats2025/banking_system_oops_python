import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from pathlib import Path

class AnalyticsService:
    """Big data analytics"""
    def __init__(self):
        self.transactions_df = None

    def load_transactions(self, csv_path: str = 'data/synthetic_data.csv'):
        """Load transaction data"""
        try:
            if Path(csv_path).exists():
                self.transactions_df = pd.read_csv(csv_path)
                return True
        except:
            pass
        return False
    
    def get_statistics(self) -> dict:
        """Calculate metrics"""
        if self.transactions_df is None or self.transactions_df.empty:
            return {}
        
        df = self.transactions_df
        return {
            'total_transactions': len(df),
            'total_volume': float(df['amount'].sum()),
            'avg_transaction': float(df['amount'].mean()),
            'fraud_count': int(df['is_fraud'].sum()) if 'is_fraud' in df else 0,
            'fraud_rate': float((df['is_fraud'].sum() / len(df) * 100)) if 'is_fraud' in df else 0
        }
    def get_transaction_by_type(self) -> dict:
        """Group by type"""
        if self.transactions_df is None:
            return {}
        return self.transactions_df.groupby('type')['amount'].agg(['count', 'sum', 'mean']).to_dict()
    
    def detect_spending_patterns(self) -> dict:
        "K-means clustering"
        if self.transactions_df is None or len(self.transactions_df) < 10:
            return {}
        try:
            df = self.transactions_df.copy()
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['hour'] = df['timestamp'].dt.hour

            features = df[['amount', 'hour']].values
            kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
            df['cluster'] = kmeans.fit_predict(features)

            patterns = {}
            for cluster in range(3):
                cluster_data = df[df['cluster'] == cluster]
                patterns[f'pattern_{cluster}'] = {
                    'avg_amount' : float(cluster_data['amount'].mean()),
                    'count': int(len(cluster_data)),
                    'common_time': int(cluster_data['hour'].mode()[0]) if len(cluster_data) > 0 else 0
                }
            return patterns
        except:
            return {}
        