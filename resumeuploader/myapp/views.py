from django.shortcuts import render
from django.views import View
from .models import Resume
from .forms import ResumeForm

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'myapp/home.html', {'candidates': candidates, 'form': form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        candidates = Resume.objects.all()

        if form.is_valid():
            form.save()
            form = ResumeForm()  # Reset the form on success
            message = {'success': 'Resume uploaded successfully!'}
        else:
            message = {'error': 'There was an error in your submission.'}

        return render(request, 'myapp/home.html', {**message, 'form': form, 'candidates': candidates})

class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html', {'candidate': candidate})
