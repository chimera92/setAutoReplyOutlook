import urllib
from lxml import html
from subprocess import Popen, PIPE


tree = html.fromstring(urllib.urlopen("https://www.mozilla.org/en-US/firefox/organizations/notes/").read())
version=tree.xpath('//*[@class="version"]/h2/text()')[0]


process = Popen(['powershell.exe', 'getFirefoxVersion.ps1'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
# print stdout
# print stderr
current_version=stdout.strip()
if(version==current_version):
    print "Already up-to-date"
    pass
else:
    urllib.urlretrieve('https://download.mozilla.org/?product=firefox-esr-latest-ssl&os=win&lang=en-US',"Firefox Setup {}esr.exe".format(version))




