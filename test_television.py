import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_tv_sequence(tv):
    # Initial state
    assert str(tv) == 'Power=False, Channel=0, Volume=0'
    tv.power()
    assert str(tv) == 'Power=True, Channel=0, Volume=0'

    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.volume_up()
    assert str(tv) == 'Power=True, Channel=3, Volume=1'
    tv.channel_up()
    assert str(tv) == 'Power=True, Channel=0, Volume=1'

    tv.channel_down()
    tv.volume_up()
    assert str(tv) == 'Power=True, Channel=3, Volume=2'
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == 'Power=True, Channel=3, Volume=0'
    tv.volume_down()
    assert str(tv) == 'Power=True, Channel=3, Volume=0'

    #tv off
    tv.power()
    assert str(tv) == 'Power=False, Channel=3, Volume=0'
    #should still be the same
    tv.volume_up()
    tv.channel_down()
    assert str(tv) == 'Power=False, Channel=3, Volume=0'

    #status=true
    tv.power()
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == 'Power=True, Channel=3, Volume=2'

    # new tv
    tv2 = Television()
    tv2.power()
    tv2.channel_up()
    tv2.volume_up()
    assert str(tv2) == 'Power=True, Channel=1, Volume=1'

    # mute
    #calling tv1 not 2
    tv.mute()

    assert str(tv) == 'Power=True, Channel=3, Volume=0'
    # tv 1 volume is 2
    tv.volume_down()
    assert str(tv) == 'Power=True, Channel=3, Volume=1'

    tv.mute()
    assert str(tv) == 'Power=True, Channel=3, Volume=0'

    tv2.volume_up()
    assert str(tv2) == 'Power=True, Channel=1, Volume=2'

    tv.power()
    tv.mute()
    assert str(tv) == 'Power=False, Channel=3, Volume=0'
    tv2.power()
    assert str(tv2) == 'Power=False, Channel=1, Volume=2'
