def is_admin()
  #test logic
@users_passes_test(admin_test)
admin_view = user_passes_test(is_admin)(admin_view)
def admin_view(request)
#your view logic
return render(*args,*kwargs)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
  if created:
    UserProfile.objects.create(user=instance)
