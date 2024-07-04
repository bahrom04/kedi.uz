from apps.book.models import Community
from allauth.socialaccount.models import SocialAccount

def top_communities(request):
    top_community = Community.objects.all()[:3]
    socialaccount_obj = SocialAccount.objects.filter(
                provider="google", user_id=request.user.id
            )
    return {'top_community': top_community, "socialaccount_obj": socialaccount_obj}
