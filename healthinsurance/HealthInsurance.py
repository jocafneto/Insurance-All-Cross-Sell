import pickle
import pandas as pd
import numpy as np

class HealthInsurance( object ):

    def __init__( self ):
        self.home_path = ''
        self.annual_premium_scaler         = pickle.load( open( self.home_path + 'features/annual_premium_scaler.pkl','rb' ) )
        self.age_scaler                    = pickle.load( open( self.home_path + 'features/age_scaler.pkl','rb' ) )
        self.vintage_scaler                = pickle.load( open( self.home_path + 'features/vintage_scaler.pkl', 'rb' ) )
        self.gender_scaler                 = pickle.load( open( self.home_path + 'features/gender_scaler.pkl', 'rb' ) )
        self.region_code_scaler            = pickle.load( open( self.home_path + 'features/region_code_scaler.pkl', 'rb' ) )
        self.vehicle_age_scaler            = pickle.load( open( self.home_path + 'features/vehicle_age_scaler.pkl', 'rb' ) )
        self.policy_sales_channel_scaler   = pickle.load( open( self.home_path + 'features/policy_sales_channel_scaler.pkl', 'rb' ) )

    def data_cleaning( self, df ):
        cols_new = ['id', 'gender', 'age', 'driving_license', 'region_code',
                    'previously_insured', 'vehicle_age', 'vehicle_damage', 'annual_premium',
                    'policy_sales_channel', 'vintage', 'response']
        df.columns = cols_new

        return df

    def feature_engineering( self, df ):
    
        df['region_code'] = df['region_code'].astype('int64')
        df['annual_premium'] = df['annual_premium'].astype('int64')
        df['policy_sales_channel'] = df['policy_sales_channel'].astype('int64')
        
        # vehicle age
        df['vehicle_age'] = df['vehicle_age'].apply( lambda x: 'over_2_years' if x == '> 2 Years' else 'between_1_2_years' if x == '1-2 Year' else 'below_1_year' )
    
        # vehicle damage
        df['vehicle_damage'] = df['vehicle_damage'].apply( lambda x: 1 if x == 'Yes' else 0 )
    
        return df

    def data_preparation( self, df ):
        # annual_premium
        df['annual_premium'] = self.annual_premium_scaler.transform( df[['annual_premium']].values )
    
        # age
        df['age'] = self.age_scaler.transform( df[['age']].values )
    
        # vintage
        df['vintage'] = self.vintage_scaler.transform( df[['vintage']].values )
    
        # gender - Frequency Encoding / *Target Encoding / Weighted Target ENcoding
        df.loc[:, 'gender'] = df['gender'].map( self.gender_scaler )
    
        # region_code - Frequency Encoding / *Target Encoding / Weighted Target ENcoding
        df.loc[:, 'region_code'] = df['region_code'].map( self.region_code_scaler )
        
        # vehicle_age - *One Hot Encoding / Order Encoding / Frequency Encoding / Target Encoding / Weighted Target ENcoding
        df.loc[:, 'vehicle_age'] = df['vehicle_age'].map( self.vehicle_age_scaler )
    
        # policy_sales_channel - Target Encoding / *Frequency Encoding
        df.loc[:, 'policy_sales_channel'] = df['policy_sales_channel'].map( self.policy_sales_channel_scaler )
        
        # select columns
        cols_selected = ['annual_premium', 'vintage', 'age', 'region_code', 'vehicle_damage', 'previously_insured', 'policy_sales_channel']
        
        df = df.fillna(0)

        return df[cols_selected]
    
    def get_prediction( self, model, original_data, test_data ):
        self.threshold = lambda x: 0 if x < 0.31 else 0
        # model prediction
        pred = model.predict_proba( test_data )

        # join prediction into original_data
        original_data['score'] = pred[:, 1].tolist()

        # sort_values
        original_data = original_data.sort_values( 'score', ascending = False )
    
        # threshold
        original_data.loc[:, 'score'] = original_data['score'].map( self.threshold )

        return original_data.to_json( orient='records', date_format='iso')