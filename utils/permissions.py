from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
        

class IsAdmin(BasePermission): 
    def has_permission(self, request, view):
        admin = request.user.user_type ==3
        return bool(
             super().has_permission(request, view)
             and (admin)
            )      
class IsClientOrAdmin(BasePermission): 
    def has_permission(self, request, view):
        client = request.user.user_type ==2
        admin = request.user.user_type ==3
        return bool(
             super().has_permission(request, view)
             and (client or admin)
            )

class IsGuestOrAdmin(BasePermission): 
    def has_permission(self, request, view):
        guest = request.user.user_type ==4
        admin = request.user.user_type ==3
        return bool(
             super().has_permission(request, view)
             and (guest or admin)
            )
        

class IsQuizOrAdmin(BasePermission): 
    def has_permission(self, request, view):
        quiz = request.user.user_type ==5
        admin = request.user.user_type ==3
        return bool(
             super().has_permission(request, view)
             and (quiz or admin)
            )

class IsQuickresponseOrAdmin(BasePermission): 
    def has_permission(self, request, view):
        quizresponse = request.user.user_type ==6
        admin = request.user.user_type ==3
        return bool(
             super().has_permission(request, view)
             and (quizresponse or admin)
            )

# class IsCustomerOrClientOrAdminOrGuestOrQuizOrQuizresponse(BasePermission): 
#     def has_permission(self, request, view):
#         customer = request.user.user_type ==1
#         client = request.user.user_type ==2
#         admin = request.user.user_type ==3
#         guest = request.user.user_type ==4
#         quiz = request.user.user_type ==5
#         quizresponse = request.user.user_type ==6
#         return bool(
#              super().has_permission(request, view)
#              and (client or admin or customer or guest or quiz or quizresponse)
#             )