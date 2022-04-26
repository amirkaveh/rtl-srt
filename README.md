# RTL-SRT

## Description
This script fixes Persian .SRT subtitles right-to-left direction. It simply adds a Right-To-Left Embedding charachter to the beginning of each line that contains persian characters. 

این اسکریپت جهت نمایش زیرنویس های فارسی را به صورت راست به چپ تنظیم می کند تا به هم ریختگی آن در بعضی از نرم افزارهای پخش فیلم برطرف شود. 

### Sample 1
Before fix:

<img src="https://user-images.githubusercontent.com/20387401/165393883-a693a16b-b7ce-4c69-bb2c-a4cf8598393d.png" width="350">

After fix:

<img src="https://user-images.githubusercontent.com/20387401/165394230-19bdc7db-39e7-4901-a29c-e31c0bb080a4.png" width="350">

### Sample 2
Before fix:

<img src="https://user-images.githubusercontent.com/20387401/165395027-3fdc6539-eb7a-4080-a93f-272e1b594827.png" width="350">

After fix:

<img src="https://user-images.githubusercontent.com/20387401/165394853-2dac00d9-8e7f-41f5-bdc9-c30a8f09e9de.png" width="350">

## Requirements
It requires:
1. Python 3
2. pip requirements

You can install pip requirements by running the following command under the project directory:

`pip install -r requirements.txt`

## Usage
Just run either of these under the project directory.

`python main.py /path/to/subtitle.srt [overwrite]`

or

`./main.py /path/to/subtitle.srt [overwrite=False]`

Make sure `main.py` is executable before running the second command.

Giving the overwrire argument is optional. Possible values are 'True' and 'False'. Default value is 'False'.

The script will overwrite the existing file or creating a new file with the pattern `subtitle_modified.srt` under the same direcotry as provided `subtitle.srt`.
