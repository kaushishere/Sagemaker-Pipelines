import argparse
import os
import logging
import sys

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.utils import resample


logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)


def parse_args():
    logger.info('Parsing arguments')
    parser = argparse.ArgumentParser(description='Data processing')

    parser.add_argument('--input-data', type=str,
        default='/opt/ml/processing/input/data',
    )
    parser.add_argument('--output-train', type=str,
        default='/opt/ml/processing/output/train',
    )
    parser.add_argument('--output-validation', type=str,
        default='/opt/ml/processing/output/validation',
    )
    parser.add_argument('--output-test', type=str,
        default='/opt/ml/processing/output/test',
    )

    return parser.parse_args()

if __name__ == '__main__':
    logger.info('Starated preprocessing. Args: %s', sys.argv)
    
    args = parse_args()
    
    input_csv_path = os.path.join(args.input_data, 'raw_data.csv')
    logger.info('Reading data from %s', input_csv_path)
    df = pd.read_csv(input_csv_path)
    
    logger.info('Starting preprocessing')
    
    # change dt column to a pandas dt object
    df.TransactionDT = pd.to_datetime(df.TransactionDT)
    # card_no to an object dtype
    df.card_no = df.card_no.astype(object)
    # move label column to the left
    df = pd.concat(
    [df.isFraud, df.drop(['isFraud'], axis=1)], axis=1
    )

    # drop transactionID
    df = df.drop(['TransactionID'],axis = 1)
    # sort chronological order
    df = df.sort_values('TransactionDT')
    # create "time since last transaction" feature
    df['time_since_last_transaction'] = df.groupby('card_no').TransactionDT.diff().dt.seconds
    # fill NaN values with median
    df['time_since_last_transaction'] = df['time_since_last_transaction'].fillna(df.time_since_last_transaction.median())

    # create more time features
    df['hour'] = df.TransactionDT.dt.hour
    df['day_of_week'] = df.TransactionDT.dt.dayofweek
    df['day'] = df.TransactionDT.dt.day

    email_domain_mapping = dict(df.email_domain.value_counts())
    df.email_domain = df.email_domain.map(email_domain_mapping)

    # drop card_no
    df = df.drop(['card_no'],axis = 1)
    df = df.drop(['TransactionDT'], axis = 1)

    # convert card_type and ProductCD to one hot encoded vectors
    df = pd.get_dummies(df)

    # upsample minority class so our model doesn't learn to predict "NotFraud" for all examples
    df_minority = df[df.isFraud==1]
    df_majority = df[df.isFraud==0]

    df_minority_upsampled = resample(
        df_minority, 
        replace=True,
        n_samples = len(df_majority)
        )

    df = pd.concat([df_majority, df_minority_upsampled])


    logger.info('Splitting data')
    df_shuffled = df.sample(frac=1, random_state=42)
    df_train, df_rest = train_test_split(df,test_size=0.4,random_state=42)
    df_test, df_validate = train_test_split(df_rest, test_size=0.5)
    
    df_train.to_csv(
        os.path.join(args.output_train, 'train.csv'),
        header=False,
        index=False
    )
    df_validate.to_csv(
        os.path.join(args.output_validation, 'validation.csv'),
        header=False,
        index=False
    )
    df_test.to_csv(
        os.path.join(args.output_test, 'test.csv'),
        header=False,
        index=False
    )
    