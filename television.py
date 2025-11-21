class Television:
    MIN_VOLUME=0
    MAX_VOLUME=2
    MIN_CHANNEL=0
    MAX_CHANNEL=3
    def __init__(self):
        self.status=False
        self.muted=False
        self.volume=Television.MIN_VOLUME
        self.channel=Television.MIN_CHANNEL
    def power(self):
        status=self.status
        if status==False:
            status=True
            self.status=status
        else:
            status=False
            self.status=status


    def mute(self):
        if self.status==True:
            self.muted=not self.muted
        else:
            self.status=self.status

    def channel_up(self):
        if self.status==True:
            self.channel+=1
            if self.channel>=Television.MAX_CHANNEL:
                self.channel=Television.MIN_CHANNEL
        else:
            self.status=self.status

    def channel_down(self):
        pass
    def volume_up(self):
        pass
    def volume_down(self):
        pass

    def __str__(self):
        if self.muted:
            return f'Volume={Television.MIN_VOLUME}'
        else:
            return f'XXX'