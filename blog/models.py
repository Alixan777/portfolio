from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length = 100)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def newbody(self):
        if len(self.body)>100:
            return self.body[:100]+"..."
        else:
            return self.body

    def date(self):
        now = datetime.now()
        y = self.pub_date.year
        mo = self.pub_date.month
        d = self.pub_date.day
        h = self.pub_date.hour
        m = self.pub_date.minute
        s = self.pub_date.second
        if h+5>23:
            h=h+5-24
        else:
            h +=5
        if now.year - y == 0:
            if now.month - mo ==0:
                return "Posted "+str(now.day - d)+" days "+(str(now.hour-h) if now.hour>h else str(h-now.hour))+" hours "+(str(now.minute-m) if now.minute>m else str(m-now.minute))+" minutes "+(str(now.second-s) if now.second>s else str(s-now.second))+" seconds ago."
            else:
                return "Posted "+(str(now.month - mo)+" month(s) "+str(now.day - d) if now.day>=d else str(now.day+30-d))+" days "+(str(now.hour-h) if now.hour>h else str(h-now.hour))+" hours "+(str(now.minute-m) if now.minute>m else str(m-now.minute))+" minutes "+(str(now.second-s) if now.second>s else str(s-now.second))+" seconds ago."
        else:
            return "Posted "+(str(now.month - mo)+" month(s) "+str(now.day - d) if now.day>=d else str(now.day+30-d))+" days "+(str(now.hour-h) if now.hour>h else str(h-now.hour))+" hours "+(str(now.minute-m) if now.minute>m else str(m-now.minute))+" minutes "+(str(now.second-s) if now.second>s else str(s-now.second))+" seconds ago."
