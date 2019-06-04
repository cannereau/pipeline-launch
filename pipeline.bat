@echo off

7z a -tzip pipeline.zip pipeline.py
aws lambda update-function-code --function-name pipeline-launch --zip-file fileb://pipeline.zip --output table
del pipeline.zip
