# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:21:02 2021

@author: 88
"""
import boto3

access_key='42FE4D16E62917AD254E'
secret_key='WzBFRkY0NkQyNDgxQzFDMDRCRUIxNUVDQUIxOTIy'
url='http://10.16.0.1:81'

s3=boto3.resource(
            service_name='s3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            endpoint_url=url,
            verify=False
            )

BUCKET='wxy'
PATH='F:\shixun1\hwk'



