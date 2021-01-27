from rest_framework import generics
from rest_framework.response import Response

from .models import Poll, Choice, PollMain, Vote

from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, PollMainSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PollMainListGeneric(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = PollMain.objects.all()
    serializer_class = PollMainSerializer


class PollListGeneric(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetailGeneric(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class VoteDetailGeneric(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        q_poll = Poll.objects.filter(id=serializer.data['poll'])
        q_poll_main = PollMain.objects.filter(id=q_poll.values()[0]['poll_id'])
        q_choice = Choice.objects.filter(id=serializer.data['choice'])
        data = {
            "poll_main_name": q_poll_main.values()[0]['poll_main_name'],
            "poll_name": q_poll.values()[0]['poll_name'],
            "poll_text": q_poll.values()[0]['poll_text'],
            "choice": q_choice.values()[0]['choice_text']
        }
        return Response(data)


class ChoiceList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer

