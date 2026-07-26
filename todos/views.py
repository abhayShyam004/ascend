import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task

def todo_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            last_task = Task.objects.order_by('position').last()
            new_pos = (last_task.position + 1) if last_task else 0
            Task.objects.create(title=title, position=new_pos)
        return redirect('todo_list')
        
    tasks = Task.objects.all()
    return render(request, 'todos.html', {'tasks': tasks})

@csrf_exempt
def reorder_tasks(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            task_ids = data.get('task_ids', [])
            for index, task_id in enumerate(task_ids):
                Task.objects.filter(id=task_id).update(position=index)
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'invalid method'}, status=405)
