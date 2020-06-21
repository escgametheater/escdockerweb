#!/usr/bin/env python3
import json
import mimetypes
from pathlib import Path

import boto3
import botocore

MEDIA_DIR = Path('/home/esc-minio/s3_backup')

def main():
    s3 = boto3.resource('s3', endpoint_url='http://localhost:9000')

    for bucket_name in ('game-build-assets'):
        try:
            s3.meta.client.head_bucket(Bucket=bucket_name)
        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                s3.Bucket(bucket_name).create()
                s3.BucketPolicy(bucket_name).put(Policy=json.dumps({
                  "Version": "2017-05-03",
                  "Statement": [
                    {
                      "Sid": "AddPerm",
                      "Effect": "Allow",
                      "Principal": "*",
                      "Action": ["s3:GetObject"],
                      "Resource": ["arn:aws:s3:::{}/*".format(bucket_name)]
                    }
                  ]
                }))

    for bucket in s3.buckets.all():
        print("{name}\t{created}".format(name=bucket.name,
                                         created=bucket.creation_date))


if __name__ == '__main__':
    main()
