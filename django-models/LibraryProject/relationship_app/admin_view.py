def is_admin()
  #test logic
@user_passes_test(admin_test)
admin_view = user_passes_test(is_admin)(admin_view)
def admin_view(request)
#your view logic
return render(*args,*kwargs)
