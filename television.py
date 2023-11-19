class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        This function creates the television object and sets the volume and channel at the minimum values
        """
        self.__muted = False
        self.__status = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        This function turns the television on or off
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        This function mutes or unmutes the television when the television is on
        """
        if self.__status == True:
            self.__muted = not self.__muted


    def channel_up(self) -> None:
        """
        This function moves the channel up when the television is on
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        This function moves the channel down when the television is on
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None :
        """
        This function moves the volume up when the television is on
        """
        if self.__status == True:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        This function moves the volume up when the television is on
        """
        if self.__status == True:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        This function returns the values of Power, Channel and Volume
        :return: Present values of Power, Channel, and Valume
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
