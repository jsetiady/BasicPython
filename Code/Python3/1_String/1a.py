# Copy-Paste dan Run program ini
from datetime import datetime
now = datetime.now()

print ('%s/%s/%s' % (now.month, now.day, now.year))
print ('%s:%s:%s' % (now.hour, now.minute, now.second))