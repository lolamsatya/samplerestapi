from rest_framework import serializers

from .models import FrequentlyAskedQuestions

class FrequentlyAskedQuestionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestions
        fields = ('id', 'question', 'answer')