from django.db import models


HOLES_NUMBER = (
    ('18', '18'),
    ('9', '9'),
)



class TeeTimes(models.Model):
  # date_time                  = models.DateTimeField()
  date                       = models.DateField()
  time                       = models.TimeField()
  is_reserved                = models.BooleanField('Is Reserved', default=False, null=False, blank=False)
  is_using_cart              = models.BooleanField('Using Cart', default=False, null=False, blank=False)
  player_count               = models.IntegerField('Player Count',default=0)
  holes                      = models.CharField('Holes Playing', max_length=2, choices=HOLES_NUMBER, default='18')
  player_1_name              = models.CharField('Player 1 Name', max_length=100, null=True, blank=True)
  player_2_name              = models.CharField('Player 2 Name', max_length=100, null=True, blank=True)
  player_3_name              = models.CharField('Player 3 Name', max_length=100, null=True, blank=True)
  player_1_is_checkedin      = models.BooleanField('Player 1 Checked In', default=False, null=False, blank=False)
  player_2_is_checkedin      = models.BooleanField('Player 2 Checked In', default=False, null=False, blank=False)
  player_3_is_checkedin      = models.BooleanField('Player 3 Checked In', default=False, null=False, blank=False)

  def __str__(self):
      return str(self.date) + " " + str(self.time) + " - " + self.player_1_name

  class Meta:
      verbose_name = 'Tee Times'
      verbose_name_plural = 'Tee Times'


