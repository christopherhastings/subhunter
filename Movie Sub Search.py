#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pysrt
import pandas as pd

pd.set_option('display.max_rows', None)


# In[35]:


# This is the array of your movie SRT files. 
movie_list = ['SRT/The.Shawshank.Redemption.1994.1080p.x264.YIFY.srt','SRT/Batman.The.Dark.Knight.2008.1080p.BluRay.x264.YIFY.srt','SRT/V.For.Vendetta.2006.1080p.BrRip.x264.YIFY.srt','SRT/Armageddon.1998.1080p.BrRip.x264.YIFY.srt']


# In[36]:


def word_search(word, movie_list):
    for x in movie_list:
        final_df = movie_search(x)
        display(x)
        display(final_df[final_df['Text'].str.contains(word)])


# In[37]:


def movie_search(sub):
    subs = pysrt.open(str(sub), encoding='iso-8859-1')
    final_df = pd.DataFrame(columns=['Start Hour','Start Min', 'Start Sec','End Hour', 'End Min', 'End Sec', 'Text'])

    for line in subs: 

        to_append = [line.start.hours, line.start.minutes, line.start.seconds, line.end.hours, line.end.minutes,line.end.seconds,line.text]
        df_length = len(final_df)
        final_df.loc[df_length] = to_append
    return final_df


# In[ ]:


#
# Add the word or phrase as the first positional argument. 
# The second positional argument is the link to an SRT file. 
# The second positional argument also supports an array of SRT files. 
#

word_search("My God", movie_list)


# In[ ]:




