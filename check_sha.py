import hashlib
f=open(rC:/Users/jinting.yuan/KimiReports/site/index.html,rb)
print(hashlib.sha1(f.read()).hexdigest())
