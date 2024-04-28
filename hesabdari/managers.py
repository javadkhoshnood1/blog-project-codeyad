from django.db import models


### شخصی سازی متدها
class CustomerManagers(models.Manager):
    def customer_javad(self):
        return self.filter(name="جواد خشنود")
