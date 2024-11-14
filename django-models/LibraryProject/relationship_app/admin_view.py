def is_admin()
  #test logic
@user_passes_test(admin_test)
def admin_view(request)
#your view logic
return render(*args,*kwargs)
