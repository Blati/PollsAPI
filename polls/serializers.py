from .models import Vote, Poll, Choice, PollMain
from rest_framework import serializers


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('poll', 'choice')

    def create(self, validated_data):
        validated_data['voted_by'] = self.context.get('request', None).session._get_or_create_session_key()
        return Vote.objects.create(**validated_data)


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = "__all__"


class PollMainSerializer(serializers.ModelSerializer):
    polls = PollSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = PollMain
        fields = '__all__'
