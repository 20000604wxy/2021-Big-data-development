# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 19:59:13 2021

@author: 88
"""

import doto3
import logging
from connection import s3
 
def createBucket(bucket_name):
	s3.createBucket(Bucket=bucket_name)