from .models import Community

def top_communities(request):
    top_community = Community.objects.all()[:3]
    return {'top_community': top_community}
