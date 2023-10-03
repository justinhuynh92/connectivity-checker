#import urllib
import urllib.request as urllib

#write a function that takes a url
def main(url):
    print("Checking connectivity ")

    #use urllib.request to get the data from the url
    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was:", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the url of the site: ")

#return a response
main(input_url)
