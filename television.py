class Television:
    MIN_VOLUME:int =0
    MAX_VOLUME:int=2
    MIN_CHANNEL:int=0
    MAX_CHANNEL:int=3
    def __init__(self: "Television"):
        self.status:bool=False
        self.muted:bool=False
        self.volume:int=Television.MIN_VOLUME
        self.channel:int=Television.MIN_CHANNEL
    def power(self)->None:
        """
        Method that turns on/off tv
        sets status to opposite of current boolean value
        All methods in TV Class Check if status is True
        in order to operate, otherwise methods will simply
        make status=current status (TV is OFF)
        :return: none
        """
        status=self.status
        if status==False:
            status=True
            self.status=status
        else:
            status=False
            self.status=status


    def mute(self)->None:
        """
        Method that sets mute to the opposite
        of its current boolean value
        if mute is true: mute=false
        if mute is false: mute=true
        :return: none
        """

        if self.status==True:
            self.muted=not self.muted
        else:
            self.status=self.status

    def channel_up(self)->None:
        """
        Method that increments channel by 1
        if current channel is less than the minimum channel
        set channel to maximum channel value
        :return: none
        """
        if self.status==True:
            self.channel+=1
            if self.channel>Television.MAX_CHANNEL:
                self.channel=Television.MIN_CHANNEL
        else:
            self.status=self.status

    def channel_down(self)->None:
        """
        Method that decrements channel by 1
        if current channel is less than the minimum channel
        set channel to maximum channel value
        :return: none
        """
        if self.status==True:
            self.channel-=1
            if self.channel<Television.MIN_CHANNEL:
                self.channel=Television.MAX_CHANNEL
        else:
            self.status=self.status
    def volume_up(self)->None:
        """
        Method that increments volume by 1
        if greater than minimum volume
        sets mute to false
        :return: none
        """
        if self.status == True:
            if self.volume <Television.MAX_VOLUME:
                self.volume += 1
            self.muted = False
        else:
            self.status = self.status
    def volume_down(self)->None:
        """
        Method that decrements volume by 1
        if greater than minimum volume
        sets mute to false
        :return: none
        """
        if self.status == True:
            if self.volume>Television.MIN_VOLUME:
                self.volume-=1
            self.muted=False
        else:
            self.status = self.status

    def __str__(self)->str:
        """
        Method shows the status of tv,
        :return: tv status-> power=bool, channel=int,volume=int
        """
        if self.muted:
            return f'Power={self.status}, Channel={self.channel}, Volume={Television.MIN_VOLUME}'
        else:
            return f'Power={self.status}, Channel={self.channel}, Volume={self.volume}'