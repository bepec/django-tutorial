import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from polls.models import Poll


class PollTest(TestCase):

    def test_was_published_recently_with_future_pub_date(self):
        """
        was_published_recently should return False
        if pub_date is in future
        """
        future = timezone.now() + datetime.timedelta(days=30)
        future_poll = Poll(pub_date=future)
        self.assertFalse(future_poll.was_published_recently())

    def test_was_published_recently_with_old_pub_date(self):
        """
        was_published_recently should be False if the poll
        is older than 1 day
        """
        past = timezone.now() - datetime.timedelta(days=2)
        poll = Poll(pub_date=past)
        self.assertFalse(poll.was_published_recently())

    def test_was_publiched_recently_with_recent_pub_date(self):
        """
        """
        recent = timezone.now() - datetime.timedelta(hours=20)
        poll = Poll(pub_date=recent)
        self.assertTrue(poll.was_published_recently())


def create_poll(question, days):
    date = timezone.now() + datetime.timedelta(days=days)
    return Poll.objects.create(question=question, pub_date=date)


class PollViewTest(TestCase):

    def test_index_with_no_polls(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "No polls")
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

    def test_index_with_past_poll(self):
        create_poll(question="past", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
            ['<Poll: past>'])

    def test_index_view_with_a_future_poll(self):
        create_poll(question="future", days=1)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

    def test_index_with_two_past_poll(self):
        create_poll(question="1", days=-1)
        create_poll(question="2", days=-2)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
            ['<Poll: 1>', '<Poll: 2>'])
