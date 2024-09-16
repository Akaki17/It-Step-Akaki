

from abc import ABC, abstractmethod


class Play(ABC):
    
    @abstractmethod
    def play(self):
        pass
    
class Pause(ABC):
    @abstractmethod
    def pause(self):
        pass

class Stop(ABC):
    @abstractmethod
    def stop(self):
        pass
    
class Rewindable(ABC):
    @abstractmethod
    def rewindable(self):
        pass
    
class FastForward(ABC):
    @abstractmethod
    def fastForward(self):
        pass
    
    

class AudioPayer(Play, Pause, Stop):
    def play(self):
        print('Playing audio')
        
    def pause(self):
        print('Pausing audio')
        
    def stop(self):
        print('Stopping audio')
        
        
        
class VideoPlayer(Play, Pause, Stop, Rewindable, FastForward):
    def play(self):
        print('Playing video')
    
    def pause(self):
        print('Pausing video')
        
    def stop(self):
        print('Stopping video')
        
    def rewindable(self):
        print('Rewinding video')
        
    def fastForward(self):
        print('Fast forwarding video')



class StreamingPlayer(Play, Pause, Stop):
    def play(self):
        print('Playing stream')
    
    def pause(self):
        print('Pausing stream')
        
    def stop(self):
        print('Stopping stream')
    


def main():
    audio_player = AudioPayer()
    video_Player = VideoPlayer()
    streaming_player = StreamingPlayer()
    
    audio_player.play()
    audio_player.pause()
    audio_player.stop()
    
    video_Player.play()
    video_Player.rewindable()
    video_Player.fastForward()
    video_Player.pause()
    video_Player.stop()
    
    streaming_player.play()
    streaming_player.pause()
    streaming_player.stop()

if __name__ == '__main__':
    main()