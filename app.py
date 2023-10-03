#use urllib.request to get the data from the url
#returns a response

#import urllib
import urllib.request as urllib

print("This is a site connectivity checker program")
input_url = input("Input the url of the site: ")

#write a function that takes a url
def main(url):
    print("Checking connectivity ")

    #open up url
    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
