from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

class QuestionList(generics.ListCreateAPIView):
    """
    List questions or create a new question.
    """
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a question.
    """
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Question.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)

class ChoiceList(generics.ListCreateAPIView):
    """
    List choices or create a new choice for a specific question.
    """
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        question = get_object_or_404(Question, pk=question_id)
        return question.choices.all()  # Use the related_name 'choices' here

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return JsonResponse(serializer.data, status=201, headers=headers)
        except Exception as e:
            logger.error("Error creating choice: %s", e)
            return JsonResponse({"error": "Failed to create choice"}, status=400)


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a choice for a specific question.
    """
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        choice_id = self.kwargs['pk']
        # Query the Choice objects associated with the given Question object
        return Choice.objects.filter(question_id=question_id, id=choice_id)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        for user_id in request.data['users']:
            user = User.objects.get(pk=user_id)
            instance.users.add(user)
        instance.save()
        return_data = self.get_serializer(instance)
        return JsonResponse(return_data.data)