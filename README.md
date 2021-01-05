# editor

Hi!

this is a very basic django app

the downloads an article and makes a summary of the article. 

The libraries used besides django it self:
1. Spacey
2. Newspaper3k

please note if you haven't installed spacey before, you will need to download a pre-trained model.
The one that i used in my code is the small pretrainen model.

If you run the following code in your terminal, the pretrained model will be downloaded and installed:

python -m spacey download en_core_web_sm


if for whatever reason you want to download the bigger models, you can run the following codes in your terminal

python -m spacey download en_core_web_md

or

python -m spacey download en_core_web_lg

bare in mind you will need to change the "views.py"  file and update it with the model that you used if you change to a medium or large spacey model.

please see below for a link to the youtube video, where i walk through the code:


If you have any questions, please let me know.

thanks

R
