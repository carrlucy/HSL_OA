
![UVA HSL logo](https://user-images.githubusercontent.com/61550284/121027476-fd048e00-c774-11eb-963c-320792136746.jpg)

This is a project by UVA Claude Moore Health Sciences Library 


Studying the open access publication patterns of UVA Health faculty and staff
Getting started is simple
Set up a github repo - you're certainly welcome to fork ours here https://github.com/carrlucy/HSL_OA
Set up a streamlit share account https://share.streamlit.io/ this may take a day or two - so plan ahead :)
Connect the two - there are some pictures here https://guides.hsl.virginia.edu/it-services-blog/zoombites/Geopandas-and-streamlit-to-display-local-tree-data-in-deckgl
Now we're off to the races - you should have a URL where your app is going to be showing up every time your github code gets updated https://share.streamlit.io/carrlucy/hsl_oa/main is our app link

Tech notes... Caching.... it's a thing
I feel like a jerk for not testing the streamlit caching tools in the past.  They're amazing.  What a difference it makes with these larger queries.  Just add @st.cache() before a function and it the results get cached... done.  We do all the processing in the pandas data frame after that and it's super speedy

Creating a development app was a great way to test against our main code - we

forked a development branch on github and 
selected the new branch on streamlit sharing
Boom! new app to test on https://share.streamlit.io/carrlucy/hsl_oa/development
The gift of gab
Every aspect of this process is open source, and all the development and support involves real people.  Introduce yourself to the community.  The groups we reached out to in working on this project included

EuropePMC group has a google group section https://groups.google.com/a/ebi.ac.uk/g/epmc-webservices
I posted here one day because we were having difficulty using the next cursor tools with our XML parser - within 24 hours a researcher, Dr. Maaly Nassar who works at EMBL in the McEntyre Literature Services Team was able to identify an improved method to use their API using JSON... 

Streamlit - https://discuss.streamlit.io/ is the forum for working with the Streamlit community
The streamlit sharing section was helpful for me https://discuss.streamlit.io/c/streamlit-sharing/13
These folks are also on Twitter https://twitter.com/streamlit and Randy Zwitch https://twitter.com/randyzwitch is their community development partner.  They are a tremendously responsive team...

Stack Overflow - i know this seems obvious... but yeah
https://stackoverflow.com/questions/67243829/restful-pagination-using-python-elementree-xml-parser-and-loop no one answered the question, but it was very helpful for me to write down the problem i was having... 
You?
If you have ideas or insights in to how we can improve this project we'd like to hear from you - my email is adp6j@virginia.edu 
