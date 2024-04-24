from rest_framework import serializers
from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes', 'users']

    def update(self, instance, validated_data):
        instance.choice_text = validated_data.get('choice_text', instance.choice_text)
        # Update the votes field if it's present in the validated_data
        if 'votes' in validated_data:
            instance.votes = validated_data['votes']
        instance.save()
        return instance

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'created_at', 'choices']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question