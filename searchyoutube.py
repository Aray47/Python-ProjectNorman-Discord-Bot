import urllib.request
import urllib.parse
import re
import sys



def main():
    searchYT()

def searchYT():
    uI = input('Type in a video to search: ')
    query_string = urllib.parse.urlencode({"search_query" : uI})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("http://www.youtube.com/watch?v=" + search_results[0])
    print("http://www.youtube.com/watch?v=" + search_results[1])
    print("http://www.youtube.com/watch?v=" + search_results[2])
    






    
if __name__ == '__main__':
    sys.exit(main())


