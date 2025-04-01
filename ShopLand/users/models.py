#from django.db import models
#from django.contrib.auth.models import AbstractUser
#from django.utils.translation import gettext_lazy as _
#from django.utils import timezone
#from django.contrib.auth.models import PermissionsMixin
# Create your models here.



#class CustomUser(AbstractUser, PermissionsMixin):
    
 #   first_name = models.CharField(_('first name'), max_length=150, blank=True)
  #  last_name = models.CharField(_('last name'), max_length=150, blank=True)
   # email = models.EmailField(_('email'), unique=True)
    #phone = models.CharField(_('phone'), max_length=15, blank=True)
   # is_active = models.BooleanField(_('active'), default=True)
   # is_staff = models.BooleanField(_('staff'), default=False)
   # date_joined = models.DateTimeField(_('date joined'), default=timezone.now)


    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []
    #class Meta:
     #   verbose_name = _('user')
      #  verbose_name_plural = _('users')
   # def get_full_name(self):
    #    return f"{self.first_name} {self.last_name}"